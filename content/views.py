from django.shortcuts import render
from django.views.generic import TemplateView,View
# Create your views here.
from user.models import Profile
class Cart(View):
    def get(self, request, *args, **kwargs):
        user=request.user
        profile=Profile.objects.get(username=user.username)
        return render(request,'cart.html',{'name':profile.phone_number,})    