from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    facebook_id = models.TextField(null=True)
    is_sms_verified = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.name+" "+self.surname

class Profile(models.Model):

    user = models.ForeignKey('User',on_delete=models.CASCADE)
    email = models.CharField(max_length=32)
    birthday = models.DateField(null=True)
    bio = models.TextField(null=True)
    points = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.name+ " " + self.user.surname