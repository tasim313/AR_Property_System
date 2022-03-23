from django.contrib import admin
from App_Add_Flat.models import Category, Add_Flat, Update_Rent, Notification
class Add_Flat_Admin(admin.ModelAdmin):
    list_display = ['Category', 'House_name', 'Flat_image', 'Floor', 'Flat_number', 'Square_feet', 'Bedroom', 'Guest_room',
                    'Number_of_bath', 'Number_of_balcony', 'House_rent', 'Utility_bill', 'Address', 'Created_at', 'Updated_at']
    class Meta:
        model = Add_Flat

class Update_rent_Admin(admin.ModelAdmin):
    list_display = ['House_rent', 'Utility_bill']

    class Meta:
        model = Update_Rent
class Catagory_Admin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

    class Meta:
        model = Category

# Register your models here.
admin.site.register(Category, Catagory_Admin)
admin.site.register(Add_Flat, Add_Flat_Admin)
admin.site.register(Update_Rent, Update_rent_Admin)
admin.site.register(Notification)
