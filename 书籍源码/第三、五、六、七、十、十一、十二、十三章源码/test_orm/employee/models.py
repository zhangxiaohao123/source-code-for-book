from django.db import models

#Create your models here.
class employee(models.Model):#员工数据模型（员工数据表）
    name=models.CharField(max_length=32,verbose_name='姓名') #员工姓名
    email=models.EmailField(verbose_name='邮箱')#员工的邮箱
    dep=models.ForeignKey(to="department",to_field="id",on_delete=models.CASCADE) #员工的部门，外键，形成一对多的关系
    group=models.ManyToManyField(to="group")#员工加入的团体，多对多关系，就是一个员工可以加入多个团体，一个团体有多个员工
    salary=models.DecimalField(max_digits=8,decimal_places=2)#薪水,数值型
    info = models.OneToOneField(to='employeeinfo',on_delete=models.CASCADE,null=True)#员工补充信息，一对一关系
class department(models.Model):#　部让数据模型（部门数据表）
    dep_name=models.CharField(max_length=32,verbose_name='部门名称',unique=True,blank=False)#部门名称
    dep_script=models.CharField(max_length=60,verbose_name='备注',null=True) #部门备注说明

class group(models.Model):#团体数据模型（团体数据表）
    group_name=models.CharField(max_length=32,verbose_name='团体名称',unique=True,blank=False) #　团体名称
    group_script=models.CharField(max_length=60,verbose_name='备注',null=True) #团体备注说明

class employeeinfo(models.Model): #员工补充信息
    phone = models.CharField(max_length=11) #电话号码
    address = models.CharField(max_length=50)#电话号码

#----------------------------------


