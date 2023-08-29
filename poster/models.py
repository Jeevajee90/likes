from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.
def getFilename(request,filename):
    now_time =datetime.datetime.now().strftime("%Y%n%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)


class upload_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=getFilename,null=False, blank=False)
    description = models.CharField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-public,1-private")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.file.name}'
    
    