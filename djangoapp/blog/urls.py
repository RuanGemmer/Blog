from django.urls import path
from blog.views import index, page, post


app_name = 'blog'

urlpatterns = [
    path('post/<slug:slug>', post, name='post'),
    path('page/', page, name='page'),
    path('', index, name='index'),
]
