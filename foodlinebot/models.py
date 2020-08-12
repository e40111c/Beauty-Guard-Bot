from django.db import models

# Create your models here.



# Create your models here.
class Music(models.Model):
    song = models.TextField(default="song")
    singer = models.TextField(default="AKB48")
    last_modify_date = models.DateTimeField(auto_now=True)
    state = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"

class CustomerState(models.Model):
    uid = models.TextField()
    cnt = models.IntegerField()
    continuous = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "CustomerState"

class Product(models.Model):
    uid = models.TextField()
    pname = models.TextField()
    pbrand = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "CustomerProduct"
