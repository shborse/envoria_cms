from django.contrib import admin
from django.urls import path
from core.views import home_api   # 👈 IMPORTANT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/home/', home_api),   # 👈 THIS LINE FIXES EVERYTHING
]