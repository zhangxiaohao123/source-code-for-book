from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=60)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey('blog.Blog',on_delete=models.CASCADE,)

    def __str__(self):
        return self.text[:20]
