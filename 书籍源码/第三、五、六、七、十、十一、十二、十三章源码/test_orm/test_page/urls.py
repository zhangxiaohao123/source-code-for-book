from django.urls import path,include
from . import views


urlpatterns = [
    path('person_page/',views.person_page),
    path('person_pagenew/',views.person_pagenew)
    ]
