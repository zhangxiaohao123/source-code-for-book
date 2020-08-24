from django.urls import  path
from . import views

urlpatterns = [
    path('tangshi/', views.tangshi),
    path('tangshi_ret/',views.tangshi_ret),
    path('tangshi_img/',views.tangshi_img),
    path('list_person/',views.list_person),
    path('del_row/',views.del_row),
    path('add_person/',views.add_person),
    path('test_name/',views.test_name),


    ]
