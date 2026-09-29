from django.shortcuts import render, redirect
from .forms import SocialPostForm
from user_post.utils import auth_required
from django.contrib import messages
from .models import SocialPost
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
    # Fetch all social posts from the database
    posts = SocialPost.objects.all()
    return render(request, "social_post_list.html", {"posts": posts})