from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from .models import BlogPost


# Create your views here.

class BlogPostListView(ListView):
    queryset = BlogPost.objects.filter(status_of_post='published')
    context_object_name = "posts"
    paginate_by = 5
    template_name = 'blog/blogpost/list.html'


def blogpost_detail(request, id):
    try:
        post = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        raise Http404("No Post found.")
    return render(request,
                  'blog/blogpost/detail.html',
                  {'post': post})
