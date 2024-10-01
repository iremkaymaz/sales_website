from django.urls import path
from . import views

app_name = 'website_app'

urlpatterns = [
	path('', views.products, name="products"),
        path('ordersuccess/', views.order_success, name="order_success"),
        path('1/', views.info_1, name="info_1"),
        path('2/', views.info_2, name="info_2"),
        path('3/', views.info_3, name="info_3"),
        path('4/', views.info_4, name="info_4"),
        path('order1/', views.order_1,name="order_1"),
        path('order2/', views.order_2,name="order_2"),
        path('order3/', views.order_3,name="order_3"),
        path('order4/', views.order_4,name="order_4"),
	]