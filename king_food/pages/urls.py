from django.urls import path
from . import views


urlpatterns = [
        path ('',views.home ,name= 'home'),
        path ('shop/', views.shop_views,name='shop'),
        path ('about/',views.about_views ,name= 'about'),
        path ('contact/',views.contact_view ,name= 'contact'),
        path ('gg/',views.privacy_policy ,name= 'privacy'),

        path ('product/<int:id>/',views.product_views ,name= 'product'),
        path ('products/<int:id>/',views.product5_views ,name= 'products'),




]