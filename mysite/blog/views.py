from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from . models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

# Create your views here.


def home(request):

    return render(request, 'home.html')


def about(request):

    return render(request, 'about.html')


def post_list(request):

    post_list = Post.objects.all()
    paginator = Paginator(post_list, 1)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render(request, 'post_list.html', {'posts': posts})

# class PostListView(ListView): # Building Class Based Views
#     model = Post
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = "post_list.html"


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


def post_share(request, post_id):

    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    sent = False

    if request.method == 'POST':

        form = EmailPostForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url} \n {cd['name']} \'s comments: {cd['comments']}"
            send_mail(subject, message, 'islam4401@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'share.html', {'post': post, 'form': form, 'sent': sent})
