"""genericviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from app1.views import index_view
from app1.models import Customer, Product, SalesOrder
from django.views.generic import TemplateView, CreateView, ListView,\
UpdateView, DeleteView

from app1.views import SaleCreateview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', TemplateView.as_view(
    	template_name="app1/index.html")),
    url(r'^customers/', ListView.as_view(
    	model=Customer,
    	)),
    url(r'^deletecustomer/(?P<pk>[0-9]+)', DeleteView.as_view(
    	model=Customer,
    	template_name="app1/cust_delete.html",
    	success_url="/customers/",
    	)),
    
    url(r'^updatecustomer/(?P<pk>[0-9]+)', UpdateView.as_view(
    	model=Customer,
    	success_url="/customers/",
    	fields="__all__",
    	)),
    url(r'^createcustomer/', CreateView.as_view(
    	model=Customer,
    	success_url="/customers/",
    	fields="__all__",
    	)),
    url(r'^products/', ListView.as_view(
    	model=Product,
    	)),
    url(r'^deleteproduct/(?P<pk>[0-9]+)', DeleteView.as_view(
    	model=Product,
    	template_name="app1/product_delete.html",
    	success_url="/products/",
    	)),
    
    url(r'^updateproduct/(?P<pk>[0-9]+)', UpdateView.as_view(
    	model=Product,
    	success_url="/products/",
    	fields="__all__",
    	)),
    url(r'^createproduct/', CreateView.as_view(
    	model=Product,
    	success_url="/products/",
    	fields="__all__",
    	)),
    url(r'^saleorders/', ListView.as_view(
    	model=SalesOrder,
    	)),
    url(r'^deletesaleorder/(?P<pk>[0-9]+)', DeleteView.as_view(
    	model=SalesOrder,
    	template_name="app1/saleorder_delete.html",
    	success_url="/saleorders/",
    	)),
    
    url(r'^updatesaleorder/(?P<pk>[0-9]+)', UpdateView.as_view(
    	model=SalesOrder,
    	success_url="/saleorder/",
    	fields="__all__",
    	)),
    url(r'^createsaleorder/', SaleCreateview.as_view(
    	model=SalesOrder,
    	success_url="/saleorders/",
    	fields="__all__",
    	)),
]
