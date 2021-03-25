from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.views.generic import ListView
from .models import Item, Category
from PIL import Image

# Create your views here.

def loginpage(request):
    return render(request, 'accounts/login.html')

def registerpage(request):
    return render(request, 'accounts/register.html')

def home(request):
    return render(request, "home.html")

def products(request):
    return render(request,"products.html")

class ItemListView(ListView):
    template_name = 'home.html'
    model = Item
    context_object_name = 'items'
    
    def get_queryset(self):

        items = Item.objects.all()

        category = self.request.GET.get('category', None)

        if category is not None:
            items = products.filter(category__id=int(category))

        return items