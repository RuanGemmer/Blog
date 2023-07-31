from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404


POST_PER_PAGE: int = 9


def index(request):
    posts = Post.objects.get_published()
    paginator = Paginator(posts, POST_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': 'Home - '
        }
    )


def post(request, slug):
    post_obj = Post.objects.get_published().filter(slug=slug).first()

    if post_obj is None:
        raise Http404()

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post_obj,
            'page_title': f'{post_obj.title} - Post - '
        }
    )


def page(request, slug):
    page_obj = Page.objects.get_published().filter(slug=slug).first()

    if page_obj is None:
        raise Http404()

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page_obj,
            'page_title': f'{page_obj.title} - Page - '
        }
    )


def created_by(request, pk):
    posts = Post.objects.get_published().filter(created_by__pk=pk)
    paginator = Paginator(posts, POST_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    user = User.objects.filter(pk=pk).first()

    if user is None:
        raise Http404()

    user_full_name = user.username

    if user.first_name:
        user_full_name = f'{user.first_name.capitalize()} \
            {user.last_name.capitalize()}'

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': f'{user_full_name} - Posts - '
        }
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(posts, POST_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': f'{page_obj[0].category.name} - Category - '
        }
    )


def tag(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)
    paginator = Paginator(posts, POST_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': f'{page_obj[0].tags.first().name} - Tag - '
        }
    )


def search(request):
    search_value = request.GET.get('search', '').strip()
    posts = Post.objects.get_published().filter(
        Q(title__icontains=search_value) |
        Q(summary__icontains=search_value) |
        Q(content__icontains=search_value)
    )[:POST_PER_PAGE]

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': posts,
            'search_value': search_value,
            'page_title': f'{search_value[:20]} - Search - '
        }
    )
