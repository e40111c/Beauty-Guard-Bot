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

class Product(models.Model):
    uid = models.TextField(default=None, blank=True, null=True)
    pname = models.TextField(default=None, blank=True, null=True)
    pbrand = models.TextField(default=None, blank=True, null=True)


    class Meta:
        db_table = "Customer_Product"
        

        
class UserProduct(models.Model):
    uid = models.TextField(default=None, blank=True, null=True)
    pname = models.TextField(default=None, blank=True, null=True)
    pbrand = models.TextField(default=None, blank=True, null=True)
    fit_prod = models.TextField(default=None, blank=True, null=True)  # Field name made lowercase.
    unfit_prod = models.TextField(default=None, blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        db_table = 'User_Product'

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
        
class Picture(models.Model):
    uid = models.TextField(default=None, blank=True, null=True)
    skincare = models.TextField(default=None, blank=True, null=True)
    foundation = models.TextField(default=None, blank=True, null=True)
    cosmetic = models.TextField(default=None, blank=True, null=True)
    

    class Meta:
        db_table = "Cosemetic_Picture"
        

class Temp(models.Model):
    uid = models.TextField(default=None, blank=True, null=True)
    pname = models.TextField(default=None, blank=True, null=True)
    price = models.IntegerField(default=None, blank=True, null=True)
    brand = models.TextField(default=None, blank=True, null=True)

    class Meta:
        db_table = "Temp_p" 

