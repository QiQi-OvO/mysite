from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BlogType (models.Model):
    type_name = models.CharField(max_length=20)
    def __str__(self):
        return self.type_name
class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<Blog: %s>" % self.title