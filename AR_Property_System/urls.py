from django.contrib import admin
from django.urls import path, include
from App_Add_Flat import views

# Media file display
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_Login.urls')),
    path('flat/', include('App_Add_Flat.urls')),
    path('about/', include('App_About.urls')),
    path('flat_booking/', include('App_Flat_Booking.urls')),
    path('payment/', include('App_Payment.urls')),
    path('feedback/', include('App_Feedback.urls')),
    path('', views.Home.as_view(), name='home'),
    path(r'^auth/', include('djoser.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
