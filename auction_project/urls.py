"""auction_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auction import views
from django.conf import settings
from django.conf.urls.static import static
#from auction.views import ItemListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.loginpage,name='login'),
    path('registration/',views.registerpage, name = 'register'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('items/add_item', views.ItemCreateView.as_view(), name='item_add'),
    path('items/<int:pk>/details', views.ItemDetailView.as_view(), name='item_details'),
    path('items/<int:pk>/delete', views.ItemDeleteView.as_view(), name='item_delete'),
    path('items<int:pk>/update', views.ItemUpdateView.as_view(), name='item_update')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
