from django.db import models

# Create your models here.
class WebUrl(models.Model):
    url1 = models.CharField(max_length=500,null=True)

class Scrapped(models.Model):
    weburl = models.ForeignKey(WebUrl,on_delete=models.CASCADE,null=True)
    word = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
