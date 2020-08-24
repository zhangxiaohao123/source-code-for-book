from django.shortcuts import render,HttpResponse
from . import models


# Create your views here.
def person_page(request):
    # 从URL取参数page,这个参数是存在视图生成的HTML代码片段中
    cur_page_num = request.GET.get("page")

    # 取得person中的记录总数
    total_count = models.person.objects.all().count()
    # 设定每一页显示多少条记录
    one_page_lines = 10
    # 页面上总共展示多少页码标签
    page_maxtag = 9
    """"
    根据总记录数，计算出总的页数。
    通过divmod()函数取得商和余数，有余数时，总页数是商加上1
    同时判断当前页的数值是否大于总页数，如果大于总页数，设置当前页数等于最后一页的页数
    """
    total_page, remainder = divmod(total_count, one_page_lines)
    if remainder:
        total_page += 1
    try:
        #参数page传递进来是字符型数值，因此需要转化为整数类型
        cur_page_num = int(cur_page_num)
        # 如果输入的页码数超过了最大的页码数，设置当前页数是最后一页的页数
        if cur_page_num > total_page:
            cur_page_num = total_page
    except Exception as e:
        # 当输入的页码不是正整数时， 设置当前页数是第一页的页数
        cur_page_num = 1

    # 定义两个变量，指定表中取出的记录开始数，以及当前页记录结束的位置
    rows_start = (cur_page_num-1)*one_page_lines
    rows_end = cur_page_num * one_page_lines
    #如果页数小于每页设置的页码标签数，设置每页页码标签数为总页数
    if total_page < page_maxtag:
        page_maxtag = total_page
    #把当前页码标签放在中间，前面放一半页码标签，后面放一半页码标签
    #因此现把页面上放置的页码标签数除以2
    half_page_maxtag = page_maxtag // 2
    # 页面上页码开始
    page_start = cur_page_num - half_page_maxtag
    # 页面上页码结束
    page_end = cur_page_num + half_page_maxtag
    """
    如果当前页减一半,小于1,页面中页码标签设置从1开始，
    页面中页码标签等页面中页码标签数
    """
    if page_start <= 1:
        page_start = 1
        page_end =  page_maxtag
    """
    如果当前页加 一半 比总页码数大,设置最后的页码标签值为总页数
    页面中页码标签起始等于总页数减掉页码标签数加1
    """
    if page_end >= total_page:
        page_end = total_page
        page_start = total_page -  page_maxtag +1
        if page_start <= 1:
            page_start = 1


    #对person表中的记录进行切片，取出属于本页的记录
    per_list = models.person.objects.all()[rows_start:rows_end]

    # 初始一个列表变量，用来保存拼接分页的HTML代码
    html_page = []
    # 首页代码
    html_page.append('<li><a href="/test_page/person_page/?page=1">首页</a></li>')
    #  上一页页码标签的HTML代码，如果当前是第一页，设置上一页标签为非可用状态
    if cur_page_num <= 1:
        html_page.append('<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'.format(cur_page_num-1))
    else:
        # 上一页页码标签的HTML代码
        html_page.append('<li><a href="/test_page/person_page/?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(cur_page_num-1))
    #依次取页码标签，注意切片函数用法
    for i in range(page_start, page_end+1):
        # 如果是当前页就加一个active样式类
        if i == cur_page_num:
            html_temp = '<li class="active"><a href="/test_page/person_page/?page={0}">{0}</a></li>'.format(i)
        else:
            html_temp = '<li><a href="/test_page/person_page/?page={0}">{0}</a></li>'.format(i)
        html_page.append(html_temp)

    # 下一页的页码标签的HTML代码
    # 判断，如果是最后一页，就没有下一页
    if cur_page_num >= total_page:
        html_page.append('<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
    else:
        html_page.append('<li><a href="/test_page/person_page/?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(cur_page_num+1))
    # 最后一页的页码标签的HTML代码
    html_page.append('<li><a href="/test_page/person_page/?page={}">尾页</a></li>'.format(total_page))
    #把HTML联结起来
    page_nav = "".join(html_page)

    return render(request,'test_page/list_person.html',{'person_list':per_list,'page_nav':page_nav})

from utils.paginater import Paginater
def person_pagenew(request):
    # 从URL取参数page,这个参数是存在视图生成的HTML代码片段中
    cur_page_num = request.GET.get("page")
    if not cur_page_num:
        cur_page_num="1"
    print(cur_page_num, type(cur_page_num))
    # 取得person中的记录总数
    total_count = models.person.objects.all().count()
    # 设定每一页显示多少条记录
    one_page_lines = 6
    # 页面上总共展示多少页码标签
    page_maxtag = 9
    page_obj=Paginater( url_address='/test_page/person_pagenew/', cur_page_num=cur_page_num, total_rows=total_count, one_page_lines=one_page_lines, page_maxtag=page_maxtag)
    # 对person表中的记录进行切片，取出属于本页的记录
    per_list = models.person.objects.all()[page_obj.data_start:page_obj.data_end]
    return render(request, 'test_page/list_person.html', {'person_list': per_list, 'page_nav': page_obj.html_page()})
