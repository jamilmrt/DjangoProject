from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='postList'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='postDetail'),
    path('post/new/', PostCreateView.as_view(), name='postCreate'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='postUpdate'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='postDelete'),
]
