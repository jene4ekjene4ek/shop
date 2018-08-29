from django.conf.urls import url, include
from core.views import Home, AboutUs, Payment, Delivery, Garanty, Contacts, Confidance, LoginFormView, RegisterFormView, AllBrands
#from django.views.generic import ListView, DetailView
from core.models import Watches

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^about_us/$', AboutUs.as_view(), name='about_us'),
    url(r'^payment/$', Payment.as_view(), name='payment'),
    url(r'^delivery/$', Delivery.as_view(), name='delivery'),
    url(r'^garanty/$', Garanty.as_view(), name='garanty'),
    url(r'^contacts/$', Contacts.as_view(), name='contacts'),
    url(r'^confidance/$', Confidance.as_view(), name='confidance'),
    #url(r'^login/$', LoginFormView.as_view(), name='login'),
    #url(r'^register/$', RegisterFormView.as_view(), name='register'),
    url(r'^all_brands/$', AllBrands.as_view(), name='all_brands'),
    url(r'^accounts/', include('registration.backends.simple.urls'))
    
    
]