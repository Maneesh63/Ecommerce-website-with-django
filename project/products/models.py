
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **add_more):

        email = self.normalize_email(email)

        user = self.model(email=email, username=username, **add_more)

        user.set_password(password)

        user.save(using=self._db)

        return user

#Determines whether Admin or not
    def create_superuser(self, email, username, password=None, **extra):
        
        extra.setdefault('is_staff', True)

        extra.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra)
                                


class CustomUser(AbstractBaseUser, PermissionsMixin):
   
    username = models.CharField(max_length=100,unique=False)
   
    email = models.EmailField(unique=True)
   
    is_active = models.BooleanField(default=True)
   
    is_staff = models.BooleanField(default=False)

    date=models.DateField(auto_now_add=True)

     
   
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



class Categories(models.Model):
      
    name=models.CharField(max_length=300,default='pots',null=True)

    def __str__(self) :
        return self.name

class Product(models.Model):

    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    name=models.CharField(max_length=255,blank=True)

    description=models.TextField(blank=True,null=True)

    image=models.ImageField(upload_to='images/', blank=True, null=True)

    orginal_price=models.DecimalField(max_digits=50,decimal_places=2)

    discounted_price=models.DecimalField(max_digits=50,decimal_places=2)

    date=models.DateField(auto_now_add=True)

    category=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True)
    
    update_at=models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self) :
        return self.name


class Cart(models.Model):

    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    quantity=models.PositiveIntegerField(default=0,null=True,blank=True)

    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    date=models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self) :
        return self.product.name + self.quantity



class Comment(models.Model):

   product=models.ForeignKey(Product,related_name='comments',on_delete=models.CASCADE)

   comment=models.CharField(max_length=1000,null=True,blank=True)

   date=models.DateField(auto_now_add=True)

   def __str__(self):
       return self.comment


class Address(models.Model):

    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    #product = models.ForeignKey(Product, on_delete=models.CASCADE)

    mobilenumber=models.CharField(max_length=15,default=9000,null=False,blank=False)

    address=models.CharField(max_length=2000,null=False,blank=False)

    pincode=models.CharField(max_length=100,null=False)

    state=models.CharField(max_length=300,null=False)

    city=models.CharField(max_length=500,null=False)

    date=models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.address


class Order(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)

    status = models.CharField(max_length=50, default='Pending')

class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    o_price = models.DecimalField(max_digits=10,default=10.00,decimal_places=2)

    d_price= models.DecimalField(max_digits=10, decimal_places=2)