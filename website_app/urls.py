from django.urls import path
from . import views

app_name = 'website_app'

urlpatterns = [
	path('', views.products, name="products"),
        path('order/', views.order, name="order"),
        path('sizetable/',views.size_table, name="size_table"),
        path('ordersuccess/', views.order_success, name="order_success"),
        path('1/', views.info_1, name="info_1"),
        path('2/', views.info_2, name="info_2"),
        path('3/', views.info_3, name="info_3"),
        path('4/', views.info_4, name="info_4"),
        path('5/', views.info_5, name="info_5"),
        path('6/', views.info_6, name="info_6"),
        path('7/', views.info_7, name="info_7"),
        path('8/', views.info_8, name="info_8"),
        path('9/', views.info_9, name="info_9"),
        path('10/', views.info_10, name="info_10"),
        path('11/', views.info_11, name="info_11"),
        path('12/', views.info_12, name="info_12"),
        path('order1/', views.order_1,name="order_1"),
        path('order2/', views.order_2,name="order_2"),
        path('order3/', views.order_3,name="order_3"),
        path('order4/', views.order_4,name="order_4"),
        path('order5/', views.order_5,name="order_5"),
        path('order6/', views.order_6,name="order_6"),
        path('order7/', views.order_7,name="order_7"),
        path('order8/', views.order_8,name="order_8"),
        path('order9/', views.order_9,name="order_9"),
        path('order10/', views.order_10,name="order_10"),
        path('order11/', views.order_11,name="order_11"),
        path('order12/', views.order_12,name="order_12"),
	]