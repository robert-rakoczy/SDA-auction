from django.shortcuts import render
from django.http import HttpResponse,Http404, request
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Item, Category, User, Bidding, Transaction, Watchlist, Purchase
from PIL import Image
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.

def loginpage(request):
    return render(request, 'accounts/login.html')

def registerpage(request):
    return render(request, 'accounts/register.html')

def home(request):
    return render(request, "home.html")

def items(request):
    return render(request,"products.html")

class ItemListView(ListView):
    template_name = 'home.html'
    model = Item
    context_object_name = 'items'
    
    def get_queryset(self):
        items = Item.objects.all()

        category = self.request.GET.get('category', None)

        if category is not None:
            items = items.filter(category__id=int(category))

        return items


class ItemCreateView(CreateView, PermissionRequiredMixin):
    permission_required = ['auction.add_item']
    template_name = 'add_item.html'
    model = Item
    Item.location = User.city
    fields = '__all__'
    success_url = reverse_lazy('index')

class ItemDetailView(DetailView):
    template_name = 'item_details.html'
    model = Item
    context_object_name = 'item'

class ItemUpdateView(UpdateView, PermissionRequiredMixin):
    template_name = 'item_update.html'
    model = Item
    context_object_name = 'item'
    fields = '__all__'
    success_url = reverse_lazy('home')

class ItemDeleteView(DeleteView, PermissionRequiredMixin):
    template_name = 'item_delete.html'
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('home')

