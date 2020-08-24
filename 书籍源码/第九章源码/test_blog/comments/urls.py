from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path(r'comment/post/<int:blog_pk>/', views.blog_comment, name='blog_comment'),
]
