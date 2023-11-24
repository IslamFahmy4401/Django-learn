from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from . models import Post

# Create your views here.


def home(request):

    return render(request, 'home.html')


def about(request):

    return render(request, 'about.html')


def post_list(request):

    posts = Post.objects.all()

    return render(request, 'post_list.html', {'posts': posts})


def post_details(request, year, month, day, post):
    # Method 1

    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404('No Post Found')

    # return render(request, 'post_details.html', {'post', post})

    # Method 2

    post = get_object_or_404(Post,  status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'post_details.html', {'post': post})
