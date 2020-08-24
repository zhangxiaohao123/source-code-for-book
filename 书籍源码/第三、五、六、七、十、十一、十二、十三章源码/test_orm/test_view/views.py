from django.shortcuts import render,HttpResponse,redirect
from . import models
import datetime

# Create your views here.
def hello_view(request):
    vnow=datetime.datetime.now().date()
    rep="<div align='center'><h1>你好，欢迎你浏览本页面</h1><hr>当前日期是：%s</div>"%vnow
    return HttpResponse(rep)
    # response = HttpResponse()
    # response.write("<p>这是一行.</p>")
    # response.write("<p>这是另一行.</p>")
    # return response
    # response = HttpResponse()
    # lines=["<p>这是一行.</p>","<p>这是第二行.</p>"]
    # response.writelines(lines)
    #reponse.flush()
    # return response

def depdetail(request,dep_id):
    obj=models.department.objects.get(id=dep_id)
    return HttpResponse('部门：'+obj.dep_name+',备注：'+obj.dep_script)

def test_redirect(request):
    obj=models.department.objects.get(id=1)
    return redirect(obj)

def test_redirectv(request):
    #return redirect('depdetail',dep_id=2)
    #return redirect('http://127.0.0.1:8000/dep/2/')
    return redirect('http://www.baidu.com/')
#-----------------------通用视图测试-----------------
from django.views.generic import TemplateView,ListView,DetailView
class test_templateview(TemplateView):
    template_name = 'test_view/test_temp.html'
    def  get_context_data(self, **kwargs):
        context=super(test_templateview,self).get_context_data(**kwargs)
        context['test']='这是一个要传递的变量'
        return context
class test_listview(ListView):
    model=models.department
    template_name = "test_view/test_listview.html"
    context_object_name = "dep_list"
class listviewdemo(ListView):
    template_name = "test_view/listviewdemo.html"
    context_object_name = "person_list"
    def get_queryset(self): #重写 get_queryset 方法，取person性别为女的人员，gander值为'2'
        personlist =models.person.objects.filter(gander='2')
        return personlist
    def get_context_data(self, **kwargs):
        kwargs['loguser'] = models.loguser.objects.all().first()
        return super(listviewdemo, self).get_context_data(**kwargs)
class test_detailview(DetailView):
    model=models.person
    template_name='test_view/testdetail.html'
    context_object_name = 'person'
    pk_url_kwarg = 'personid' # 在urls.p文件中的urlpattern 中定义的URL正则表达式中，实名参数personid
class detailviewdemo(DetailView):
    model = models.person
    template_name = 'test_view/testdetail.html'
    context_object_name = 'person'
    pk_url_kwarg = 'personid'  # 在urls.p文件中的urlpattern 中定义的URL正则表达式中，实名参数personid
    def get_object(self, queryset=None):
        obj = super(detailviewdemo, self).get_object() #调用父类的get_object()
        if obj.gander == '1':
            obj.gander='男'
        else:
            obj.gander = '女'
        return obj
    def get_context_data(self, **kwargs):
        kwargs['test'] = '这一个DetailView类通用视图生的页面'  # 增加一个变量test
        return super(detailviewdemo, self).get_context_data(**kwargs)
#----------------------------test_view的应用-----------------
def login(request):
    if request.method=='POST':
        account=request.POST.get('account')#取得表单提交account的值
        password=request.POST.get('password')#取得表单提交password的值
        remember=request.POST.get('remember') #勾选了checkbox，值是是字符串on， 没勾选就是None
        #print(remember)
        loguser=models.loguser.objects.filter(account=account,password=password).first()#数据库查询用户
        if loguser:
            rep=redirect('/test_view/index/')
            if remember=='on':
                rep.set_cookie('account',account,max_age=60*60*8)
            return rep
        else:
            errmsg='用户名或密码错误！'
            return render(request, 'test_view/login.html',{'errmsg':errmsg})
    account=request.COOKIES.get('account','')
    print(account)
    return render(request,'test_view/login.html',{'account_two':account})
def index(request):
    person_list=models.person.objects.all()
    return render(request,'test_view/index.html',{'person_list':person_list})


def add_person(request):
    if request.method=="POST":
        name=request.POST.get("name")#取得姓名
        email=request.POST.get("email")#取得邮箱地址
        gander=request.POST.get("gander")#性别值
        head_img=request.FILES.get('head_img')#图像文件从request.FILES中取值
        attachment=request.FILES.get('attachment')#文件类型从request.FILES中取值
        #print(attachment)
        new_person=models.person.objects.create(name=name,email=email,gander=gander,head_img=head_img,attachment=attachment)
        return redirect('/test_view/index/')
    return render(request,'test_view/add_person.html')

def del_person(request,personid):
    person_obj=models.person.objects.get(id=personid)
    person_obj.delete()
    return redirect('/test_view/index/')

def edit_person(request,personid):
    if request.method=="POST":
        id = request.POST.get('id')
        name = request.POST.get("name")
        email = request.POST.get("email")
        gander = request.POST.get("gander")
        head_img = request.FILES.get('head_img')
        attachment = request.FILES.get('attachment')
        person=models.person.objects.get(id=id)
        person.name=name
        person.email=email
        person.gander=gander
        if head_img:
            person.head_img=head_img #如果头像文件有值，才修改数据字段的值
        if attachment: #如果上传附件有值，才修改数据字段的值
            person.attachment=attachment
        person.save()
        return redirect('/test_view/index/')
    person_obj=models.person.objects.get(id=personid)

    return render(request, 'test_view/edit_person.html',{'person':person_obj})
