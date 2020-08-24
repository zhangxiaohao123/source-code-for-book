from django.urls import path
from . import  views
urlpatterns = [
    path('test/',views.test),
    path('test2/',views.test2),
]
