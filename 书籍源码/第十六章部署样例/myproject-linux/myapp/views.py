
from django.shortcuts import HttpResponse,render,redirect

# Create your views here.
def index(request):
    return HttpResponse('<h1>hello word</h1>')

def test(request):
    hi='你好，世界是美好的'
    test='这是一个测试页，动态页面正常显示，测试成功！'
    return render(request,"test.html",{'hi':hi,'test':test})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username=='test' and password=='123'):
            return redirect('/test/')
        else:
            return render(request, "login.html", {'error': '用户名或密码错误！'})

def template_test(request):
    v_list=['程序员','产品经理','产品销售','架构师']#列表变量
    v_dic={"name":"张三","age":16,"love":"美女"} #字典变量，注意：key名字一定包含在引号中！！
    class  coder(object): #类，有属性name,language,hair,有一个方法hope
        def __init__(self,name,language,hair): #初始化，为三个属性赋值
            self.name=name
            self.language=language
            self.hair=hair
        def hope(self): #类的方法，函数hope
            return '{}的希望是程序少出bug，工作少加班，工资开得多！'.format(self.name)
    zhang=coder('张三','python','多')#实例化类，生成类对象
    li=coder('李四','php','不多不少')#实例化类，生成类对象
    wang=coder('王五','c#','少')#实例化类，生成类对象
    coders=[zhang,li,wang]#建立列表变量coders,把类对象作为列表中的元素
    return render(request,'test_template.html',{'v_list':v_list,'v_dic':v_dic,'coders':coders}) #向html文件传参数

def test_filter(request):
    vhair="fewhair"
    return render(request,'test_filter.html',{"hair":vhair})


def test_for(request):
    v_list = ['程序员', '产品经理', '产品销售', '架构师','老板','员工']  # 列表变量
    return render(request,'test_for.html',{'vlist':v_list})

def test_tag(request):
    return render(request,'test_tag.html')

def test_inclusion_tag(request):
    return render(request,'test_inclusion_tag.html')

def test_basehtml(request):
    return render(request,'base.html')

def test_inhert(request):
    return render(request,'inhert_base.html')


def hello(request):
    return render(request,'hello.html')
def ny(request,year,month):
    year1=str(year)+'年'
    month1=str(month)+'月'
    return render(request,'ny.html',{'year':year1,'month':month1})

from django.urls import reverse

def name(request,username):
    if username=='redirectny':
        return redirect(reverse('ny',args=(2019,6,)))
    else:
        wellcome='欢迎您，'+username
        return render(request,'name.html',{'wellcome':wellcome})


