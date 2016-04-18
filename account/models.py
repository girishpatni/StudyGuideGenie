from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

class SignUp(models.Model):
    first_name = models.CharField(max_length=120,null=False, blank=False)
    last_name =  models.CharField(max_length=120,null=False, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=120,null=False, blank=False,default='12345')
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    
    
    def __unicode__(self):
        return smart_unicode(self.email)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return smart_unicode(self.user.email)

    
