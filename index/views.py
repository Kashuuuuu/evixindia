from django.shortcuts import render


# Create your views here.
def index(request):
    # data = product.objects.all()
    # context = {'data':data}
    return render(request,"index.html")
