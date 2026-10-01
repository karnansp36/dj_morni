from django.urls import path
from . import views
urlpatterns = [
    path('social_post/', views.SocialPostView, name='social_post'),
    path('social_post_list/', views.SocialPostListView, name='social_post_list'),
    path('social_post/<int:post_id>/like/', views.ToggleSocialPostLikeView, name='social_post_like'),
    path('social_post/<int:post_id>/comment/', views.SocialPostCommentView, name='social_post_comment'),
]