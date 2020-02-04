from django.views.generic import View
from content.models import Category
from django.shortcuts import render
class index(View):
    def get(self, request, *args, **kwargs):
        cat=Category.objects.filter(top_category=None)
        return render(request,'index.html',{'cat':cat,})    