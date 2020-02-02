from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View,TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from Shop import settings
from .models import Profile
import re as reg
# Create your views here.


class register_views(TemplateView):
    def get(self,request): 
        my_param = request.GET.get('username')
        if my_param is None:
            return render(request,'user_templates/register.html')
        else:
            username = request.GET['username']
            password = request.GET['password']
            lastName = request.GET['lastName']
            firstName = request.GET['firstName']
            email = request.GET['email']
            phoneNumber = request.GET['phoneNumber']
            Gender = request.GET['Gender']
            profile=Profile.objects.create_user(username,email,password)
            profile.first_name=firstName
            profile.last_name=lastName
            profile.phone_number=phoneNumber
            profile.gender=Gender
            profile.save()
            return(HttpResponse('ok'))


class login_views(View):
    def get(self,request):
        my_param = request.GET.get('username')
        if my_param is not None:
            username = my_param
            password = request.GET['password']
            phone=reg.findall(r'^\d{10}$',username)
            em=reg.findall(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",username)
            if phone:
                un=Profile.objects.filter(phone_number=phone[0]).first().username
                if un:
                    username=un
                else: 
                    return HttpResponse("Inactive user.")
                
            elif em:
                un=Profile.objects.filter(email=em[0]).first().username
                if un:
                    username=un
                else: 
                    return HttpResponse("Inactive user.")
                
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,"index.html")
                else:
                    return HttpResponse("Inactive user.")
            else:
                return HttpResponseRedirect(settings.LOGIN_URL)

            return render(request, "index.html")
        else:
            return render(request,'user_templates/login.html')    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

class profileView(View):
    username = None
    profile=None
    def get(self,request):
        if request.user.is_authenticated:
            username = request.user.username
            profile=Profile.objects.filter(username=username).first()
        if profile:

            return render(request,"user_templates/profile.html",context={"profile":profile})
        else:
            return HttpResponse("user not valid")    
