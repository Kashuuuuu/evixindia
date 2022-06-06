from django.shortcuts import render
from index.models import products

# Create your views here.
def product(request):
    data = products.objects.all()
    context = {'data':data}
    
    return render(request,"product.html",context)
