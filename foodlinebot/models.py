from django.db import models

# Create your models here.

class CosmeticProduct(models.Model):
    kind = models.CharField(default=None, blank=True, null=True,max_length=100)
    product = models.CharField(default=None, blank=True, null=True,max_length=100)
    brand = models.CharField(default=None, blank=True, null=True,max_length=100)
    pname = models.CharField(default=None, blank=True, null=True,max_length=100)
    price = models.IntegerField(default=None, blank=True, null=True)
    suitable = models.CharField(default=None, blank=True, null=True,max_length=100)
    picurl = models.CharField(default=None, blank=True, null=True,max_length=100)

    class Meta:
        db_table = 'Cosmetic_Product'



class CustomerState(models.Model):
    uid = models.CharField(default=None, blank=True, null=True,max_length=100)
    cnt = models.IntegerField(default=None, blank=True, null=True)
    continuous = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        db_table = "Customer_State"



        
class User_Product(models.Model):
    uid = models.CharField()
    wait_prod = models.CharField(default=None, blank=True, null=True,max_length=100)
    unfit_prod = models.CharField(default=None, blank=True, null=True,max_length=100)
    fit_prod = models.CharField(default=None, blank=True, null=True,max_length=100)
    picurl = models.TextField(default=None, blank=True, null=True)
    ingredient = models.TextField(default=None, blank=True, null=True)
    acne = models.TextField(default=None, blank=True, null=True)
    pchar = models.TextField(default=None, blank=True, null=True)
    dalton = models.TextField(default=None, blank=True, null=True)
    safeness = models.TextField(default=None, blank=True, null=True)
    stimulation = models.TextField(default=None, blank=True, null=True)
    score = models.TextField(default=None, blank=True, null=True)
    ptype = models.TextField(default=None, blank=True, null=True)
    suitable = models.TextField(default=None, blank=True, null=True)

    class Meta:
        db_table = "UserProduct"

class CosmeticIngredient(models.Model):
    pname = models.CharField(default=None, blank=True, null=True,max_length=100)
    ingredient = models.TextField(default=None, blank=True, null=True)
    acne = models.TextField(default=None, blank=True, null=True)
    pchar = models.TextField(default=None, blank=True, null=True)
    dalton = models.TextField(default=None, blank=True, null=True)
    safeness = models.TextField(default=None, blank=True, null=True)
    stimulation = models.TextField(default=None, blank=True, null=True)
    score = models.TextField(default=None, blank=True, null=True)

    class Meta:
        db_table = 'Cosmetic_Ingredient'    
    

class Temp(models.Model):
    uid = models.CharField(default=None, blank=True, null=True,max_length=100)
    pname = models.CharField(default=None, blank=True, null=True,max_length=100)
    price = models.IntegerField(default=None, blank=True, null=True)
    brand = models.CharField(default=None, blank=True, null=True,max_length=100)
    product = models.CharField(default=None, blank=True, null=True,max_length=100)
    userproduct = models.CharField(default=None, blank=True, null=True,max_length=100)
    userkind = models.CharField(default=None, blank=True, null=True,max_length=100)


    class Meta:
        db_table = "Temp_p"

