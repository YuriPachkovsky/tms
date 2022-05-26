from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect
from .models import TextPost
from .forms import PostForm

def main(request):
    posts = TextPost.objects.all()
    return render(request, 'base.html', {'posts': posts})


def posts(request):
    posts = TextPost.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def add_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/demo/posts')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'add_posts.html', {'form': form})

def delete_post(request, id):
    post = TextPost.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/demo/posts')