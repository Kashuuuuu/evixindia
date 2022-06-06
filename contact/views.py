from django.shortcuts import render
from contact.models import contactus
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages as sms
# Create your views here.
def contact(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        service = request.POST['service']
        enquiry = request.POST['enquiry']
        data = contactus(firstname=firstname,lastname=lastname,email=email,mobile=mobile,service=service,enquiry=enquiry)
        # data.save()
          
        send_mail("get in touch",
        enquiry,
        settings.EMAIL_HOST_USER,
        [email]
        )
       
    sms.success(request,'Information sent successfully..')        
    return render(request,"contact.html")