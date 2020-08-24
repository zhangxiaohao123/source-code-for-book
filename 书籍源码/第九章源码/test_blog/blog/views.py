from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from . import models
from comments.forms import CommentForm
from django.views.generic import ListView,DetailView
from django.contrib.auth.models import auth

from django.db.models import Q


class indexview(ListView):
    model = models.Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # 首先获得父类生成的传递给模板的字典。
        context = super().get_context_data(**kwargs)

        paginator = context.get('paginator')
        pageobj = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        #设置每页显示的页码标签数
        show_pagenumber=7
        # 调用自定义 get_page_data 方法获得显示分页导航条需要的数据
        page_data = self.get_page_data(is_paginated, paginator, pageobj, show_pagenumber)
        # 将page_data变量更新到 context 中，注意 page_data 是一个字典。
        context.update(page_data)
        context['tabname'] = 'firsttab'
        # 将更新后的 context 返回，以便 ListView 使用这个字典中的模板变量去渲染模板。
        # 注意此时 context 字典中已有了显示分页导航条所需的数据。
        return context

    def get_page_data(self,is_pageinated,paginator,pageobj,show_pagenumber):
        # 如果没有分页，返加空字典
        if not is_pageinated:
            return {}
        """
        分页数据有三部分组成，
        左边用left存页码,右边用right存页码，中间部分就是当前页page_obje.number
        lefe,right都初始列表
        """
        left=[]
        right=[]

        #当前页面数值的获取,得用户当前请求的页码号
        cur_page=pageobj.number
        print('cur_page',cur_page)
        #取出分页中最后的页码
        total=paginator.num_pages
        #得到显示页数的一半，‘//’可以取得两数相除的商的整数部分
        half=show_pagenumber//2
        print(half)
        #取出当前页面前(letf)显示页标签个数,注意range(）如：range(start, stop)用法，计数从 start 开始， 计数到 stop 结束但不包括 stop
        for i in range(cur_page - half,cur_page):
        #数值大于等于1时，才取数值放到left列表中
            if i>=1:
                left.append(i)
        # 取出当前页后前(right)显示页标签个数,再次提示注意range()用法
        for i in range(cur_page+1, cur_page + half +1):
            # 数值小于等于页数的最大页数时，才取数值放到right列表中
            if i <= total:
                right.append(i)
        page_data={
            'left':left,
            'right':right,
        }
        return page_data


class blogdetailview(DetailView):
    model = models.Blog
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    pk_url_kwarg = 'pk'
    def get_object(self,queryset=None):
        blog=super(blogdetailview,self).get_object(queryset=None)
        blog.increase_views()
        return blog
    def get_context_data(self,**kwargs):
        context=super(blogdetailview,self).get_context_data(**kwargs)
        form=CommentForm()
        comment_list=self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_list':comment_list
        })
        return context



def archives(request, year, month):
   blog_list = models.Blog.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
   return render(request, 'blog/index.html', context={'blog_list':blog_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    blog_list = models.Blog.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'Blog_list':blog_list})

class categoryview(ListView):
    model=models.Blog
    template_name='blog/index.html'
    context_object_name='blog_list'
    def get_queryset(self):
        cate=get_object_or_404(models.Category,pk=self.kwargs.get('pk'))
        return super(categoryview,self).get_queryset().filter(category=cate).order_by('-created_time')

class tagview(ListView):
    model=models.Blog
    template_name='blog/index.html'
    context_object_name='blog_list'
    def get_queryset(self):
        tag=get_object_or_404(models.Tag,pk=self.kwargs.get('pk'))
        return super(tagview,self).get_queryset().filter(tags=tag).order_by('created_time')

def search(request):
    print('qqqqq')
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = "请输入关键词"
        return render(request, 'blog/index.html', {'error_msg': error_msg})
    blog_list = models.Blog.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'error_msg': error_msg,'blog_list':blog_list})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username") #从提交过来的数据提取用户名和密码
        pwd = request.POST.get("password")
        user = auth.authenticate(username=username, password=pwd) # 利用auth模块做用户名和密码的校验
        #print(type(user),user)
        if user:
            auth.login(request, user)  # 用户登录，并将登录用户赋值给request.user
            return redirect("/")
        else:
            errormsg="用户名或密码错误！"
            return render(request,'blog/login.html',{'error':errormsg})
    return render(request,'blog/login.html')

# 注册的视图函数
from . import forms
def registe(request):
    if request.method == "POST":
        #form_obj = forms.reg_form(request.POST)#有图片上传,这个句代码是错误的!!!!!!!!!!!
        form_obj = forms.reg_form(request.POST,request.FILES)
        if form_obj.is_valid(): # 判断校验是否通过
            form_obj.cleaned_data.pop("repassword")
            #head_img = request.FILES.get("head_img")
            user_obj=models.loguser.objects.create_user(**form_obj.cleaned_data,is_staff=1,is_superuser=1)
            #obj.is_staff
            auth.login(request, user_obj)  # 用户登录，可将登录用户赋值给request.user
            return redirect('/')
        else:
            #print(form_obj['repassword'].errors)
            return render(request, "blog/registe.html", {"formobj": form_obj})
    form_obj = forms.reg_form()# 生成一个form对象
    return render(request, "blog/registe.html", {"formobj": form_obj})



def myindex(request,userid):
   blog_list = Blog.objects.filter(id=userid).order_by('-created_time')
   tabname='mytab'
   return render(request, 'blog/index.html', context={'blog_list':blog_list,'tabname':tabname})

class myindex(ListView):
    model = models.Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'
    def get_queryset(self):
        loguser=get_object_or_404(models.loguser,pk=self.kwargs.get('loguserid'))
        return super(myindex,self).get_queryset().filter(author=loguser).order_by('-created_time')
    def get_context_data(self, **kwargs):
        context=super(myindex,self).get_context_data(**kwargs)
        context['tabname']='mytab'
        return context

class authorindex(ListView):
    model = models.Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'
    def get_queryset(self):
        user=get_object_or_404(models.loguser,pk=self.kwargs.get('id'))
        return super(authorindex,self).get_queryset().filter(author=user).order_by('-created_time')
    def get_context_data(self, **kwargs):
        context=super(authorindex,self).get_context_data(**kwargs)
        context['tabname']='firsttab'
        return context


def logout(request):
    auth.logout(request)
    return redirect("/")

#-------------------测试前台使用django ckeditor-----------
def test_ckeditor_front(request):
    user_obj = models.loguser.objects.all().first()
    auth.login(request, user_obj)

    blog=models.Blog.objects.get(id=1)
    return render(request,'blog/test_ckeditor_front.html',{'blog':blog})
"""
"""
