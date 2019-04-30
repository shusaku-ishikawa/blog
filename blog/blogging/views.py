from django.shortcuts import render
from django.views import generic
from .models import *


class PostList(generic.ListView):
    model = Post
    template_name = 'blogging/post_list.html'

    def get_queryset(self):
        published_posts = Post.objects.filter(published_at__isnull = False)
        
        return published_posts

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogging/post_detail.html'
