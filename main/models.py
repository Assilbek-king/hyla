from django.db import models
from datetime import datetime
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, blank=True)
    level = models.IntegerField(blank=True, default=0)
    info = models.TextField(blank=True, default=0)
    logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f'{self.title} --> {self.info} '


class Good(models.Model):
    title = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    level = models.IntegerField(blank=True, default=0)
    old_price = models.FloatField(default=0)
    price = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    mini_description = models.TextField(blank=True)
    # size = models.ForeignKey("Size", on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='upload', blank=True)
    logo2 = models.ImageField(upload_to='upload', blank=True)
    logo3 = models.ImageField(upload_to='upload', blank=True)
    logo4 = models.ImageField(upload_to='upload', blank=True)
    description = models.TextField(blank=True)
    dimensions = models.TextField(blank=True)
    materials = models.TextField(blank=True)
    extra_info = models.TextField(blank=True)
    is_new = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)
    stock = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.category} --> {self.title} '


class Cart(models.Model):
    last_name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    is_accepted = models.BooleanField(default=False)
    #is_payed = models.BooleanField(default=False)
    status = models.IntegerField(default=0)  # 0 - created zakaz, -1 - otmenen,  1 - confirmed, 2 - accepted
    session_id = models.CharField(max_length=200, blank=True)
    amount = models.FloatField(default=0)
    #discount = models.FloatField(default=0)
    orig_price = models.FloatField(default=0)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.session_id}  '


class CartItem(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    status = models.IntegerField(default=0)  # 0 - created, -1 - deleted
    all_price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.cart.id}   {self.good.title}  {self.amount}'


class WishItem(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)  # 0 - created zakaz, -1 - otmeneen,  1 - confirmed, 2 - accepted

    def __str__(self):
        return f'{self.session_id} {self.good.title}'



class Message(models.Model):
    name = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=300, blank=True)
    message = models.TextField(max_length=300, blank=True)


    def __str__(self):
        return f'{self.name} --> {self.phone} --> {self.message}'



class Contact(models.Model):
    addres = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=300, blank=True)


    def __str__(self):
        return f'{self.addres}'


class Blog(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    mini_description = models.TextField(max_length=500, blank=True)
    description = models.TextField(max_length=300, blank=True)
    date = models.DateField(default=datetime.now())
    author = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.title} '

class Service(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    mini_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.title} '

class About(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    logo1 = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f'{self.title}  '


class Member(models.Model):
    name = models.CharField(max_length=300, blank=True)
    last_name = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    doljnost = models.CharField(max_length=300, blank=True)
    facebook_link = models.CharField(max_length=300, blank=True)
    instagram_link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.name} {self.last_name} '


class Info(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f'{self.title}  '


class Nagrada(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(default=datetime.now())

    def __str__(self):
        return f'{self.title} '