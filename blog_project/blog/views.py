from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/postList.html'  # Corrected template path
    context_object_name = 'posts'  # Context variable to access posts in the template

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/postDetail.html'  # Corrected template path
    context_object_name = 'post'  # Context variable to access the post in the template
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  # Use the custom form for creating posts
    template_name = 'blog/postForm.html'  # Corrected template path
    success_url = reverse_lazy('postList')  # Redirect to post list after successful creation
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm  # Use the custom form for updating posts
    template_name = 'blog/postForm.html'  # Corrected template path
    success_url = reverse_lazy('postList')  # Redirect to post list after successful update
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to update the post
    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the author is set to the current user
        return super().form_valid(form)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/postConfirmDelete.html'  # Corrected template path
    success_url = reverse_lazy('postList')  # Redirect to post list after successful deletion
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to delete the post