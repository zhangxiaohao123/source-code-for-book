from django.urls import path,include
from employee.views import  * #导入视图中的函数，*代表所有

urlpatterns = [
    path('test_foreign/', test_foreign),
    path('index/',index),
    #-------------旧版URL配置项---------------
    path('list_employee_old/',list_employee_old),
    path('add_employee_old/',add_employee_old),
    path('edit_employee_old/<int:emp_id>/',edit_employee_old),
    path('del_employee_old/<int:emp_id>/',delete_employee_old),
    path('add_dep_old/',add_dep_old),
    path('list_dep_old/',list_dep_old),
    path('del_dep_old/<int:dep_id>/',del_dep_old),
    path('edit_dep_old/<int:dep_id>/',edit_dep_old),
    path('add_group_old/',add_group_old),
    path('list_group_old/',list_group_old),
    path('del_group_old/<int:group_id>/',del_group_old),
    path('edit_group_old/<int:group_id>/',edit_group_old),
    path('add_employeeinfo_old/', add_employeeinfo_old),#增加一条用户补充信息（employeeinfo表）
    path('list_employeeinfo_old/', list_employeeinfo_old),#用户补充信息列表（employeeinfo表）
    path('del_employeeinfo_old/<int:info_id>/', del_employeeinfo_old),#删除一条用户补充信息（employeeinfo表）
    path('edit_employeeinfo_old/<int:info_id>/', edit_employeeinfo_old),#修改一条用户补充信息（employeeinfo表）
    # -------------以上旧版URL配置项---------------
    path('list_employee/',list_employee),
    path('add_employee/',add_employee),
    path('edit_employee/<int:emp_id>/',edit_employee),
    path('del_employee/<int:emp_id>/',delete_employee),
    path('add_dep/',add_dep),
    path('list_dep/',list_dep),
    path('del_dep/<int:dep_id>/',del_dep),
    path('edit_dep/<int:dep_id>/',edit_dep),
    path('add_group/',add_group),
    path('list_group/',list_group),
    path('del_group/<int:group_id>/',del_group),
    path('edit_group/<int:group_id>/',edit_group),
    path('add_employeeinfo/', add_employeeinfo),#增加一条用户补充信息（employeeinfo表）
    path('list_employeeinfo/', list_employeeinfo),#用户补充信息列表（employeeinfo表）
    path('del_employeeinfo/<int:info_id>/', del_employeeinfo),#删除一条用户补充信息（employeeinfo表）
    path('edit_employeeinfo/<int:info_id>/', edit_employeeinfo),#修改一条用户补充信息（employeeinfo表）
    ]
