from django.db import models
from rbac import models as rbac_models

# Create your models here.
class carinfo(models.Model):
    plate_number=models.CharField(max_length=7,verbose_name='车牌号',unique=True)
    driver=models.CharField(max_length=10,verbose_name='司机')
    price=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='单价')
    remarks=models.CharField(max_length=32,verbose_name='备注说明',blank=True,null=True)
    def __str__(self):
        return self.plate_number

class loguser(models.Model):#员工数据模型（员工数据表）
    user_obj=models.OneToOneField(to=rbac_models.UserInfo,on_delete=models.CASCADE,null=True,blank=True)
    head_img = models.ImageField(upload_to='headimage', blank=True, null=True, verbose_name='头像')  # 头像
    dep=models.ForeignKey(to="department",to_field="id",on_delete=models.CASCADE,blank=True,null=True) #员工的部门，外键，形成一对多的关系

    def __str__(self):
        return self.user_obj.username

class department(models.Model):#　部让数据模型（部门数据表）
    dep_name=models.CharField(max_length=32,verbose_name='部门名称',unique=True,blank=False)#部门名称
    dep_script=models.CharField(max_length=60,verbose_name='备注',null=True) #部门备注说明
    def __str__(self):
        return self.dep_name
class fare(models.Model):
    dep=models.ForeignKey(to="department",to_field="id",on_delete=models.CASCADE) #员工的部门，外键，形成一对多的关系
    passenger=models.CharField(max_length=32,verbose_name='乘车人')
    car=models.ForeignKey(to='carinfo',on_delete=models.CASCADE)
    driver = models.CharField(max_length=10, verbose_name='司机')
    price=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='单价')
    distance=models.IntegerField(verbose_name='公里数')
    fare=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='车费')
    drive_date=models.DateField(auto_now_add=True,verbose_name='乘车时间',blank=True,null=True)
    remark=models.CharField(max_length=100,verbose_name='乘车说明')
    oprator=models.CharField(max_length=32,verbose_name='录入人员')
    approve_date=models.DateField(verbose_name='审批时间',auto_now=True,blank=True,null=True)
    approve_status=models.CharField(max_length=1,choices=(('0','未审批'),('1','通过审批')),verbose_name='审批状态',blank=True,null=True)

