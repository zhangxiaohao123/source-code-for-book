"""test_orm URL Configuration

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
from django.urls import path,include

from test_form import views
from django.conf.urls.static import static
from . import settings
import test_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_orm/',include('employee.urls')),
    path('test_orm_old/',include('employee.urls')),
    path('test_page/',include('test_page.urls')),
    path('test_ajax/',include('test_ajax.urls')),
    path('test_middleware/',include('test_middleware.urls')),
    path('test_auth/',include('test_auth.urls')),
    # -----------form--------------
    path('test_form/', views.testform),
    #--------------Form----------
    path('login/',views.login),
    path('test_widget/',views.test_widget),
    path('add_loguser/',views.add_loguser),
    path('list_loguser/',views.list_loguser),
    path('edit_loguser/<int:loguser_id>/',views.edit_loguser),
    path('del_loguser/<int:loguser_id>/', views.del_loguser),
    #---------------ModelForm-------
    path('add_loguserm/',views.add_loguserm),
    path('list_loguserm/',views.list_loguserm),
    path('edit_loguserm/<int:loguser_id>/',views.edit_loguserm),
    path('del_loguserm/<int:loguser_id>/', views.del_loguserm),
    #---------------test_view----------
    path('test_view/',include('test_view.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
