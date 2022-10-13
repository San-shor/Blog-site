from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    writter=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_writter')
    bTitle=models.CharField(max_length=264,verbose_name="Give a title")
    slug=models.SlugField(max_length=264,unique=True)
    bContent=models.TextField(verbose_name="What is on your mind?")
    image=models.ImageField(upload_to='blog_images',verbose_name="image")
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-publish_date',)

    def __str__(self):
        return self.bTitle

class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comments=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comments

class Like(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_like')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_like')


    def __str__(self):
        return sel.user+"likes"+self.blog
