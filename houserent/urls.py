from django.urls import path
from . import views



urlpatterns = [
    path('', views.city_list, name='city_list'),
    path('houses/', views.house_list, name='house_list'),
    path('cities/<int:pk>', views.city_detail, name='city_detail'),
    path('house/<int:pk>', views.house_detail, name='house_detail'),
    path('city/new', views.city_create, name='city_create'),
    path('house/new', views.house_create, name='house_create'),
    path('city/<int:pk>/edit', views.city_edit, name='city_edit'),
    path('house/<int:pk>/edit', views.house_edit, name='house_edit'),
    path('city/<int:pk>/delete', views.city_delete, name='city_delete'),
    path('house/<int:pk>/delete', views.house_delete, name='house_delete')
] 