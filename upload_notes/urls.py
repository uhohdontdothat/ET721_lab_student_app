from django.urls import path
from .views import HomePageView, CreatePostView

urlpatterns = [
    path('', HomePageView.as_view(), name='image_list'),
    path('post',CreatePostView.as_view(),name='add_post'),
]