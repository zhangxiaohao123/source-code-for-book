from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
# Create your views here.
from rbac import models
from rbac.service.init_permission import init_permission

class BasePermPage(object):
    def __init__(self, code_list):
        self.code_list = code_list

    def has_add(self):
        if "add" in self.code_list:
            return True

    def has_del(self):
        if "del" in self.code_list:
            return True

    def has_edit(self):
        if "edit" in self.code_list:
            return True


def login(request):
    if request.method == "GET":
        return render(request, "test_rbac/login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = models.UserInfo.objects.filter(username=username, password=password).first()
        if user:
            init_permission(request,user)
            return redirect("/index/")
        else:
            return render(request, "test_rbac/login.html")


def index(request):
    return render(request, "test_rbac/index.html")


def userinfo(request):


    pagpermission =BasePermPage(request.session.get('permission_codes'))  # 实例化
    # print("code......", request.permission_code_url)
    data_list = [
        {"id": 1, "name": "张三","work":"律师"},
        {"id": 2, "name": "李四","work":"教师"},
        {"id": 3, "name": "王五","work":"程序员"},
        {"id": 4, "name": "赵六","work":"医生"},
        {"id": 5, "name": "田七","work":"小护士"},
    ]
    #print("data_list",data_list)
    #print("pagpermission",pagpermission)
    return render(request, "test_rbac/userinfo.html", {"data_list": data_list, "pagpermission": pagpermission})


def userinfo_add(request):
    if request.method == "GET":
        return render(request,"test_rbac/useradd.html")
    else:
        return redirect("/userinfo/")#redirect中的/urserinfo/对应的是网址，前有/是绝对地址，前无/相对地址


def userinfo_del(request, nid):
    return HttpResponse("删除用户")


def userinfo_edit(request, nid):
    return HttpResponse("编辑用户")


def department(request):
    pagpermission = BasePermPage(request.session.get('permission_codes'))  # 实例化
    #print('aaaaaaaaaaaadddddddddddddd',request.session.get('permission_codes'))

    return render(request,"test_rbac/department.html",{"pagpermission":pagpermission})


def department_add(request):
    return HttpResponse("添加部门")


def department_del(request, nid):
    return HttpResponse("删除部门")


def department_edit(request, nid):
    return HttpResponse("编辑部门")



def order(request):
    pagpermission = BasePermPage(request.session.get('permission_codes'))  # 实例化

    return render(request,"test_rbac/order.html",{"pagpermission":pagpermission}) # render中对应的settins.py中的TEMPLATES中的DIRS设置，test_rbac/order.html前面不能加/


def order_add(request):
    return HttpResponse("添加订单")


def order_del(request, nid):
    return HttpResponse("删除订单")


def order_edit(request, nid):
    return HttpResponse("编辑订单")

def logout(request):
    request.session.clear()
    return redirect('/login/')
