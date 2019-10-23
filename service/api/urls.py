from django.urls import path

from . import views

app_name = 'service_api'
urlpatterns = [
    path('orders/', views.PemesananListApiView.as_view(), name='order_list'),
    path('create-order/', views.PemesananCreateApiView.as_view(), name='create_order'),
    path('order/<int:pk>/', views.PemesananDetailApiView.as_view(), name='order_detail'),
    path('order/<int:pk>/update/', views.PemesananUpdateApiView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', views.PemesananDestroyApiView.as_view(), name='destroy_order'),
]