from django.contrib import admin
from .models import Blog,Category,Tag,loguser

class BlogAdmin (admin.ModelAdmin):
    list_display=("title","created_time","modified_time","category","author","views",)
admin.site.register(loguser)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)

