from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = "about"),
    path('orders/', views.orders, name = "orders"),
    path('orderlist/', views.orderlist, name = "orderlist"),
    path('update_order/<str:pk>', views.update_order, name = "update_order"),  
    # path('show_category/<str:pk>', views.show_category, name = "show_category"),
    path('order_details/<str:pk>', views.show_order, name = "order_details"), 
]