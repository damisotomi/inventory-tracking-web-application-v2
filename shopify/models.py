from django.db import models
from django.urls import reverse
import uuid
from django.db.models import Sum    


# Create your models here.

class Group(models.Model):
    '''This model stores info about a product's group'''
    name=models.CharField('Group Name',max_length=200,help_text='Enter the product group name',unique=True)

    def __str__(self):
        """string for representing the Model Object(in admin site)"""
        return self.name

    def get_absolute_url(self):
        '''Returns the Url  to access a detail record for this product'''
        return reverse("group_detail", args=[str(self.id)])


class Warehouse(models.Model):
    '''This models stores info about a particular warehouse'''
    name =models.CharField(max_length=200, blank=False, null=False, help_text="Name of the warehouse",unique=True)
    location=models.CharField(max_length=200, blank=False, null=False, help_text="Location of warehouse")

    class Meta:
        ordering=['name']

    def __str__(self) -> str:
        ''' String for representing the model object in admin site'''
        return f'{self.name}'


    def get_absolute_url(self):
        '''Returns the Url  to access a detail record for this warehouse'''
        return reverse("warehouse_detail", kwargs={"pk": self.id})
    
    def totalquantity(self):
        totalquantity=0
        for warehouse in self.warehouse.all():
            totalquantity+=warehouse.quantity
        return totalquantity



class Product(models.Model):
    '''This model stores info about a product available by the logistics company'''
    name=models.CharField(max_length=50,blank=False,null=False,help_text="Enter name of product",unique=True)
    description=models.TextField(null=False,blank=False,max_length=1000,help_text="A short description of the product")
    code=models.UUIDField('Product code',primary_key=True, default=uuid.uuid4, help_text='Unique ID For this particular product across all warehouses/location')
    group=models.ForeignKey(Group,on_delete=models.SET_NULL,null=True,blank=True, related_name='group',help_text='Select a group (optional)')  

    class Meta:
        ordering=['name']

    def __str__(self) -> str:
        ''' String for representing the model object in admin site'''
        return f'{self.name}'

    def totalquantity(self):
        total=0
        for instance in self.product.all(): #note product is the related name here
            total+=instance.quantity
        return total

    def get_absolute_url(self):
        '''Returns the Url  to access a detail record for this product'''
        return reverse("product_detail", args=[str(self.code)])


class ProductInstance(models.Model):
    product=models.ForeignKey(Product,on_delete=models.RESTRICT,related_name='product')
    quantity=models.IntegerField(help_text="Enter number of bags")
    warehouse=models.ForeignKey(Warehouse,on_delete=models.RESTRICT,related_name='warehouse')
    price=models.DecimalField(max_digits=9,decimal_places=2,help_text="Price for 1 bag")

    def __str__(self) -> str:
        ''' String for representing the model object in admin site'''
        return  f'{self.product.name}'
       
    
    def total (self,quantity=quantity):
        return(self.objects.aggregate(Sum(quantity)))

    def get_absolute_url(self):
        '''Returns the Url  to access a detail record for this productinstance'''
        return reverse("product_instance_detail", args=[str(self.id)])

    class Meta:
        ordering=['-id']
