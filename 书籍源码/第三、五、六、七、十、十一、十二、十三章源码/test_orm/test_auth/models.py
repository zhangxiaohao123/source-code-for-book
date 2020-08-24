from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

# Create your models here.
class authority(models.Model):
    codename = models.CharField("权限代码", max_length=32)
    url = models.CharField('URL配置项名称', max_length=128)
    name = models.CharField('权限描述', max_length=120)

    def save(self, *args, **kwargs):
        #
        content_type_obj = ContentType.objects.get(app_label='test_auth', model='authority')
        permission = Permission.objects.create(codename=self.codename,
                                               name=self.name,
                                               content_type=content_type_obj)
        super(authority, self).save(*args, **kwargs)  # 调用父类的 save 方法将数据保存到数据库中
    def delete(self, *args,**kwargs):
        content_type_obj = ContentType.objects.get(app_label='test_auth', model='authority')
        permission=Permission.objects.get(codename=self.codename,
                              content_type=content_type_obj)
        permission.delete()
        super(authority, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name
