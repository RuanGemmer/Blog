from django.urls import path
from blog.views import PostListView, CreatedByListView, page, \
    post, CategoryListView, TagListView, SearchListView


app_name = 'blog'

urlpatterns = [
    path('post/<slug:slug>/', post, name='post'),
    path('page/<slug:slug>/', page, name='page'),
    path('created_by/<int:pk>/',
         CreatedByListView.as_view(), name='created_by'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('tag/<slug:slug>/', TagListView.as_view(), name='tag'),
    path('search/', SearchListView.as_view(), name='search'),
    path('', PostListView.as_view(), name='index'),
]
