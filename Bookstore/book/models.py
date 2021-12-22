from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=50)
    price=models.PositiveIntegerField(default=20)
    copies=models.PositiveIntegerField(default=1)
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.book_name

class Cart(models.Model):
    item=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(("incart","incart"),
    ("cancelled","cancelled"),
    ("orderplaced","orderplaced"))
    status=models.CharField(max_length=30,choices=options,default="incart")


class Orders(models.Model):
    item=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.CharField(max_length=40)
    address=models.CharField(max_length=120)
    date_order=models.DateField(auto_now_add=True)
    options=(
        ("orderplaced","orderplaced"),
        ("dispatch","dispatch"),
        ("intransit","intransit"),
        ("delivered","delivered"),
        ("order_cancelled","order_cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="orderplaced")
    expected_delivery_date=models.DateField(null=True,blank=True)

# class WhishList(models.Model):
#     wishitem=models.ForeignKey(Book,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE) 