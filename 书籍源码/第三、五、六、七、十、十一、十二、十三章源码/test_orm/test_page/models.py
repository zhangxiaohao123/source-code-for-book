from django.db import models

class person(models.Model):#员工数据模型（员工数据表）
    name=models.CharField(max_length=32,verbose_name='姓名') #员工姓名
    email=models.EmailField(verbose_name='邮箱')#员工的邮箱
    dep=models.ForeignKey(to="department",to_field="id",on_delete=models.CASCADE) #员工的部门，外键，形成一对多的关系
    salary=models.DecimalField(max_digits=8,decimal_places=2)#薪水,数值型
    def __str__(self):
        return self.name

class department(models.Model):#　部让数据模型（部门数据表）
    dep_name=models.CharField(max_length=32,verbose_name='部门名称',unique=True,blank=False)#部门名称
    dep_script=models.CharField(max_length=60,verbose_name='备注',null=True) #部门备注说明
    def __str__(self):
        return self.dep_name