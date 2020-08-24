from django.db import models
from django.urls import reverse
# Create your models here.
class department(models.Model):#　部门数据模型（部门数据表）
    dep_name=models.CharField(max_length=32,verbose_name='部门名称',unique=True,blank=False)#部门名称
    dep_script=models.CharField(max_length=60,verbose_name='备注',null=True) #部门备注说明
    def get_absolute_url(self):
        return reverse('depdetail',kwargs={'dep_id':self.pk})
class loguser(models.Model):
    account=models.CharField(max_length=32,verbose_name="登录账号")
    password=models.CharField(max_length=20,verbose_name="密码")

class person(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')  # 姓名
    email = models.EmailField(verbose_name="邮箱") #邮箱
    gander = models.CharField(max_length=1, choices=(("1", "男"), ("2", "女"),),verbose_name='性别') #性别
    head_img = models.ImageField(upload_to='headimage',  blank=True, null=True,verbose_name='头像') #头像
    attachment=models.FileField(upload_to='filedir',blank=True,null=True,verbose_name='附件') #附件，文件类型字段
