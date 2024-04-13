from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class users(models.Model):
    username=models.CharField(max_length=30)
    number=models.IntegerField(max_length=10)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)
    last_login=models.DateTimeField(max_length=10)

    class Meta:
        db_table = 'users'


class admins(models.Model):
    username=models.CharField(max_length=30)
    number=models.IntegerField(max_length=10)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)
    last_login=models.DateTimeField(max_length=10)

    class Meta:
        db_table = 'admins'

class message(models.Model):
    user_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    message=models.TextField(max_length=100)

    class Meta:
        db_table = 'message'


class trianer(models.Model):
    name=models.CharField(max_length=30)
    number=models.IntegerField(max_length=10)
    email=models.EmailField(max_length=30)

    class Meta:
        db_table = 'trianer'

class product(models.Model):
    name=models.CharField(max_length=30)
    # company_name=models.CharField(max_length=30)
    price=models.IntegerField(max_length=10)
    quantity=models.TextField(max_length=30)
    description=models.TextField(max_length=50)

    class Meta:
        db_table = 'product'

class membership(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(max_length=10)
    total_day=models.TextField(max_length=30)

    class Meta:
        db_table = 'membership'

class yoga_class(models.Model):
    yoga_trainer_name=models.CharField(max_length=30)
    price=models.IntegerField(max_length=10)
    total_day=models.TextField(max_length=30)
    time=models.TextField(max_length=30)


    class Meta:
        db_table = 'yoga_class'


class membership_holders(models.Model):
    membership_type=models.CharField(max_length=30)
    membership_price=models.IntegerField(max_length=30)
    membership_total_day=models.CharField(max_length=30)
    user_name=models.CharField(max_length=10)
    user_email=models.EmailField(max_length=30)


    class Meta:
        db_table = 'membership_holders'


class yoga_class_member(models.Model):
    trainer_name=models.CharField(max_length=30)
    class_price=models.IntegerField(max_length=30)
    total_day=models.CharField(max_length=30)
    class_time=models.CharField(max_length=10)
    user_name=models.CharField(max_length=30)
    user_email=models.EmailField(max_length=30)

    class Meta:
        db_table = 'yoga_class_member'



class userorder(models.Model):
    product_id=models.CharField(max_length=30)
    product_name=models.CharField(max_length=30)
    product_price=models.IntegerField(max_length=30)
    product_quantity=models.CharField(max_length=30)
    user_name=models.CharField(max_length=10)
    user_email=models.CharField(max_length=30)
    user_address=models.CharField(max_length=100)

    class Meta:
        db_table = 'userorder'


class cart(models.Model):
    product_id=models.CharField(max_length=30)
    product_name=models.CharField(max_length=30)
    product_price=models.IntegerField(max_length=30)
    product_quantity=models.CharField(max_length=30)

    class Meta:
        db_table = 'cart'