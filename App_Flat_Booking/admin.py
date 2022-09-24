from django.contrib import admin
from App_Flat_Booking.models import Booking


class Booking_Admin(admin.ModelAdmin):
    list_display = ['renter', 'info_flat', 'created', ]
    # list_filter = ('status', 'created', 'publish', 'author')
    # search_fields = ('title', 'body')
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('renter',)
    # date_hierarchy = 'publish'
    # ordering = ('status', 'publish')

    class Meta:
        model = Booking


# Register your models here.
admin.site.register(Booking, Booking_Admin)

from .models import Cart, Order
# Register your models here.

admin.site.register(Cart)
admin.site.register(Order)