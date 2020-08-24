from django.db import models

class person(models.Model):#员工数据模型（员工数据表）
    name=models.CharField(max_length=32,verbose_name='姓名') #员工姓名
    email=models.EmailField(verbose_name='邮箱')#员工的邮箱
    salary=models.DecimalField(max_digits=8,decimal_places=2)#薪水,数值型
    def __str__(self):
        return self.name
