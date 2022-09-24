from django.contrib import admin
from App_Login.models import user_registration, CreateUser


class User_registration_Admin(admin.ModelAdmin):
    list_display = ['user', 'Full_name', 'User_email', 'User_phone', 'User_image', 'Address']
    list_filter = ('user', 'User_phone',  'Full_name', 'User_email', )
    search_fields = ('User_phone',  'Full_name', 'User_email',)
    raw_id_fields = ('user',)
    ordering = ('id',)
    class Meta:
        model = user_registration


# Register your models here.
admin.site.register(user_registration, User_registration_Admin)
admin.site.register(CreateUser)
