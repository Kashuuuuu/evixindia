from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages as sms
from django.contrib.auth.models import User
from contact.models import contactus
from dashboard import views
from dashboard.models import ad_profile,frgt_pwd

from django.core.mail import send_mail
from django.conf import settings
from become_dealer.models import be_dealer


# Create your views here.
def admin_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request,"dashboard.html")
    else:
        return redirect('login')    

def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('admin_dash')
    else:
        if request.method == 'POST':   
            username = request.POST.get('username')
            password= request.POST.get('password') 
            print(username)
            USER = authenticate(request, username=username,password=password)
            if USER is not None:
                login(request,USER)
                if request.user.is_superuser:
                    sms.success(request,"Logged in successfully..")
                    return redirect('admin_dash')
                else:
                    sms.success(request,"wrong username or password")
                    return redirect('login')

    return render(request,"login.html") 

def ad_logout(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            logout(request)
            sms.success(request,"Logged out successfully..")
            return redirect('login')
        except:
            sms.warning(request,'something went wrong !')
            return redirect('login')
    else:        
        return redirect('login')  

def admin_profile(request):
    if request.user.is_authenticated and request.user.is_superuser:
        profile_data = ad_profile.objects.all()
        se= request.POST.get('edit')
        if request.POST.get('uss')!=None:
                   
                    old = request.POST['old']
                    new = request.POST['new']
                    confirm = request.POST['confirm']
                    user = User.objects.get(id=request.user.id)
                    mail=user.email
                    check=user.check_password(old)
                    if confirm==new:
                        if check==True:
                            user.set_password(new)
                            user.save()
                            # user=User.objects.get(email=mail)
                            login(request,user)
                            sms.success(request, "Password Updated")
                            return redirect('admin_profile')
                        else:
                            sms.error(request, "Incorrect Old Password")
                            return redirect('admin_profile')
                    else:
                        sms.error(request,'New And Confirm Password Not Match.')
        elif se!=None:
            img = request.POST['img']
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            dob = request.POST['dob']
            address = request.POST['address']
            prod = ad_profile.objects.filter(id=se)
            if len(prod)>0:
                ob=prod[0] 
                print(ob)
                if len(img)>0:
                    ob.img=img
                if len(name)>0:
                    ob.name=name
                if len(email)>0:
                    ob.email=email
                if len(dob)>0:
                    ob.dob=dob
                if len(address)>0:
                    ob.address=address
                if len(mobile)>0:
                    ob.mobile=mobile    
                ob.save()
                sms.success(request,"Profile updated successfully..")                
            return redirect('admin_profile')
        

    context = {'profile_data':profile_data}
    return render(request,"profile.html",context)    

def password_reset(request,token):
    if request.user.is_authenticated!=True and request.user.is_superuser!= True:
        if request.method=='POST':
            try:
                pass1=request.POST['pass1']
                confirm=request.POST['pass2']
                if pass1==confirm:
                    frgpwd=frgt_pwd.objects.get(frg_token=token)
                    user=User.objects.get(username=frgpwd)
                    user.set_password(pass1)
                    user.save()
                    sms.success(request, "Password Change Successfully.\n +Please login. ")
                    return redirect('login')
                else:
                    sms.error(request,'Password Not Match.Enter Same Password.')
            except:
                pass
        return render(request,'password_reset.html')
    else:
        return redirect('error')    

def user(request):
    data = contactus.objects.all()
    context = {'data': data}

    return render(request,"user.html" ,context)

def dealer(request):
    data = be_dealer.objects.all()
    context = {'data': data}

    return render(request,"dealer.html" ,context)    