class Paginater():

    def __init__(self, url_address,cur_page_num, total_rows,  one_page_lines=10, page_maxtag=9):
        """
        url_adress: 页码标签href的地址
        cur_page_num: 当前页码数
        total_rows: 数据模型的记录总数
        one_page_lines: 每页显示多少条记录
        page_maxtag: 页面上显示页码标签的个数
        """
        self.url_address = url_address
        self.page_maxtag=page_maxtag

        """
        根据总记录数，计算出总的页数。
        通过divmod()函数取得商和余数，有余数时，总页数是商加上1
        同时判断当前页的数值是否大于总页数，如果大于总页数，设置当前页数等于最后一页的页数
        """
        total_page, remainder = divmod(total_rows, one_page_lines)
        if remainder:
            total_page += 1
        self.total_page = total_page
        try:
            # 参数page传递进来是字符型数值，因此需要转化为整数类型
            cur_page_num = int(cur_page_num)
            # 如果输入的页码数超过了最大的页码数，设置当前页数是最后一页的页数
            if cur_page_num > total_page:
                cur_page_num = total_page
            #避免出现当前页数为0
            if cur_page_num == 0:
                cur_page_num=1
        except Exception as e:
            # 当输入的页码不是正整数时， 设置当前页数是第一页的页数
            cur_page_num = 1
        self.cur_page_num = cur_page_num

        # 定义两个变量，指定表中取出的记录开始数，以及当前页记录结束的位置
        self.rows_start = (cur_page_num - 1) * one_page_lines
        self.rows_end = cur_page_num * one_page_lines
        # 如果页数小于每页设置的页码标签数，设置每页页码标签数为总页数
        if total_page < page_maxtag:
            page_maxtag = total_page
        # 把当前页码标签放在中间，前面放一半页码标签，后面放一半页码标签
        # 因此现把页面上放置的页码标签数除以2
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
            page_end = page_maxtag
        """
        如果当前页加 一半 比总页码数大,设置最后的页码标签值为总页数
        页面中页码标签起始等于总页数减掉页码标签数加1
        """
        if page_end >= total_page:
            page_end = total_page
            page_start = total_page - page_maxtag + 1
            if page_start <= 1:
                page_start = 1
        self.page_start=page_start
        self.page_end=page_end


    def html_page(self):
        # 初始一个列表变量，用来保存拼接分页的HTML代码
        html_page = []
        # 首页代码
        html_page.append('<li><a href="{}?page=1">首页</a></li>'.format(self.url_address))
        #  上一页页码标签的HTML代码，如果当前是第一页，设置上一页标签为非可用状态
        if self.cur_page_num <= 1:
            html_page.append('<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                self.cur_page_num - 1))
        else:
            # 上一页页码标签的HTML代码
            html_page.append('<li><a href="{}?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(self.url_address, self.cur_page_num-1))
        # 依次取页码标签，注意切片函数用法
        for i in range(self.page_start, self.page_end + 1):
            # 如果是当前页就加一个active样式类
            if i == self.cur_page_num:
                tmp = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.url_address, i)
            else:
                tmp = '<li><a href="{0}?page={1}">{1}</a></li>'.format(self.url_address, i)
            html_page.append(tmp)

        # 下一页的页码标签的HTML代码
        # 判断，如果是最后一页，就没有下一页
        if self.cur_page_num >= self.total_page:
            html_page.append('<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
        else:
            html_page.append('<li><a href="{}?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(self.url_address, self.cur_page_num+1))
        # 最后一页的页码标签的HTML代码
        html_page.append('<li><a href="{}?page={}">尾页</a></li>'.format(self.url_address, self.total_page))
        # 把HTML联结起来
        page_nav = "".join(html_page)
        return page_nav

    @property
    def data_start(self):
        return self.rows_start

    @property
    def data_end(self):
        return self.rows_end

