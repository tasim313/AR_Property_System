from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=400, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Add_Flat(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    Flat_image = models.ImageField(blank=True, null=True, upload_to='flat_pics')
    House_name = models.CharField(max_length=250, blank=True, null=True)
    Floor = models.IntegerField(blank=True, null=True)
    Flat_number = models.CharField(max_length=50, blank=True, null=True)
    Square_feet = models.FloatField(blank=True, null=True)
    Bedroom = models.IntegerField(blank=True, null=True)
    Guest_room = models.IntegerField(blank=True, null=True)
    Number_of_bath = models.IntegerField(blank=True, null=True)
    Number_of_balcony = models.IntegerField(blank=True, null=True)
    House_rent = models.FloatField(blank=True, null=True)
    Utility_bill = models.FloatField(blank=True, null=True)
    Address = models.TextField(blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.House_name + str(self.Flat_number)

    class Meta:
        ordering = ['-Created_at']




class Update_Rent(models.Model):
    House_rent = models.FloatField(blank=True, null=True)
    Utility_bill = models.FloatField(blank=True, null=True)


class Notification(models.Model):
    pass
