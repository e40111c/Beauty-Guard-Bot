from django.db import models

class Product(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True)
    pname = models.CharField(max_length=255, blank=True, null=True)
    pbrand = models.CharField(max_length=255, blank=True, null=True)
    reg_date = models.DateTimeField()
    nid = models.AutoField(primary_key=True)
    

    class Meta:
        db_table = 'product'

class CustomerStatus(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True)
    continuous = models.IntegerField(blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)
    reg_date = models.DateTimeField()
    nid = models.AutoField(primary_key=True)
    

    class Meta:
        db_table = 'customer_status'
        
        
        
class CustomerProduct(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True)
    pname = models.CharField(max_length=255, blank=True, null=True)
    pbrand = models.CharField(max_length=255, blank=True, null=True)
    fit_prod = models.TextField(db_column='fit_Prod', blank=True, null=True)  # Field name made lowercase.
    unfit_prod = models.TextField(db_column='unfit_Prod', blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateTimeField()
    nid = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'customer_product'


class Customer(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True)
    continuous = models.CharField(max_length=255, blank=True, null=True)
    cnt = models.CharField(max_length=20, blank=True, null=True)
    nid = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'customer'
        
        
class CosmeticProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    kind = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    pname = models.CharField(max_length=255)
    char = models.CharField(max_length=255, blank=True, null=True)
    price = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'cosmetic_product'
        
        
        
        
class CosmeticIngredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    pname = models.CharField(max_length=255)
    ingredient = models.TextField(blank=True, null=True)
    acne = models.TextField(blank=True, null=True)
    pchar = models.TextField(blank=True, null=True)
    dalton = models.TextField(blank=True, null=True)
    safeness = models.TextField(blank=True, null=True)
    stimulation = models.TextField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'cosmetic_ingredient'
        
        

# Create your models here.
