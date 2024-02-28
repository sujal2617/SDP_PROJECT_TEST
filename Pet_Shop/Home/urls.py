from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home1"),
    path("about/", views.about, name="About"),
    path("animals/", views.animals, name="Animals"),
    path("dogs/", views.dog, name="Dogs"),
    path("cats/", views.cat, name="Cat"),
    path('rabbit/', views.rabbit, name='Rabbit'),
    path("contact/", views.contact, name="contact"),
    path('success/', views.success, name='success_page'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('faqs/', views.faqs, name='faqs'),
    path("birds/", views.birds, name="Birds"),
    path("fishes/", views.fish, name="Fish"),
    path("accessories/", views.accessories, name="Accessory"),
    path('add_product/',views.add_product,name='add_product'),
    path('product_list/',views.product_list,name='product_list'),
    path('change_password/', views.change_password, name='change_password'),
    path('checkout/',views.checkout,name='Checkout'),
    path('checkout/success/',views.payment_sucess,name="success_page"),
]