
from email.policy import default
from itertools import product
from django.db import models
from product.models import Product
from accounts.models import Account

# Create your models here.
class Cart(models.Model):

    cart_id = models.CharField(max_length = 200, blank = True)
    date_added = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):

    user = models.ForeignKey(Account, on_delete = models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null = True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)


    def sub_total(self):
         return self.product.price * self.quantity   

    def offer_total(self):
        return self.product.offer * self.quantity     



    def __str__(self):
        return str(self.product)





class WishListItem(models.Model):

    user = models.ForeignKey(Account, on_delete = models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    is_active = models.BooleanField(default=True)        


    def __str__(self):
        return str(self.product)