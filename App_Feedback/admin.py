from django.contrib import admin
from App_Feedback.models import Feedback, Replay_Feedback

# Register your models here.


class FlatAdmin(admin.ModelAdmin):
    list_display = ['user', 'house_name', 'flat_number']


admin.site.register(Feedback, FlatAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['feedback', 'replay_feedback', 'created']


admin.site.register(Replay_Feedback, ReplyAdmin)
