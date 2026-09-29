from django.shortcuts import redirect


def auth_required(func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('login')  # Redirect to your login URL
        return func(request, *args, **kwargs)
    return wrapper