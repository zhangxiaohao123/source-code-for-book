# -*- coding: UTF-8 -*-
from django.core.files.storage import FileSystemStorage
class RenameUpload(FileSystemStorage):
    from django.conf import settings

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # 初始化
        super(RenameUpload, self).__init__(location, base_url)

    def _save(self, name, content): # 重写 _save方法, name为上传文件名称
        import os, time, random
        ext = os.path.splitext(name)[1] # 文件扩展名
        d = os.path.dirname(name) # 文件目录
        fn = time.strftime('%Y%m%d%H%M%S') # 定义文件名，年月日时分秒随机数
        fn = fn + '_%d' % random.randint(0, 100)
        name = os.path.join(d, fn + ext) # 重写合成文件名
        return super(RenameUpload, self)._save(name, content) # 调用父类方法
