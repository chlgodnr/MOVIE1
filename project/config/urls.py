from django.contrib import admin
from django.urls import path, include
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', views.index),
    path('movie/', include('movie.urls')),
]
