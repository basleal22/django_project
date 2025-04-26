from django.shortcuts import render
from .models import product
# Create your views here.
def product_detail_view(request):
    obj = product.objects.get(id=1)
    context = {
        'title':obj.title,
        'description':obj.description,
    }
    return render(request, "product/detail.html",context)#on the "" we insert our template that we have created,{} is our context variable\
