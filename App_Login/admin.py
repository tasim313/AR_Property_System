from django.contrib import admin
from App_Login.models import user_registration, CreateUser

class User_registration_Admin(admin.ModelAdmin):
    list_display = ['user', 'Full_name', 'User_email', 'User_phone', 'User_image', 'Address']

    class Meta:
        model = user_registration


# Register your models here.
admin.site.register(user_registration, User_registration_Admin)
admin.site.register(CreateUser)
