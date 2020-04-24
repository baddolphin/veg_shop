from django.urls import path
from . import views
from vegan_app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:page_id>', ShopView.as_view()),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('product-single/', ProductSingleView.as_view(), name='product-single'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
]
