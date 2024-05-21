from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import Role

# class Test(models.Model):

#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     age = models.IntegerField()
    
    

# class Test2(models.Model):

#     nam2 = models.CharField(max_length=255)
#     surname2 = models.CharField(max_length=255)
#     age2 = models.IntegerField()

class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)  
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, default="")
    user_type = models.CharField(max_length=10, choices=Role.choices, default=Role.CUSTOMER)
    
    name_object = models.CharField(max_length=255, null=True, default="")
    bin = models.CharField(max_length=255, null=True, default="")
    legal_address = models.CharField(max_length=255, null=True, default="")
    telephone = models.CharField(max_length=255, null=True, default="")
    file = models.FileField(upload_to='users/', default=None, null=True)
    contact_number = models.CharField(max_length=255, null=True, default="")
    date_contract_conclusion = models.DateTimeField(null=True,  default=None)
    contract_validity_period = models.DateTimeField(null=True,  default=None)
    financial_conditions = models.CharField(max_length=255,  null=True, default="")
    name_of_supervisor = models.CharField(max_length=255,  null=True, default="")
    
    fullname = models.CharField(max_length=255, null=True,  default="")
    name_of_group = models.CharField(max_length=255,  null=True, default="")
    tin = models.CharField(max_length=255,  null=True, default="")
    residential_address = models.CharField(max_length=255,  null=True, default="")
    name_of_bank = models.CharField(max_length=255,  null=True, default="")
    iban = models.CharField(max_length=255,  null=True, default="")
    iin = models.CharField(max_length=255,  null=True, default="")
    by_whom_issued = models.CharField(max_length=255,  null=True, default="")
    expiration_date_id_card = models.DateTimeField(null=True,  default=None)
    
    USERNAME_FIELD = 'username'

class Request(models.Model):
    CATEGORY_CHOICES = [
        ('accounting', 'Бухгалтерия'),
        ('other', 'Прочее'),
        ('agreement', 'Договор'),
    ]

    email = models.EmailField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='accounting')
    subject = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    
# class CustomPermission(models.Model):
#     user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     user_type = models.CharField(max_length=10, choices=Role.choices, default=Role.CUSTOMER)
    