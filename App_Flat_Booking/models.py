from django.db import models
from App_Login.models import user_registration
from App_Add_Flat.models import Add_Flat
from App_Login.models import CreateUser

# Create your models here.


class Booking(models.Model):
    renter = models.ForeignKey(CreateUser, related_name='renter_info', on_delete=models.CASCADE)
    info_flat = models.ForeignKey(Add_Flat, related_name='flat_info', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    booked = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)

    # def __str__(self):
    #     return self.renter

    def get_cost(self):
        return self.info_flat.House_rent + self.info_flat.Utility_bill

# Flat add to cart


class Cart(models.Model):
    user = models.ForeignKey(CreateUser, on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Add_Flat, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} X {self.item}'

    def get_total(self):
        total = self.item.House_rent + self.item.Utility_bill
        float_total = format(total, '0.2f')
        return float_total


class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(CreateUser, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=264, blank=True, null=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total