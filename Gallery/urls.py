from django.conf.urls import url
from .views import all_paintings

urlpatterns = [
    url(r'^$', all_paintings, name='gallery'),
]