from django.contrib import admin
from django.urls import path
from adoption import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('form/', views.get_name, name='get-name'),
    path('adoptions/<int:pet_id>/', views.pet_detail, name='pet_detail'),
]
