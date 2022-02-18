from random import choices
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

def UserImages(instance, filename):
    return '/'.join( ['images', 'Users', str(instance.id), filename] )

def CategoryImages(instance, filename):
    return '/'.join( ['images', 'Categories', str(instance.id), filename] )

def ProductImages(instance, filename):
    return '/'.join( ['images', 'Products', str(instance.id), filename] )

def WishListImages(instance, filename):
    return '/'.join( ['images', 'WishLists', str(instance.wishID), filename] )

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password = None):
        
        if email is None:
            raise TypeError('Users should have an Email.')

        user = self.model(username = username, email = email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password = None):

        if password is None:
            raise TypeError('Password has not been typed')

        user = self.create_user(username, email, password)
        #user = self.model(username = username, email = self.normalize_email(email))
        user.is_superuser = True 
        user.is_staff = True
        user.save()
        return user

class Users(AbstractBaseUser, PermissionsMixin):

    OPTIONS = (('Male','Male'), ('Female', 'Female'), ('Other', 'Other')) 

    id = models.AutoField(primary_key = True, unique=True, blank=False, null=False, db_index=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    contactNo = models.CharField(max_length=100, blank=True, null=True)
    favourites = models.ManyToManyField('Products')
    image = models.ImageField(upload_to=UserImages, max_length = 255, blank = True, null = True)
    gender = models.CharField(max_length=100, choices = OPTIONS, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

class UserLogs(models.Model):
    logID = models.AutoField(primary_key = True, unique=True, blank=False, null=False)
    userID = models.ForeignKey(Users, on_delete = models.CASCADE, null = False, blank = False)
    LoginDateTime = models.DateTimeField(auto_now_add=True)
    logoutDateTime = models.DateTimeField(auto_now=True, blank=True, null=True)

class ProductCategories(models.Model):
    id = models.AutoField(primary_key = True, unique=True, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to=CategoryImages, max_length = 255, blank = True, null = True)

    def __str__(self):
        return self.title

class Products(models.Model):
    id = models.AutoField(primary_key = True, unique=True, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    category = models.ForeignKey(ProductCategories, on_delete = models.CASCADE, null=True, blank=True)
    price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    sold_qt = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add = True, blank=False, null=False)
    updated_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=ProductImages, max_length = 255, blank = True, null = True)
    
    def __str__(self):
        return self.title

class UserOrders(models.Model):

    OPTIONS = (('Cash on Delivery','Cash on Delivery'), 
               ('Credit/Debit Card', 'Credit/Debit Card'))

    orderID = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    userID = models.ForeignKey(Users, on_delete = models.CASCADE, null = False, blank = False)
    products = models.ManyToManyField(Products)
    paymentMethod = models.CharField(max_length=100, choices = OPTIONS)

    @property
    def total_price(self):
        queryset = self.productID.all().aggregate(
            total_price=models.Sum('price'))
        return queryset["total_price"]

class UserWishList(models.Model):
    wishID = models.AutoField(primary_key = True, unique=True, blank=False, null=False)
    user = models.ForeignKey(Users, on_delete = models.CASCADE, null = False, blank = False)
    title = models.CharField(max_length=100, blank=True, null=True)
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    productURL = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class UserAddress(models.Model):
    houseID = models.AutoField(primary_key = True, unique=True, blank=False, null=False)
    userID = models.ForeignKey(Users, on_delete = models.CASCADE, null = False, blank = False)
    address = models.TextField(blank=False, null=False)
    houseDescription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.userID

# class UserPayingCards(models.Model):
#     card_no = models.CharField(primary_key=True, max_length=19, blank=False, null=False)
#     owner_id = models.ForeignKey(Users, on_delete = models.CASCADE, null = False, blank = False)
#     is_verified = models.BooleanField(default=False)
#     holderName = models.CharField(max_length=50, blank=False, null=False)
#     expDate = models.

#     def __str__(self):
#         return self.holderName