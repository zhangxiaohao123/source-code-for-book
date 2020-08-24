from django.db import models

class book(models.Model):
    title=models.CharField(max_length=20,verbose_name='图书名称') #利用verbose_name属性让字段显示汉字名称
    descript=models.TextField(verbose_name='书籍简介')
    publishdate=models.DateField(verbose_name='出版日期')
    publishing=models.ForeignKey(to='publishing',on_delete=models.CASCADE,verbose_name='出版社')  #外键，多对一关系,一定加上on_delete
    author=models.ManyToManyField(to='author',verbose_name='作者') #多对多键
    class Meta:
        verbose_name='图书信息'
        verbose_name_plural='图书信息'
    def __str__(self):
        return self.title+'--相关图书信息'
class publishing(models.Model):
    name=models.CharField(max_length=20,verbose_name='出版社名称')
    address=models.CharField(max_length=20,verbose_name='出版社地址')
    class Meta:
        verbose_name='出版社信息'
        verbose_name_plural='出版社书信息'
    def __str__(self):
        return '社名：'+self.name

class author(models.Model):
    name=models.CharField(max_length=10,verbose_name='姓名')
    email=models.EmailField(verbose_name='邮箱地址')
    birthday=models.DateField(verbose_name='出生日期')
    header=models.ImageField(verbose_name='作者头像')
    class Meta:
        verbose_name = '作者基本情况'
        verbose_name_plural = '作者基本情况'
    def __str__(self):
            return '作者：'+self.name




