from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Design, Medium
from rest_framework import viewsets
from .serializers import ProductSerializer
from django.template.context_processors import csrf

# Create your views here.
def all_products(request):
    designs = Design.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, "products.html", {"designs": designs}, args)

def product_options(request, id):
    media_types = Medium.objects.all()
    design = get_object_or_404(Design,pk=id)
    return render(request, "product_options.html",{"design":design, "media_types": media_types})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class = ProductSerializer