from django.db import models
from datetime import datetime

class product(models.Model):

    name = models.CharField(unique=True,max_length=100)
    activate = models.BooleanField(default=True)
    description = models.TextField()
    photo =   models.ImageField(upload_to='photos/' )
    weight = models.CharField(max_length=150 , null=True , blank=True)
    def __str__(self):
        return self.name
    

class container_of_five_product (models.Model):

    name = models.CharField(unique=True,max_length=100)
    activate = models.BooleanField(default=True)
    description = models.TextField()
    photo1 =   models.ImageField(upload_to='photos/' )
    photo2 =   models.ImageField(upload_to='photos/' )
    photo3 =   models.ImageField(upload_to='photos/' )
    photo4 =   models.ImageField(upload_to='photos/' )
    photo5 =   models.ImageField(upload_to='photos/' )
    weight = models.CharField(max_length=150 , null=True , blank=True)
    def __str__(self):
        return self.name    
    
class about_company(models.Model):
    Name = models.CharField(max_length=200)
    phone_number1 = models.CharField(max_length=15 ,unique=True)
    phone_number2 = models.CharField(unique=True ,null=True, blank=True , max_length=15)
    address = models.CharField(max_length=600 ,default='فاطمة الزهراء, قرية، ونا القس، محافظة بني سويف')
    logo = models.ImageField(upload_to='photos/')
    gmail = models.CharField(unique=True ,null=True, blank=True , max_length=250)
    Tiktok = models.CharField(unique=True ,null=True, blank=True , max_length=250)
    Facebook =  models.CharField(unique=True ,null=True, blank=True , max_length=250)
    instagram =  models.CharField(unique=True ,null=True, blank=True , max_length=250)
    video = models.FileField (upload_to='video/')

    def __str__(self):
        return self.Name
    
    
class Certificates(models.Model):
    photo1 =   models.ImageField(upload_to='photos/' ) 
    date_added = models.DateTimeField(auto_now_add=True)
    Description =models.CharField(max_length=100)
    class Meta:
        ordering = ['-date_added'] 




class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.TextField(max_length=700)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    



class quality(models.Model):
    Description = models.TextField()
    photo = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date_added'] 
    
