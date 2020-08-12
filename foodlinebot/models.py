from django.db import models


class CustomerStatus(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True)  # 地區
    continuous = models.IntegerField(blank=True, null=True)  # 景點名稱
    nid = models.AutoField(primary_key=True)  # 地址


        
        

# Create your models here.
