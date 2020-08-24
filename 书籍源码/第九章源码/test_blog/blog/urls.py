from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.indexview.as_view(),name='index'),
    path('myindex/<int:loguserid>/',views.myindex.as_view(),name='myindex'),
    path('authorindex/<int:id>/',views.authorindex.as_view(),name='authorindex'),
    re_path('blog/(?P<pk>[0-9]+)/',views.blogdetailview.as_view(),name='detail'),
    re_path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.archives, name='archives'),
    re_path('category/(?P<pk>[0-9]+)/', views.categoryview.as_view(), name='category'),
    re_path('tag/(?P<pk>[0-9]+)/', views.tagview.as_view(), name='tag'),
    #path('search/', views.search, name='search'),
    path('login/', views.login,name='login'),
    path('registe/', views.registe,name='registe'),
    path('logout/',views.logout,name='logout'),
    path('test_ckeditor_front/',views.test_ckeditor_front),
]
