from django.db import models
from utils.rename_upload import RenameUpload

# Create your models here.

class loguser(models.Model):
    account=models.CharField(max_length=32,verbose_name="登录账号")
    password=models.CharField(max_length=20,verbose_name="密码")
    email=models.EmailField(verbose_name="邮箱")
    gander=models.CharField(max_length=1)
    hobby=models.CharField(max_length=20)
    hair=models.CharField(max_length=1)
    img=models.ImageField(upload_to='image',storage=RenameUpload(),blank=True,null=True)
