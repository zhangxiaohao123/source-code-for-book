"""rbac_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from test_rbac import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('logout/', views.logout),
    path('index/', views.index),
    path('userinfo/', views.userinfo),
    path('userinfo/add/', views.userinfo_add),
    path('userinfo/del/(\d+)/', views.userinfo_del),
    path('userinfo/edit/(\d+)/', views.userinfo_edit),
    path('order/', views.order),
    path('order/add/', views.order_add),
    path('order/del/(\d+)/', views.order_del),
    path('order/edit/(\d+)/', views.order_edit),
    path('department/', views.department),
    path('department/add/', views.department_add),
    path('department/del/(\d+)/', views.department_del),
    path('department/edit/(\d+)/', views.department_edit),
]
