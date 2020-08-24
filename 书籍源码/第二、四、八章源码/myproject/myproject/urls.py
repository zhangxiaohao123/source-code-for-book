"""myproject URL Configuration

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
from  myapp  import views
#from test_views import views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('test/', views.test),
    path('myapp/',include('myapp.urls')),
    path('template_test/', views.template_test),
    path('test_filter/', views.test_filter,name='test_filter'),
    path('test_for/',views.test_for),
    path('test_tag/',  views.test_tag),
    path('test_inclusion_tag/', views.test_inclusion_tag),
    path('test_basehtml/', views.test_basehtml),
    path('test_inhert/',views.test_inhert),
    path('hello/',views.hello),
    path('ny/<int:year>/<int:month>/',views.ny,name='ny'),
    path('name/<str:username>/',views.name,name='name'),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
