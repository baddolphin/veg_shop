from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.core.paginator import Paginator
from .settings.base import *


class IndexView(View):

    def get(self, request):
        return render(request, 'vegan_app/index.html', {'phone_number': PHONE_NUMBER,
                                                        'email': EMAIL,
                                                        'meat': MEAT,
                                                        'far_far': FAR_FAR,
                                                        'post_info': POST_INFO,
                                                        'phone_info': PHONE_INFO,
                                                        'email_info': EMAIL_INFO,
                                                        })


class WishlistView(View):

    def get(self, request):
        return render(request, 'vegan_app/wishlist.html', {'phone_number': PHONE_NUMBER,
                                                           'email': EMAIL,
                                                           'meat': MEAT,
                                                           'far_far': FAR_FAR,
                                                           'post_info': POST_INFO,
                                                           'phone_info': PHONE_INFO,
                                                           'email_info': EMAIL_INFO,
                                                           })


class ProductSingleView(View):

    def get(self, request):
        return render(request, 'vegan_app/product-single.html', {'phone_number': PHONE_NUMBER,
                                                                 'email': EMAIL,
                                                                 'meat': MEAT,
                                                                 'far_far': FAR_FAR,
                                                                 'post_info': POST_INFO,
                                                                 'phone_info': PHONE_INFO,
                                                                 'email_info': EMAIL_INFO,
                                                                 })


class CheckoutView(View):

    def get(self, request):
        return render(request, 'vegan_app/checkout.html', {'phone_number': PHONE_NUMBER,
                                                           'email': EMAIL,
                                                           'meat': MEAT,
                                                           'far_far': FAR_FAR,
                                                           'post_info': POST_INFO,
                                                           'phone_info': PHONE_INFO,
                                                           'email_info': EMAIL_INFO,
                                                           })


class AboutView(View):

    def get(self, request):
        return render(request, 'vegan_app/about.html', {'phone_number': PHONE_NUMBER,
                                                        'email': EMAIL,
                                                        'meat': MEAT,
                                                        'far_far': FAR_FAR,
                                                        'post_info': POST_INFO,
                                                        'phone_info': PHONE_INFO,
                                                        'email_info': EMAIL_INFO,
                                                        })


class BlogView(View):

    def get(self, request):
        blogs = [
            {'image': '/static/vegan_app/images/image_1.jpg',
             'date': 'July 20, 2019',
             'name': 'Admin',
             'comment': '3',
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'body': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
            {'image': '/static/vegan_app/images/image_2.jpg',
             'date': 'July 20, 2019',
             'name': 'Admin',
             'comment': '3',
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'body': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
            {'image': '/static/vegan_app/images/image_3.jpg',
             'date': 'July 20, 2019',
             'name': 'Admin',
             'comment': '3',
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'body': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
            {'image': '/static/vegan_app/images/image_4.jpg',
             'date': 'July 20, 2019',
             'name': 'Admin',
             'comment': '3',
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'body': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
            {'image': '/static/vegan_app/images/image_5.jpg',
             'date': 'July 20, 2019',
             'name': 'Admin',
             'comment': '3',
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'body': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
            {'image': '/static/vegan_app/images/image_6.jpg',
             'date': 'July 20, 2019',
             'name': 'Admin',
             'comment': '3',
             'title': 'Even the all-powerful Pointing has no control about the blind texts',
             'body': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
        ]
        return render(request, 'vegan_app/blog.html', {
            'phone_number': PHONE_NUMBER,
            'email': EMAIL,
            'meat': MEAT,
            'far_far': FAR_FAR,
            'post_info': POST_INFO,
            'phone_info': PHONE_INFO,
            'email_info': EMAIL_INFO,
            'blogs': blogs,
        })


class ContactView(View):

    def get(self, request):
        return render(request, 'vegan_app/contact.html', {
            'phone_number': PHONE_NUMBER,
            'email': EMAIL,
            'meat': MEAT,
            'far_far': FAR_FAR,
            'post_info': POST_INFO,
            'phone_info': PHONE_INFO,
            'email_info': EMAIL_INFO,
        })


class CartView(View):

    def get(self, request):
        cart_list = [
            {'image': '/static/vegan_app/images/product-3.jpg',
             'title': 'Bell Pepper',
             'body': 'Far far away, behind the word mountains, far from the countries',
             'price': '$4.90',
             'total': '$4.90'},
            {'image': '/static/vegan_app/images/product-4.jpg',
             'title': 'Purple Cabbage',
             'body': 'Far far away, behind the word mountains, far from the countries',
             'price': '$15.70',
             'total': '$15.70'},
        ]
        return render(request, 'vegan_app/cart.html', {'phone_number': PHONE_NUMBER,
                                                       'email': EMAIL,
                                                       'meat': MEAT,
                                                       'far_far': FAR_FAR,
                                                       'post_info': POST_INFO,
                                                       'phone_info': PHONE_INFO,
                                                       'email_info': EMAIL_INFO,
                                                       'carts': cart_list,
                                                       })


class ShopView(View):

    def get(self, request, page_id=1):
        products_list = [
            {'name': 'Bell Pepper',
             'image': 'vegan_app/images/product-1.jpg',
             'price': '$120.00',
             'discount': '30%',
             'price_sale': '$80.00'},
            {'name': 'Strawberry',
             'image': 'vegan_app/images/product-2.jpg',
             'price': '$120.00'},
            {'name': 'Green Beans',
             'image': 'vegan_app/images/product-3.jpg',
             'price': '$120.00'},
            {'name': 'Purple Cabbage',
             'image': 'vegan_app/images/product-4.jpg',
             'price': '$120.00'},
            {'name': 'Tomatoe',
             'image': 'vegan_app/images/product-5.jpg',
             'price': '$120.00',
             'discount': '30%',
             'price_sale': '$80.00'},
            {'name': 'Brocolli',
             'image': 'vegan_app/images/product-6.jpg',
             'price': '$120.00'},
            {'name': 'Carrots',
             'image': 'vegan_app/images/product-7.jpg',
             'price': '$120.00'},
            {'name': 'Fruit Juice',
             'image': 'vegan_app/images/product-8.jpg',
             'price': '$120.00'},
            {'name': 'Onion',
             'image': 'vegan_app/images/product-9.jpg',
             'price': '$120.00',
             'discount': '30%',
             'price_sale': '$80.00'},
            {'name': 'Apple',
             'image': 'vegan_app/images/product-10.jpg',
             'price': '$120.00'},
            {'name': 'Garlic',
             'image': 'vegan_app/images/product-11.jpg',
             'price': '$120.00'},
            {'name': 'Chilli',
             'image': 'vegan_app/images/product-12.jpg',
             'price': '$120.00'}
        ]
        paginator = Paginator(products_list, 4)
        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('shop'))
        return render(request, 'vegan_app/shop.html', {'phone_number': PHONE_NUMBER,
                                                       'email': EMAIL,
                                                       'meat': MEAT,
                                                       'far_far': FAR_FAR,
                                                       'post_info': POST_INFO,
                                                       'phone_info': PHONE_INFO,
                                                       'email_info': EMAIL_INFO,
                                                       'products': products,
                                                       })
