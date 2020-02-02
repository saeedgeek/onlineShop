from django.views.generic import View
from content.models import Category
from django.shortcuts import render
class index(View):
    def get(self, request, *args, **kwargs):
        cat=Category.objects.all()
        print("$$")
        for i in cat :
            print(i)
        return render(request,'index.html',{'cat':cat,})    