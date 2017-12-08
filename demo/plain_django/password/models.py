from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)

class Password(models.Model):
    user = models.ForeignKey(UserProfile, null=True)
    site_url = models.CharField(max_length=1024)
    site_username = models.CharField(max_length=1024)
    site_password = models.CharField(max_length=1024)


