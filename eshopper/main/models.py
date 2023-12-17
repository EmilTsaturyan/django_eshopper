from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):

    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=50)
    message = models.TextField('Message')

    def __str__(self) -> str:
        return self.email
    

class Product(models.Model):

    TYPE_CHOICE = (
        ('T-SHIRT', 'T-SHIRT'),
        ('BLAZERS', 'BLAZERS'),
        ('SUNGLASS', 'SUNGLASS'),
        ('KIDS', 'KIDS'),
        ('POLO SHIRT', 'POLO SHIRT'),
    )

    name = models.CharField('Name', max_length=50)
    image = models.ImageField('Image')
    web_id = models.PositiveIntegerField('Web ID')
    price = models.PositiveIntegerField('Price')
    type = models.CharField('Type', choices=TYPE_CHOICE, max_length=30)


    def __str__(self) -> str:
        return self.name


class Cart(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantity', default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    

