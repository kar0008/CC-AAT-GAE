from django.contrib import admin
from django.urls import path

from demo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.demo),
]