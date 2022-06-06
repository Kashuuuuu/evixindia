from django.shortcuts import render

from become_dealer.models import be_dealer

# Create your views here.
def become_dealer(request):
    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        website = request.POST['website']
        organisation = request.POST['organisation']
        firm = request.POST['firm']
        gst = request.POST['gst']
        account = request.POST['account']
        ifsc = request.POST['ifsc']
        accountholder = request.POST['accountholder']
        data = be_dealer(name=name,mobile=mobile,email=email,accountholder=accountholder,ifsc=ifsc,account=account,website=website,gst=gst,organisation=organisation,firm=firm,)
        data.save()
    return render(request,"become_dealer.html")
