from django.urls import path

from . import views

app_name = 'api_profile'
urlpatterns = [
    path('customers/', views.CustomerListApiView.as_view(), name='customer_list'),
    path('customer-signup/', views.CustomerCreateApiView.as_view(), name='customer_signup'),
    path('customer/<int:pk>/', views.CustomerDetailApiView.as_view(), name='customer_detail'),
    path('customer/<int:pk>/update/', views.CustomerUpdateApiView.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete/', views.CustomerDestroyApiView.as_view(), name='customer_destroy'),

    path('drivers/', views.DriverListApiView.as_view(), name='driver_list'),
    path('driver-signup/', views.DriverCreateApiView.as_view(), name='driver_signup'),
    path('driver/<int:pk>/', views.DriverDetailApiView.as_view(), name='driver_detail'),
    path('driver/<int:pk>/update/', views.DriverUpdateApiView.as_view(), name='driver_update'),
    path('driver/<int:pk>/delete/', views.DriverDestroyApiView.as_view(), name='driver_destroy'),
]