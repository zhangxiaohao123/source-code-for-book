import os

if __name__ == '__main__':
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BMS.settings")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_orm.settings')
    import django
    django.setup()

    from employee import models

    # #objects = models.employee.objects.all()
    # object1 = models.employee.objects.get(id=8)
    # object2 = models.employee.objects.first()
    # object3 = models.employee.objects.last()
    # object4= models.employee.objects.count()
    #models.employee.objects.first().group.create(group_name='博击',group_script='博击也是健身的项目')
    #models.group.objects.first().employee_set.create(name='吴用2',email='wy2@163.com',dep_id='11')
    #models.group.objects.get(id=4).employee_set.create(name='李明',email='lm2@163.com',dep_id='11')

    # group_list=models.group.objects.filter(id__lt=6)
    # models.employee.objects.first().group.add(*group_list)
    # obj_list=models.employee.objects.filter(id__lt=11).first()
    # obj_list.group.set([1,2,3])
    #print(models.employee.objects.all().count())
    # obj_list = models.employee.objects.all().first()
    # obj_list.group.remove(1)
    #models.employee.objects.last().group.clear()
    # emp_info = models.employeeinfo.objects.get(id=2)
    # emp_name = emp_info.employee.name  # 反操作不用employee _set,直接用employee
    # print(emp_name)
    # emp=models.employee.objects.get(id=1)
    # dep=emp.info.phone
    from django.db.models import Sum,Avg,Max,Min,Count
    # salary_data=models.employee.objects.filter(id__lt=18).aggregate(count=Count("id"),salary_hj=Sum("salary"),salary_pj= Avg("salary"),salary_zd=Max("salary"), alary_zx=Min("salary"))
    # print(salary_data)
    # dep_salary=models.employee.objects.values('dep').annotate(avg=Avg("salary")).values('dep__dep_name',"avg")
    # print(dep_salary)

    #查询字段（外键）
    # emp=models.employee.objects.values_list('name',"dep__dep_name","dep__dep_script")
    # print(emp)
    # emp2=models.employee.objects.values('name',"dep__dep_name","dep__dep_script")
    # print(emp2)
    # dep_emp=models.department.objects.values_list("dep_related__name","dep_related__email")
    # print(dep_emp)
    # 查询字段（多对多键）
    # emp_m2m=models.employee.objects.values_list("id","name","group__group_name")
    # print(emp_m2m)
    # emp_m2m=models.group.objects.values("group_name","employee__name","employee__email")
    # print(emp_m2m)
    # emp_one=models.employee.objects.values("id","name","info__phone","info__address")
    # print(emp_one)
    # emp_one = models.employeeinfo.objects.values("phone","address","employee__name","employee__email")
    # print(emp_one)
    # emp_list=models.employee.objects.annotate(groupnum=Count("group"))
    # for emp in emp_list:
    #     print(emp.name,'：参加',emp.groupnum,'个团体')
    # dep_list=models.department.objects.annotate(maxsalary=Max("employee__salary"))
    # for dep in dep_list:
    #     print(dep.dep_name,dep.maxsalary)
    # dep_list=models.department.objects.annotate(maxsalary=Max("employee__salary")).values_list("dep_name","maxsalary")
    # for dep in dep_list:
    #     print(dep)

    # dep_salary=models.employee.objects.values('dep').annotate(avg=Avg("salary")).values('dep__dep_name',"avg")
    # print(dep_salary)
    # from django.db.models import F
    # models.employee.objects.filter(id__lt=30).update(salary=F("salary")+600)
    #
    # emp=models.employee.filter()
    from django.db.models import Q

    obj=models.employee.objects.filter(Q(salary__gt=1000)& ~Q(name__startswith='李'))
    print(obj[0].salary)




