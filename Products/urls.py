from django.conf.urls import url
from .views import all_products, product_options

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<id>\d+)/options', product_options, name='product_options'),    
]