from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index),
    #车辆信息
    path('carlist/',views.carlist),
    path('caradd/',views.caradd),
    path('caredit/<int:id>/',views.caredit),
    path('cardel/<int:id>/',views.cardel),
    #部门信息
    path('deplist/',views.deplist),
    path('depadd/',views.depadd),
    path('depedit/<int:id>/',views.depedit),
    path('depdel/<int:id>/',views.depdel),
    path('userlist/',views.userlist),
    path('useredit/<int:userid>/',views.useredit),
    #每日车费上报
    path('farelist/',views.farelist),
    path('fareadd/',views.fareadd),
    path('fareedit/<int:fareid>/',views.fareedit),
    path('faredel/<int:fareid>/',views.faredel),
    #车费审批
    path('farecheck/',views.farecheck),

    path('fareapprove/<str:ids>/', views.fare_approve),
    path('farecheck2/', views.farecheck2),

    path('approvecancel/<str:ids>/', views.approve_cancel),
    path('annotate/',views.annotate_fare)
]
