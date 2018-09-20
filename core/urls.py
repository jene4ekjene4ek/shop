from django.conf.urls import url, include
from core.views import Home, AboutUs, Payment, Delivery, Garanty, Contacts, Confidance,  AllBrands, Profile, Order, FilterView, Men, Women, Unisex, Swiss, Japan, Europe, Fashion, WatchView, Br
#from django.views.generic import ListView, DetailView
from core.models import Watches
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^about_us/$', AboutUs.as_view(), name='about_us'),
    url(r'^payment/$', Payment.as_view(), name='payment'),
    url(r'^delivery/$', Delivery.as_view(), name='delivery'),
    url(r'^garanty/$', Garanty.as_view(), name='garanty'),
    url(r'^contacts/$', Contacts.as_view(), name='contacts'),
    url(r'^confidance/$', Confidance.as_view(), name='confidance'),
    url(r'^all_brands/$', AllBrands.as_view(), name='all_brands'),
    url(r'^men/$', Men.as_view(), name='men'),
    url(r'^women/$', Women.as_view(), name='women'),
    url(r'^unisex/$', Unisex.as_view(), name='unisex'),
    url(r'^swiss/$', Swiss.as_view(), name='swiss'),
    url(r'^europe/$', Europe.as_view(), name='europe'),
    url(r'^japan/$', Japan.as_view(), name='japan'),
    url(r'^fashion/$', Fashion.as_view(), name='fashion'),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/', Profile.as_view(), name='profile'),
    url(r'^orders/', Order.as_view(), name='orders'),
    url(r'^admin/', admin.site.urls),
    url(r'^filter_form/', FilterView.as_view()),
    url(r'^(?P<slug>[-\w]+)/$', WatchView.as_view(), name='watch_detail'),
    #url(r'^(?P<slug>[-\w]+)/$', Brand.as_view(), name='brand'),
    #url(r'^brand/$', Brand.as_view(), name='brand'),
    url(r'^brand/$', Br.as_view(), name='brand'),
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)