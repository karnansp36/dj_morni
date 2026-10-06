#rate limiting
from django.core.cache import cache
from django.http import HttpResponse

#need to limit 5 req per minute per ip address, if exceeded return 429 error
class RateLimitingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = self.get_client_ip(request)
        cache_key = f"rate_limit_{ip_address}"
        request_count = cache.get(cache_key, 0)

        if request_count >= 5:
            return HttpResponse("Too Many Requests", status=429)

        cache.set(cache_key, request_count + 1, timeout=60)  # Set timeout to 60 seconds
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip