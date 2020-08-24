from django.shortcuts import render,HttpResponse
from . import models
from . import forms
import json

# Create your views here.
def tangshi(request):
    ts1= request.GET.get('ts1')
    ts2 = request.GET.get('ts2')
    return render(request,'test_ajax/tangshi.html')
def tangshi_ret(request):
    ts1 = request.GET.get('ts1')
    ts2 = request.GET.get('ts2')
    if ts1=='床前明月光':
        ts3='举头望明月'
        ts4='低头思故乡'
        dic={'ts3':ts3,'ts4':ts4}
        data_ret=json.dumps(dic)
    return HttpResponse(data_ret)
def tangshi_img(request):
    src = "/media/month.jpg"
    return HttpResponse(src)

def list_person(request):
    per_list=models.person.objects.all()

    return render(request,'test_ajax/list_person.html',{'person_list':per_list})
def del_row(request):
        id = request.GET.get("id")
        print(id)
        models.person.objects.filter(id=id).delete()
        return HttpResponse("操作成功！")
from django.http import JsonResponse
def add_person(request):
    if request.method=='POST':
        ret = {"status": 0, "url_or_msg": ""}
        form_obj=forms.person_form(request.POST)
        print(form_obj)
        if form_obj.is_valid(): #表单数据校验
            person_obj=models.person.objects.create(
                name=form_obj.cleaned_data['name'],
                email=form_obj.cleaned_data['email'],
                salary=form_obj.cleaned_data['salary']
            ) #在数据库表中新增一条记录
            ret["url_or_msg"] = "/test_ajax/list_person/"
            return JsonResponse(ret)
        else:
            ret["status"] = 1
            ret["url_or_msg"] = form_obj.errors
            print(ret)
            return JsonResponse(ret)

    form_obj=forms.person_form() #第一次打开页面，初始化一个表单对象
    return render(request,'test_ajax/add_person.html',{'formobj':form_obj}) #定向到增加页面，并传递参数

# 校验用户名是否已被注册
def test_name(request):
    ret = {"status": 0, "message": ""}
    name = request.GET.get("name")
    per_obj = models.person.objects.filter(name=name)
    if per_obj:
        ret["status"] = 1
        ret["message"] = "用户名已存在，请重新录入！"
    return JsonResponse(ret)
