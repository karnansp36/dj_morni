from django.shortcuts import get_object_or_404, render, redirect
from .forms import SocialPostForm
from user_post.utils import auth_required
from django.contrib import messages
from django.db.models import Count, Exists, OuterRef
from django.views.decorators.http import require_POST
from .models import Comment, Like, SocialPost
# Create your views here.

@auth_required
def SocialPostView(request):
    if request.method == "POST":
        form = SocialPostForm(request.POST, request.FILES)
        if form.is_valid():
            userdata= form.save(commit=False)
            userdata.user_id = request.session['user_id']
            userdata.save()
            messages.success(request, "Post created successfully!")
            return redirect('profile')  # Redirect to the profile page after successful submission
        else:
            messages.error(request, "Please correct the errors below.")
            return redirect('social_post')  # Redirect back to the form page if there are errors
    return render(request, "social_post.html", {"form": SocialPostForm()})

@auth_required
def SocialPostListView(request):
    user_id = request.session['user_id']
    posts = SocialPost.objects.select_related('user').annotate(
        like_count=Count('likes'),
        is_liked=Exists(Like.objects.filter(post_id=OuterRef('pk'), user_id=user_id)),
    ).prefetch_related('comments__user')
    return render(request, "social_post_list.html", {"posts": posts})


@auth_required
@require_POST
def ToggleSocialPostLikeView(request, post_id):
    post = get_object_or_404(SocialPost, pk=post_id)
    like, created = Like.objects.get_or_create(
        post=post,
        user_id=request.session['user_id'],
    )
    if not created:
        like.delete()
    return redirect('social_post_list')


@auth_required
@require_POST
def SocialPostCommentView(request, post_id):
    post = get_object_or_404(SocialPost, pk=post_id)
    content = request.POST.get('content', '').strip()
    if content:
        Comment.objects.create(
            post=post,
            user_id=request.session['user_id'],
            content=content,
        )
    else:
        messages.error(request, "A comment cannot be empty.")
    return redirect('social_post_list')