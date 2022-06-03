from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect
from .models import TextPost
from .forms import PostForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView


class PostListView(ListView):
    model = TextPost
    template_name = 'posts.html'
    context_object_name = 'posts'

class PostEditView(UpdateView):
    model = TextPost
    template_name = 'edit_post.html'
    form_class = PostForm
    success_url = '/demo/posts'

class PostCreateView(CreateView):
    model = TextPost
    template_name = 'add_post.html'
    form_class = PostForm
    success_url = '/demo/posts'

class PostDeleteView(DeleteView):
    model = TextPost
    template_name = 'delete_post.html'
    success_url = '/demo/posts'

def delete_post(request, id):
    post = TextPost.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/demo/posts')