from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(default=None,max_length=25,null=True)
    dp = models.ImageField(upload_to='post_images',null=True,blank=True,default='post_images/dp.png') 
    follows = models.ManyToManyField('self',related_name='followed_by',symmetrical=False,blank=True)
    bio = models.CharField(default=None,max_length=50,null=True,blank=True)
    def __str__(self): 
        return str(self.user)

class Post(models.Model):
    author = models.ForeignKey('Profile',on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post_images')
    caption = models.CharField(default=None,max_length=100)
    git = models.URLField(max_length=128,unique=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author)+'_'+str(self.pk)

    class Meta:
        ordering = ['-post_date']
    