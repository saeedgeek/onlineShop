from django.db import models
from user.models import Profile 
class Category(models.Model):
    image=models.ImageField(upload_to='images/',null=True)
    top_category=models.ForeignKey('self',on_delete=None,null=True,blank=True)
    category_name=models.CharField(max_length=200)
    def __str__(self):
        return str(self.category_name)

class Product(models.Model):
    image=models.ImageField(upload_to='images/',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    name=models.CharField(max_length=200)
    weight=models.SmallIntegerField()
    choise=[
        ('rd','red'),
        ('gl','gold',),
        ('bk','black'),
        ('wt','white'),
        ('gn','green'),
        ('pr','purple'),


    ]
    color=models.CharField(max_length=200,choices=choise)
    price=models.IntegerField()
    def __str__(self):
        return str(self.name)


class Cart(models.Model):
    product=models.ManyToManyField(Product,through='Product_Cart')
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user.username)

class Product_Cart(models.Model):
    prdc=models.ForeignKey(Product,on_delete=models.CASCADE)
    crt=models.ForeignKey(Cart,on_delete=models.CASCADE)
    count=models.SmallIntegerField()
    def __str__(self):
        return str(self.prdc.name+" -----> "+self.crt.user.username)


class laptop(Product):
    choise=[
        ('mc','mac'),
        ('ln','linux',),
        ('wn','windows'),
    

    ]
    cpu=models.CharField(max_length=50)    
    ram=models.CharField(max_length=50)    
    hard=models.CharField(max_length=50)    
    os=models.CharField(max_length=50)
    

class mobile(Product):
    choise=[
        ('an','android'),
        ('is','ios',),
        ('wp','windows phone'),
    

    ]
    cpu=models.CharField(max_length=50)    
    ram=models.CharField(max_length=50)    
    hard=models.CharField(max_length=50)    
    os=models.CharField(max_length=50,choices=choise)
        

        