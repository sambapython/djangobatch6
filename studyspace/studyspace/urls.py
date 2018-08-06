"""studyspace URL Configuration

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
from django.conf.urls.static import static
from app1.views import view_index, view_syudyhalls, view_hall_update,\
view_hall_delete, view_reports, view_logout, view_forgotpassword, \
ExpensesView
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', view_index),
    url(r'^studyhalls/', view_syudyhalls),
    url(r'^expenses/', ExpensesView),
    url(r'^enquiry/', ExpensesView),
    url(r'^hall_update/([0-9]+)/', view_hall_update),
    url(r'^hall_delete/([0-9]+)/', view_hall_delete),
    url(r'^reports/', view_reports),
    url(r'^logout/', view_logout),
    url(r'^forgotpassword/', view_forgotpassword),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
