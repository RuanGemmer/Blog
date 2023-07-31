from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from blog.models import Post, Page
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404, HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView


POST_PER_PAGE: int = 9


class PostListView(ListView):
    model = Post
    template_name = 'blog/pages/index.html'
    context_object_name = 'posts'
    ordering = '-pk'
    paginate_by = POST_PER_PAGE
    queryset = Post.objects.get_published()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context.update({
            'page_title': 'Home - ',
        })

        return context


class CreatedByListView(PostListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._temp_context: dict[str, Any] = {}

    def get(self, request, *args, **kwargs):
        pk_ = self.kwargs.get('pk')
        user = User.objects.filter(pk=pk_).first()

        if user is None:
            raise Http404()

        self._temp_context.update({
            'author_pk': pk_,
            "user": user,
        })

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self._temp_context['user']

        user_full_name = user.username
        if user.first_name:
            user_full_name = f'{user.first_name.capitalize()} \
                {user.last_name.capitalize()}'

        context.update({
            'page_title': f'{user_full_name} - Posts - '
        })

        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()

        queryset = queryset.filter(
            created_by__pk=self._temp_context['user'].pk
        )
        return queryset


class CategoryListView(PostListView):
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(
            category__slug=self.kwargs.get("slug")
        )

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'page_title':
            f'{self.object_list[0].category.name}'  # type: ignore
            ' - Category - '
        })

        return ctx


class TagListView(PostListView):
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(
            tags__slug=self.kwargs.get("slug")
        )

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'page_title':
            f'{self.object_list[0].tags.first().name}'  # type: ignore
            ' - Tag - '
        })

        return ctx


class SearchListView(PostListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._search_value = ''

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self._search_value = request.GET.get('search', '').strip()
        return super().setup(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        search_value = self._search_value
        return super().get_queryset().filter(
            Q(title__icontains=search_value) |
            Q(summary__icontains=search_value) |
            Q(content__icontains=search_value)
        )[:POST_PER_PAGE]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        search_value = self._search_value
        ctx.update({
            'search_value': search_value,
            'page_title': f'{search_value[:20]} - Search - '
        })

        return ctx

    def get(self,
            request: HttpRequest,
            *args: Any,
            **kwargs: Any) -> HttpResponse:
        if self._search_value == '':
            return redirect('blog:index')

        return super().get(request, *args, **kwargs)


class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/pages/page.html'
    slug_field = 'slug'
    context_object_name = 'page'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'page_title': f'{self.get_object().title} - Page - '  # type:ignore
        })

        return ctx

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/pages/post.html'
    slug_field = 'slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'page_title': f'{self.get_object().title} - Post - '  # type:ignore
        })

        return ctx

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published=True)
