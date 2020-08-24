from django.shortcuts import render,redirect,HttpResponse
from . import forms
from . import models

def testform(request):
    if request.method=="POST":
        test_form=forms.test_form(request.POST)
        if test_form.is_valid():
            account=test_form.cleaned_data.get("account")
            pw=test_form.cleaned_data.get("password")
            if (account=='test' and pw=='123'):
                return HttpResponse("登录成功")
            else:
                return HttpResponse("用户名或密码错误")
        else:
            return HttpResponse("数据录入不合法")
    test_form=forms.test_form()
    return render(request,'test_form.html',{'testform':test_form})


def login(request):
    if request.method == 'POST':
       form_obj=forms.login_form(request.POST)
       if form_obj.is_valid():
           account=form_obj.cleaned_data['account']
           pwd=form_obj.cleaned_data['pwd']
           user_obj=models.loguser.objects.filter(account=account,password=pwd).first()
           if user_obj:
               return redirect('/list_loguser/')
           else:
               error='用户不存在或密码错误！'
               return render(request,'login.html', {'form_obj': form_obj,'errmsg':error})
       else:
           return render(request, 'login.html', {'form_obj': form_obj})
    form_obj=forms.login_form()
    return render(request,'login.html',{'form_obj':form_obj})

def test_widget(request):
    if request.method == 'POST':
       form_obj=forms.test_widget(request.POST)
       print('yydd')
       if form_obj.is_valid():
           return HttpResponse('ok')
       else:
           return render(request, 'test_widget.html', {'form_obj': form_obj})
    form_obj=forms.test_widget()
    return render(request,'test_widget.html',{'form_obj':form_obj})

def add_loguser(request):
    if request.method=='POST':
        form_obj=forms.loguser_form(request.POST or None,request.FILES or None) #由于有上传图象文件，所以参数中增加request.FILES
        #print(form_obj)
        if form_obj.is_valid(): #表单数据校验
            loguser_obj=models.loguser.objects.create(
                account=form_obj.cleaned_data['account'],
                password = form_obj.cleaned_data['password'],
                email=form_obj.cleaned_data['email'],
                gander=form_obj.cleaned_data['gander'],
                hobby=form_obj.cleaned_data['hobby'],
                hair=form_obj.cleaned_data['hair'],
                img=form_obj.cleaned_data['img']
            ) #在数据库表中新增一条记录
            return redirect('/list_loguser/') #增加记录后生定向到列表页面
        else:
            return render(request, 'add_loguser.html', {'formobj': form_obj}) #数据未通过校验，重新加到增加页面
    form_obj=forms.loguser_form() #第一次打开页面，初始化一个表单对象
    return render(request,'add_loguser.html',{'formobj':form_obj}) #定向到增加页面，并传递参数

def list_loguser(request):
    users=models.loguser.objects.all()
    return render(request, 'list_loguser.html', {'usr_list':users})

def edit_loguser(request,loguser_id):
    if request.method=='POST':
        form_obj = forms.loguser_form(request.POST or None, request.FILES or None)
        if form_obj.is_valid():
            id=form_obj.cleaned_data['id']
            loguser_obj=models.loguser.objects.get(id=id)
            loguser_obj.account=form_obj.cleaned_data['account']
            loguser_obj.password=form_obj.cleaned_data['password']
            loguser_obj.email=form_obj.cleaned_data['email']
            loguser_obj.gander=form_obj.cleaned_data['gander']
            loguser_obj.hobby=form_obj.cleaned_data['hobby']
            loguser_obj.hair=form_obj.cleaned_data['hair']
            loguser_obj.img = form_obj.cleaned_data['img']
            if not loguser_obj.img:
                loguser_obj.img=request.POST.get('img1')
            loguser_obj.save()
            imgname=loguser_obj.img
            # if not imgname:
            #     imgname=request.POST.get('img1')
            # print(imgname)
            return render(request, 'edit_loguser.html', {'formobj': form_obj, 'img': imgname})
        else:
            return render(request, 'add_loguser.html', {'formobj': form_obj})
    obj_list=models.loguser.objects.filter(id=loguser_id).values('id','account','password','email','gander','hobby','hair','img')
    dic=obj_list[0]
    #print(dic)
    imgname=dic['img']
    form_obj=forms.loguser_form(initial=dic)
    return render(request, 'edit_loguser.html', {'formobj': form_obj,'img': imgname})

def del_loguser(request,loguser_id):
    obj=models.loguser.objects.get(id=loguser_id)
    obj.delete()
    return redirect('/list_loguser/')

#-----------------------ModelForm--------

def list_loguserm(request):
    users=models.loguser.objects.all()
    return render(request, 'list_loguser1.html', {'usr_list':users})

def add_loguserm(request):
    if request.method=='POST':
        form_obj=forms.loguser_modelform(request.POST or None,request.FILES or None) #由于有上传图象文件，所以参数中增加request.FILES
        #print(form_obj)
        if form_obj.is_valid(): #表单数据校验
            form_obj.save() #在数据库表中新增一条记录
            return redirect('/list_loguserm/') #增加记录后生定向到列表页面
        else:
            return render(request, 'add_loguser1.html', {'formobj': form_obj}) #数据未通过校验，重新加到增加页面
    form_obj=forms.loguser_modelform() #第一次打开页面，初始化一个表单对象
    return render(request,'add_loguser1.html',{'formobj':form_obj}) #定向到增加页面，并传递参数


def edit_loguserm(request,loguser_id):
    loguser_obj = models.loguser.objects.get(id=loguser_id)#取出符合条件的记录
    if request.method=='POST':
        form_obj = forms.loguser_modelform(request.POST or None, request.FILES or None,instance=loguser_obj)
        if form_obj.is_valid():
            loguser=form_obj.save()
            imgname=loguser.img
            return render(request, 'edit_loguser1.html', {'formobj': form_obj, 'img': imgname})
        else:
            return render(request, 'add_loguser1.html', {'formobj': form_obj})
    imgname=loguser_obj.img #取记录中的图像文件的地址
    form_obj=forms.loguser_modelform(instance=loguser_obj)#用数据记录数据初始化一个表单对象
    return render(request, 'edit_loguser1.html', {'formobj': form_obj,'img': imgname})

def del_loguserm(request,loguser_id):
    obj=models.loguser.objects.get(id=loguser_id)
    obj.delete()
    return redirect('/list_loguser/')
