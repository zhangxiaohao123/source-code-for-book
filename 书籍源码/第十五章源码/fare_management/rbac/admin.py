from django.contrib import admin
from rbac import models
admin.site.register(models.Menu)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['title','url','perm_code','perm_group','pid']

admin.site.register(models.Permission,PermissionAdmin)
class PermGroupAdmin(admin.ModelAdmin):
    list_display = ['title','menu']
admin.site.register(models.PermGroup,PermGroupAdmin)
admin.site.register(models.Role)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username','password','nickname','email']
admin.site.register(models.UserInfo,UserInfoAdmin)

