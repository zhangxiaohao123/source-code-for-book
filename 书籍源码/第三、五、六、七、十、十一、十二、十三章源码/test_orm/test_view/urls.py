from django.urls import path
from . import views

urlpatterns = [
    path('hello_view/', views.hello_view),
    path('dep/<int:dep_id>/',views.depdetail,name='depdetail'),
    path('test_redirect/',views.test_redirect),
    path('test_redirectv/', views.test_redirectv),
    path('test_templateview/',views.test_templateview.as_view()),
    path('test_listview/',views.test_listview.as_view()),
    path('listviewdemo/',views.listviewdemo.as_view()),
    path('test_detailview/<int:personid>/',views.test_detailview.as_view()),
    path('detailviewdemo/<int:personid>/',views.detailviewdemo.as_view()),
    path('login/', views.login), #登录
    path('index/',views.index), #主页，人员列表
    path('add_person/',views.add_person), #增加人员
    path('del_person/<int:personid>/',views.del_person), #删除人员
    path('edit_person/<int:personid>/',views.edit_person), #修改人员
    ]
