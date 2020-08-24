from django.shortcuts import render,redirect,HttpResponse
from .models import employee,department,group,employeeinfo
# Create your views here.

def index(request):
    return render(request,'test_orm/index.html')
def test_foreign(request):
    emp=employee.objects.get(id=16)
    dep_name=emp.dep.dep_name #通过外键值dep关键到department对象，然后取得该对象的dep_name字段。
    #反向操作
    dep_obj = department.objects.get(id=3)
    emp_list = dep_obj.employee_set.all()
    #emp_list=dep_obj.dep_related.all()
    emp_names=[ emp.name for emp in emp_list]
    return HttpResponse("1、正向查找：员工名称：{0},所在部门名称:{1} <br> 2、反向查找：部门名称:{2},部门员工:{3}".format(emp.name,dep_name,dep_obj.dep_name,emp_names))

#--------------旧版本的视图函数--------------------
def add_employee_old(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        dep=request.POST.get("dep")
        info = request.POST.get("info")
        salary = request.POST.get("salary")
        groups=request.POST.getlist("group")
        new_emp=employee.objects.create(name=name,email=email,salary=salary,dep_id=dep,info_id=info)
        new_emp.group.set(groups)
        return redirect('/test_orm_old/list_employee_old/')
    dep_list=department.objects.all()
    group_list=group.objects.all()
    info_list = employeeinfo.objects.all()

    return render(request,'test_orm_old/add_employee_old.html',{'dep_list':dep_list,'group_list':group_list,'info_list':info_list})


def list_employee_old(request):
    emp=employee.objects.all()
    return render(request,'test_orm_old/list_employee_old.html',{'emp_list':emp})
def edit_employee_old(request,emp_id):
    if request.method=="POST":
        id=request.POST.get('id')
        name=request.POST.get("name")
        email=request.POST.get("email")
        dep=request.POST.get("dep")
        info=request.POST.get("info")
        groups=request.POST.getlist("group")
        emp=employee.objects.get(id=id)
        emp.name=name
        emp.email=email
        emp.dep_id=dep
        emp.info_id=info
        emp.group.set(groups)
        emp.save()

        return redirect('/test_orm_old/list_employee_old/')
    emp=employee.objects.get(id=emp_id)
    dep_list = department.objects.all()
    group_list = group.objects.all()
    info_list = employeeinfo.objects.all()
    return render(request, 'test_orm_old/edit_employee_old.html',{'emp':emp,'dep_list':dep_list,'group_list':group_list,'info_list':info_list})

def delete_employee_old(request,emp_id):
    emp=employee.objects.get(id=emp_id)
    emp.delete()
    return redirect('/test_orm_old/list_employee_old')

def add_dep_old(request):
    if request.method=='POST':
        dep_name=request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        if dep_name.strip()=='':
            return render(request, 'test_orm_old/add_dep_old.html', {'error_info': '部门名称不能为空！'})
        try:
            p=department.objects.create(dep_name=dep_name,dep_script=dep_script)
            return redirect('/test_orm_old/list_dep_old/')
        except Exception as e:
            return render(request, 'test_orm_old/add_dep_old.html',{'error_info':'录入部门名称重复或信息有错误！'})
        finally:
            pass
    return render(request,'test_orm_old/add_dep_old.html')
def list_dep_old(request):
    dep_list=department.objects.all()
    return render(request,'test_orm_old/list_dep_old.html',{'dep_list':dep_list})

def del_dep_old(request,dep_id):
    dep_object=department.objects.get(id=dep_id)
    dep_object.delete()
    return redirect('/test_orm_old/list_dep_old/')

def edit_dep_old(request,dep_id):
    if request.method=='POST':
        id=request.POST.get('id')
        dep_name=request.POST.get('dep_name')
        dep_script=request.POST.get('dep_script')
        dep_object=department.objects.get(id=id)
        dep_object.dep_name=dep_name
        dep_object.dep_script=dep_script
        dep_object.save()
        return redirect('/test_orm_old/list_dep_old/')
    else:
        dep_object=department.objects.get(id=dep_id)
        return render(request,'test_orm_old/edit_dep_old.html',{'department':dep_object})


#团队增删改查
def list_group_old(request):
    group_list=group.objects.all()
    return render(request,'test_orm_old/list_group_old.html',{'group_list':group_list})

def add_group_old(request):
    if request.method=='POST':
        group_name=request.POST.get('group_name')
        group_script = request.POST.get('group_script')
        if group_name.strip()=='':
            return render(request, 'test_orm_old/add_group.html', {'error_info': '团队名称不能为空！'})
        try:
            group.objects.create(group_name=group_name,group_script=group_script)
            return redirect('/test_orm_old/list_group_old/')
        except Exception as e:
            return render(request, 'test_orm_old/add_group_old.html',{'error_info':'录入团队名称重复或信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm_old/add_group_old.html')

def del_group_old(request,group_id):
    group_object=group.objects.get(id=group_id)
    group_object.delete()
    return redirect('/test_orm_old/list_group_old/')

def edit_group_old(request,group_id):
    if request.method=='POST':
        id=request.POST.get('id')
        group_name=request.POST.get('group_name')
        group_script=request.POST.get('group_script')
        group_object=group.objects.get(id=id)
        group_object.group_name=group_name
        group_object.group_script=group_script
        group_object.save()
        return redirect('/test_orm_old/list_group_old/')
    else:
        group_object=group.objects.get(id=group_id)
        return render(request,'test_orm_old/edit_group_old.html',{'group':group_object})



#employeeinf增删改查
def list_employeeinfo_old(request):#员工补充信息列表
    info_list=employeeinfo.objects.all()
    return render(request,'test_orm_old/list_employeeinfo_old.html',{'info_list':info_list})
def add_employeeinfo_old(request):#增加一条员工补充信息记录
    if request.method=='POST':
        phone=request.POST.get('phone')
        address = request.POST.get('address')
        if phone.strip()=='':
            return render(request, 'test_orm_old/add_employeeinfo_old.html', {'error_info': '电话不能为空！'})
        try:
            employeeinfo.objects.create(phone=phone,address=address)
            return redirect('/test_orm_old/list_employeeinfo_old/')
        except Exception as e:
            return render(request, 'test_orm_old/add_employeeinfo_old.html',{'error_info':'信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm_old/add_employeeinfo_old.html')

def del_employeeinfo_old(request,info_id):#删除一条员工补充信息记录
    info_object=employeeinfo.objects.get(id=info_id)
    info_object.delete()
    return redirect('/test_orm_old/list_employeeinfo_old/')

def edit_employeeinfo_old(request,info_id):#修改一条员工补充信息记录
    if request.method=='POST':
        id=request.POST.get('id')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        info_object=employeeinfo.objects.get(id=id)
        info_object.phone=phone
        info_object.address=address
        info_object.save()
        return redirect('/test_orm_old/list_employeeinfo_old/')
    else:
        info_object=employeeinfo.objects.get(id=info_id)
        return render(request,'test_orm_old/edit_employeeinfo_old.html',{'info':info_object})
#--------------以上旧版本的视图函数--------------------
def add_employee(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        dep=request.POST.get("dep")
        info = request.POST.get("info")
        salary = request.POST.get("salary")
        groups=request.POST.getlist("group")
        new_emp=employee.objects.create(name=name,email=email,salary=salary,dep_id=dep,info_id=info)
        new_emp.group.set(groups)
        return redirect('/test_orm/list_employee/')
    dep_list=department.objects.all()
    group_list=group.objects.all()
    info_list = employeeinfo.objects.all()

    return render(request,'test_orm/add_employee.html',{'dep_list':dep_list,'group_list':group_list,'info_list':info_list})


def list_employee(request):
    emp=employee.objects.all()
    return render(request,'test_orm/list_employee.html',{'emp_list':emp})
def edit_employee(request,emp_id):
    if request.method=="POST":
        id=request.POST.get('id')
        name=request.POST.get("name")
        email=request.POST.get("email")
        dep=request.POST.get("dep")
        info=request.POST.get("info")
        groups=request.POST.getlist("group")
        emp=employee.objects.get(id=id)
        emp.name=name
        emp.email=email
        emp.dep_id=dep
        emp.info_id=info
        emp.group.set(groups)
        emp.save()

        return redirect('/test_orm/list_employee/')
    emp=employee.objects.get(id=emp_id)
    dep_list = department.objects.all()
    group_list = group.objects.all()
    info_list = employeeinfo.objects.all()
    return render(request, 'test_orm/edit_employee.html',{'emp':emp,'dep_list':dep_list,'group_list':group_list,'info_list':info_list})

def delete_employee(request,emp_id):
    emp=employee.objects.get(id=emp_id)
    emp.delete()
    return redirect('/test_orm/list_employee')

def add_dep(request):
    if request.method=='POST':
        dep_name=request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        if dep_name.strip()=='':
            return render(request, 'test_orm/add_dep.html', {'error_info': '部门名称不能为空！'})
        try:
            p=department.objects.create(dep_name=dep_name,dep_script=dep_script)
            return redirect('/test_orm/list_dep/')
        except Exception as e:
            return render(request, 'test_orm/add_dep.html',{'error_info':'录入部门名称重复或信息有错误！'})
        finally:
            pass
    return render(request,'test_orm/add_dep.html')
def list_dep(request):
    dep_list=department.objects.all()
    return render(request,'test_orm/list_dep.html',{'dep_list':dep_list})

def del_dep(request,dep_id):
    dep_object=department.objects.get(id=dep_id)
    dep_object.delete()
    return redirect('/test_orm/list_dep/')

def edit_dep(request,dep_id):
    if request.method=='POST':
        id=request.POST.get('id')
        dep_name=request.POST.get('dep_name')
        dep_script=request.POST.get('dep_script')
        dep_object=department.objects.get(id=id)
        dep_object.dep_name=dep_name
        dep_object.dep_script=dep_script
        dep_object.save()
        return redirect('/test_orm/list_dep/')
    else:
        dep_object=department.objects.get(id=dep_id)
        return render(request,'test_orm/edit_dep.html',{'department':dep_object})


#团队增删改查
def list_group(request):
    group_list=group.objects.all()
    return render(request,'test_orm/list_group.html',{'group_list':group_list})

def add_group(request):
    if request.method=='POST':
        group_name=request.POST.get('group_name')
        group_script = request.POST.get('group_script')
        if group_name.strip()=='':
            return render(request, 'test_orm/add_group.html', {'error_info': '团队名称不能为空！'})
        try:
            group.objects.create(group_name=group_name,group_script=group_script)
            return redirect('/test_orm/list_group/')
        except Exception as e:
            return render(request, 'test_orm/add_group.html',{'error_info':'录入团队名称重复或信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm/add_group.html')

def del_group(request,group_id):
    group_object=group.objects.get(id=group_id)
    group_object.delete()
    return redirect('/test_orm/list_group/')

def edit_group(request,group_id):
    if request.method=='POST':
        id=request.POST.get('id')
        group_name=request.POST.get('group_name')
        group_script=request.POST.get('group_script')
        group_object=group.objects.get(id=id)
        group_object.group_name=group_name
        group_object.group_script=group_script
        group_object.save()
        return redirect('/test_orm/list_group/')
    else:
        group_object=group.objects.get(id=group_id)
        return render(request,'test_orm/edit_group.html',{'group':group_object})



#employeeinf增删改查
def list_employeeinfo(request):#员工补充信息列表
    info_list=employeeinfo.objects.all()
    return render(request,'test_orm/list_employeeinfo.html',{'info_list':info_list})
def add_employeeinfo(request):#增加一条员工补充信息记录
    if request.method=='POST':
        phone=request.POST.get('phone')
        address = request.POST.get('address')
        if phone.strip()=='':
            return render(request, 'test_orm/add_employeeinfo.html', {'error_info': '电话不能为空！'})
        try:
            employeeinfo.objects.create(phone=phone,address=address)
            return redirect('/test_orm/list_employeeinfo/')
        except Exception as e:
            return render(request, 'test_orm/add_employeeinfo.html',{'error_info':'信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm/add_employeeinfo.html')

def del_employeeinfo(request,info_id):#删除一条员工补充信息记录
    info_object=employeeinfo.objects.get(id=info_id)
    info_object.delete()
    return redirect('/test_orm/list_employeeinfo/')

def edit_employeeinfo(request,info_id):#修改一条员工补充信息记录
    if request.method=='POST':
        id=request.POST.get('id')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        info_object=employeeinfo.objects.get(id=id)
        info_object.phone=phone
        info_object.address=address
        info_object.save()
        return redirect('/test_orm/list_employeeinfo/')
    else:
        info_object=employeeinfo.objects.get(id=info_id)
        return render(request,'test_orm/edit_employeeinfo.html',{'info':info_object})


#------------------------------------------
