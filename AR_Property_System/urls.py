from django.contrib import admin
from django.urls import path, include
from App_Login import views
# Media file display
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_Login.urls')),
    path('flat/', include('App_Add_Flat.urls')),
    path('', views.home, name='home')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
