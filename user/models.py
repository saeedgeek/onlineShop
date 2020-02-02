from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class Profile(User):
    image = models.ImageField(upload_to='images/', null=True)
    phone_regex=r'^\d{10}$'
    phone_regex = RegexValidator(regex=phone_regex, message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10,null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    gender = models.CharField(null=True,max_length=1, choices=GENDER_CHOICES)
