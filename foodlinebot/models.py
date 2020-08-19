from django.db import models

# Create your models here.



# Create your models here.

class CustomerState(models.Model):
    uid = models.TextField()
    cnt = models.IntegerField()
    continuous = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Customer_State"

class Product(models.Model):
    uid = models.TextField()
    pname = models.TextField()
    pbrand = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Customer_Product"
        
class CosmeticProduct(models.Model):
    kind = models.TextField()
    brand = models.TextField()
    pname = models.TextField()
    char = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = 'Cosmetic_Product'
        
class UserProduct(models.Model):
    uid = models.TextField()
    pname = models.TextField()
    pbrand = models.TextField()
    fit_prod = models.TextField()  # Field name made lowercase.
    unfit_prod = models.TextField()  # Field name made lowercase.
    reg_date = models.DateTimeField()

    class Meta:
        db_table = 'User_Product'

class CosmeticIngredient(models.Model):
    pname = models.TextField()
    ingredient = models.TextField()
    acne = models.TextField()
    pchar = models.TextField()
    dalton = models.TextField()
    safeness = models.TextField()
    stimulation = models.TextField()
    score = models.TextField()

    class Meta:
        db_table = 'Cosmetic_Ingredient'    
        
class Picture(models.Model):
    skincare = models.TextField()
    foundation = models.TextField()
    cosmetic = models.TextField()
    

    class Meta:
        db_table = "Cosemetic_Picture"
        
