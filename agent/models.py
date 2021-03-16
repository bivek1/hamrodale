from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):
    user_type_data = ((1, 'Admin'), (2, 'Customer'))
    email = models.EmailField(unique=True)
    user_type = models.CharField(default = 1, choices = user_type_data, max_length = 10)
    
class AdminOwner(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Customer(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = "user_Profile", blank = True)
    address = models.CharField(max_length = 200)
    number = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True) 
    objects = models.Manager()

class advertise(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    ads_created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length = 400, blank = False, default= 'Property In Sell')
    district = models.CharField(max_length = 100, choices = (
        ('Kathmandu','Kathmandu'),
        ('Bhaktapur','Bhaktapur'),
        ('Lalitpur','Lalitpur'),
        ('Makwanpur','Makwanpur'),
        ('Chitwan','Chitwan'),
        ('Dhading','Dhading'),
        ('Dhankuta','Dhankuta'),
        ('Gorkha','Gorkha'),
        ('Jhapa','Jhapa'),
        ('Kaski','Kaski'),
        ('Kavrepalanchok','Kavrepalanchok'),
        ('Sindhupalchok','Sindhupalchok'),
        ('Solukhumbu','Solukhumbu'),
        ('Surkhet','Surkhet'),
        ('Taplejung','Taplejung'),
        ('Other','Other'),
        ), default = 'Kathmandu')
    woda = models.IntegerField(blank = False, default = 1)
    location = models.CharField(max_length = 400, blank = False)
    price = models.BigIntegerField(blank = False)
    price_in_words = models.CharField(max_length = 400)
    selling_in = models.CharField(max_length = 50, choices =(
        ('Fixed', 'Fixed Price'),
        ('Bargainable', 'Bragainable')
    ), default =  'Bargainable')
    images = models.ImageField(blank=True)
    premium = models.CharField(max_length = 20, choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    ), default = 'No')
    feature =  models.CharField(max_length = 20, choices = (
        ('Yes', 'Yes'),
        ('No', 'No')
    ), default = 'No')
    description = models.CharField(max_length = 5000, blank = True)
    objects = models.Manager()
    def __str__(self):
        return self.title
    
class ImagesAd(models.Model):
    post = models.ForeignKey(advertise, default=None, on_delete=models.CASCADE)
    image = models.FileField(max_length = 255)
    
class house(models.Model):

    objectname = models.OneToOneField(advertise, on_delete=models.CASCADE, null = True, related_name = "house")
    landsize = models.CharField(max_length = 300)
    road_size = models.CharField(max_length = 200)
    floor = models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    kitchen = models.IntegerField()
    face_toward = models.CharField(max_length = 200, blank = True, choices = (
        ('East', 'East'),
        ('West', 'West'),
        ('North', 'North'),
        ('South', 'South')
    ), default = 'East')
    garden = models.CharField(max_length = 200, choices= (
    ('Yes', 'YES'),
    ('No', 'No')
    ), default = 'Yes')
    garage = models.CharField(max_length = 200, choices= (
    ('Yes', 'YES'),
    ('No', 'No')
    ), default = 'Yes')
    undergroudTank = models.CharField(max_length = 200, choices= (
    ('Yes', 'YES'),
    ('No', 'No')
    ), default = 'Yes')
    objects = models.Manager()
    def __str__(self):
        return self.objectname.location

class rent(models.Model):
    objectname = models.OneToOneField(advertise, on_delete=models.CASCADE, null = True, related_name = "rent")
    rentroom = models.IntegerField()
    bathroom = models.IntegerField()
    internet = models.CharField(max_length = 200, choices = (
        ('YES', 'YES'),
        ('NO', 'NO')
    ), default = 'YES')
    garage = models.CharField(max_length = 200, choices = (
        ('YES', 'YES'),
        ('NO', 'NO')
    ), default = 'YES')
    tvchannel = models.CharField(max_length = 200, choices = (
        ('YES', 'YES'),
        ('NO', 'NO')
    ), default = 'YES')
    objects = models.Manager()
    def __str__(self):
        return self.objectname.location
    
class land(models.Model):
    objectname = models.OneToOneField(advertise, on_delete=models.CASCADE, null = True, related_name = "land")
    landsize = models.CharField(max_length = 200)
    road_size = models.CharField(max_length = 200)
    electrivityline = models.CharField(max_length = 200, choices = (
        ('YES', 'YES'),
        ('NO', 'NO')
    ), default = 'YES')
    plotting = models.CharField(max_length = 200, choices = (
        ('YES', 'YES'),
        ('NO', 'NO')
    ), default = 'YES')
    objects = models.Manager()
    def __str__(self):
        return self.objectname.location
    
class business(models.Model):
    objectname = models.OneToOneField(advertise, on_delete=models.CASCADE, null = True, related_name="business")
    businesstype = models.CharField(max_length = 200, blank = False)
    objects = models.Manager()
    def __str__(self):
        return self.objectname.location
    
class requestBuy(models.Model):
    req_ads = models.ForeignKey(advertise, on_delete=models.CASCADE, related_name='buyrequest')
    req_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    created_date = models.DateTimeField(default=timezone.now)
    dealed = models.CharField(max_length = 20, choices = (
        ('Yes','Yes'),
        ('No','No'),
    ), default = 'No')
    
class comment(models.Model):
    comment_ads = models.ForeignKey(advertise, on_delete=models.CASCADE, related_name='comment')
    comment_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    body = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    unread = models.BooleanField(default=True)
    ureadCustomer = models.BooleanField(default=True)

@receiver(post_save, sender= CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminOwner.objects.create(admin = instance)
        if instance.user_type == 2:
            Customer.objects.create(admin = instance)
            
@receiver(post_save, sender= CustomUser)
def _post_save_receiver(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminowner.save()
    if instance.user_type == 2:
        instance.customer.save()