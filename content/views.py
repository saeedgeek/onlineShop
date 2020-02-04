from django.shortcuts import render
from django.views.generic import TemplateView,View
# Create your views here.
from user.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Category as Categorym
from .models import Product ,Cart as cartmodel,Product_Cart
from user.models import Profile
@method_decorator(login_required,name="dispatch")
class Cart(View):
    def get(self, request, *args, **kwargs):
        user=request.user
        profile=Profile.objects.get(username=user.username)
        return render(request,'cart.html',{'name':profile.phone_number,})    

class Category(View):
    def get(self, request, *args, **kwargs):
        user=request.user
        profile=Profile.objects.get(username=user.username)
        cart,bol=cartmodel.objects.get_or_create(user=profile)

        if "rempr" in request.GET:
            product_name=request.GET["rempr"]
            product=Product.objects.get(name=product_name)
            Product_Cart.objects.filter(crt=cart,prdc=product).delete()
            catname=product.category.category_name
        elif "addpr" in request.GET:
            product_name=request.GET["addpr"]
            product=Product.objects.get(name=product_name)
            Product_Cart.objects.get_or_create(crt=cart,prdc=product,count=1)
            catname=product.category.category_name
        else :
            catname=request.GET["category_name"]
        category=Categorym.objects.get(category_name=catname)
        subCategorie=Categorym.objects.filter(top_category=category)
        product=Product.objects.filter(category=category)
        
        return render(request,'category.html',{"subcat":subCategorie,"product":product,"cart":cart})    




