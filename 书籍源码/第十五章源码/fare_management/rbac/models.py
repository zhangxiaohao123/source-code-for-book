from django.db import models



class Role(models.Model):
    """
    角色：与权限关联，与权限表是多对多关系
    """
    title = models.CharField(max_length=32, unique=True,verbose_name="角色名")
    permissions = models.ManyToManyField("Permission",blank=True,verbose_name="拥有权限")   # 定义角色和权限的多对多关系

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural="角色表"

class Permission(models.Model):
    """
    权限
    """
    title = models.CharField(max_length=32, unique=True,verbose_name="权限名称")
    url = models.CharField(max_length=128, unique=True,verbose_name="URL")

    perm_code=models.CharField(max_length=32,verbose_name="权限代码")
    perm_group=models.ForeignKey(to='PermGroup',blank=True,on_delete=models.CASCADE,verbose_name="所属权限组")
    pid=models.ForeignKey(to='Permission',null=True,blank=True,on_delete=models.CASCADE,verbose_name="所属二级菜单")

    def __str__(self):
        # 显示带菜单前缀的权限
        return self.title
    class Meta:
        verbose_name_plural="权限表"

class PermGroup(models.Model):
    title = models.CharField(max_length=32,verbose_name="组名称")
    menu = models.ForeignKey(to="Menu",verbose_name="所属菜单",blank=True,on_delete=models.CASCADE)  #一个组下有多个菜单
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "权限组"

class UserInfo(models.Model):
    """
    用户：
    """
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=32)
    email = models.EmailField()

    roles = models.ManyToManyField("Role")   # 定义用户和角色的多对多关系

    def __str__(self):
        return self.nickname
    class Meta:
        verbose_name_plural="用户表"


class Menu(models.Model):
    """
    菜单
    """
    title = models.CharField(max_length=32, unique=True,verbose_name="一级菜单")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="一级菜单表"






