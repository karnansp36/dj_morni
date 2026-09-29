from django.urls import path
from . import views
urlpatterns = [
    path('social_post/', views.SocialPostView, name='social_post'),
    path('social_post_list/', views.SocialPostListView, name='social_post_list'),
]