from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def user_login(request):
    if request.method == "GET":
        return render(request, "test_auth/login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(username=username, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect("/test_auth/index/")
        else:
            return render(request, "test_auth/login.html")

def logout(request):
    request.session.clear()
    return redirect('/test_auth/user_login/')



def index(request):
    return render(request, "test_auth/index.html")


def userinfo(request):
    data_list = [
        {"id": 1, "name": "张三","work":"律师"},
        {"id": 2, "name": "李四","work":"教师"},
        {"id": 3, "name": "王五","work":"程序员"},
        {"id": 4, "name": "赵六","work":"医生"},
        {"id": 5, "name": "田七","work":"小护士"},
    ]

    return render(request, "test_auth/userinfo.html", {"data_list": data_list})


def userinfo_add(request):
    if request.method == "GET":
        return render(request,"test_auth/useradd.html")
    else:
        return redirect("/test_auth/userinfo/")#redirect中的/urserinfo/对应的是网址，前有/是绝对地址，前无/相对地址


def userinfo_del(request, nid):
    return HttpResponse("删除用户")


def userinfo_edit(request, nid):
    return HttpResponse("编辑用户")


def department(request):

    return render(request,"test_auth/department.html")


def department_add(request):
    return HttpResponse("添加部门")


def department_del(request, nid):
    return HttpResponse("删除部门")


def department_edit(request, nid):
    return HttpResponse("编辑部门")
