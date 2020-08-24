from django.db import models

# Create your models here.

class CosmeticProduct(models.Model):
    kind = models.TextField(default=None, blank=True, null=True)
    product = models.TextField(default=None, blank=True, null=True)
    brand = models.TextField(default=None, blank=True, null=True)
    pname = models.TextField(default=None, blank=True, null=True)
    price = models.IntegerField(default=None, blank=True, null=True)
    suitable = models.TextField(default=None, blank=True, null=True)
    picurl = models.TextField(default=None, blank=True, null=True)

    class Meta:
        db_table = 'Cosmetic_Product'



class CustomerState(models.Model):
    uid = models.TextField(default=None, blank=True, null=True)
    cnt = models.IntegerField(default=None, blank=True, null=True)
    continuous = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        db_table = "Customer_State"



        
class User_Product(models.Model):
    uid = models.TextField()
    wait_prod = models.TextField(default=None, blank=True, null=True)
    unfit_prod = models.TextField(default=None, blank=True, null=True)
    fit_prod = models.TextField(default=None, blank=True, null=True)
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
    pname = models.TextField(default=None, blank=True, null=True)
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
    uid = models.TextField(default=None, blank=True, null=True)
    pname = models.TextField(default=None, blank=True, null=True)
    price = models.IntegerField(default=None, blank=True, null=True)
    brand = models.TextField(default=None, blank=True, null=True)
    product = models.TextField(default=None, blank=True, null=True)
    userproduct = models.TextField(default=None, blank=True, null=True)
    userkind = models.TextField(default=None, blank=True, null=True)


    class Meta:
        db_table = "Temp_p"

