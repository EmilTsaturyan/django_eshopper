from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_request, name='login'),
    path('register/',views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:id>', views.product_detail, name='product_detail')
]

