from django.db import models
from App_Login.models import CreateUser
from App_Add_Flat.models import Add_Flat
from django.db.models.signals import post_save
# Create your models here.


class BillingInfo(models.Model):
    Bank = 1
    CreditCard = 2
    Bkash = 3
    Nagad = 4
    billing_user = models.ForeignKey(
        CreateUser, on_delete=models.CASCADE, related_name="billing_user")
    flat = models.ForeignKey(Add_Flat, on_delete=models.CASCADE, related_name="billing_flat")
    billing_date = models.DateField(auto_now_add=True)
    billing_time = models.TimeField(auto_now_add=True)
    payment_method_choise = [
        (Bank, 'Bank'),
        (CreditCard, 'Credit Card'),
        (Bkash, 'Bkash'),
        (Nagad, 'Nagad')
    ]
    payment_method = models.CharField(
        max_length=20, choices=payment_method_choise)
    billing_amount = models.IntegerField()

    billing_status_choise = [
        ('Pending', 'Pending'),
        ('UnPaid', 'UnPaid'),
        ('Paid', 'Paid'),
    ]
    billing_status = models.CharField(
        max_length=20, choices=billing_status_choise, default=Pending)

    def __str__(self):
        return self.billing_user.username

    def get_total(self):
        total = self.flat.House_rent + self.flat.Utility_bill
        float_total = format(total, '0.2f')
        return float_total


class BankInfo(models.Model):

    bank_info_user = models.ForeignKey(
        CreateUser, on_delete=models.CASCADE, related_name='bank_info_user')
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account_number = models.CharField(
        max_length=255, blank=True, null=True)
    bank_swift_code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.bank_info_user.username


def create_bank_info(sender, instance, created, **kwargs):

        if created:
            bank_info = BillingInfo.objects.get(id=instance.id)
            print('test', bank_info)

            if bank_info.payment_method_choise == 1:
                BankInfo.objects.create(bank_info_user=instance)
                print(
                    f'sender:{sender}, instance-{instance}, created-{created}, kw-{kwargs}')


post_save.connect(create_bank_info, sender=CreateUser)


class CreditCardInfo(models.Model):

    credit_card_info_user = models.ForeignKey(
        CreateUser, on_delete=models.CASCADE, related_name='card_info_user')
    credit_card_name = models.CharField(max_length=255, blank=True, null=True)
    credit_card_number = models.CharField(
        max_length=255, blank=True, null=True)
    credit_card_expire_date = models.CharField(
        max_length=255, blank=True, null=True)
    cvv_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.credit_card_info_user.username


def create_credit_card_info(sender, instance, created, **kwargs):

        if created:
            credit_card_info = BillingInfo.objects.get(id=instance.id)
            print('test', bank_info)

            if credit_card_info.payment_method_choise == 2:
                BankInfo.objects.create(card_info_user=instance)
                print(
                    f'sender:{sender}, instance-{instance}, created-{created}, kw-{kwargs}')


post_save.connect(create_credit_card_info, sender=CreateUser)

