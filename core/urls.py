from django.conf.urls import url, include
from core.views import Home, AboutUs, Payment, Delivery, Garanty, Contacts, Confidance,  AllBrands, Profile, Men, Women, Unisex, Swiss, Japan, Europe, Fashion, WatchView, BrandView, Sale, PreOrder, CartCart, AddToCart

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
 
    url(r'^admin/', admin.site.urls),
     url(r'^cart/$', CartCart.as_view(), name='cart'),
    url(r'^sale/$', Sale.as_view(), name='sale'),
    url(r'^preorder/$', PreOrder.as_view(), name='preorder'),
    url(r'^(?P<namebrand_slug>[-\w]+)/$$', BrandView.as_view(), name='brand_detail'),
    # url(r'^\w+/(?P<namebrand_slug>[-\w]+)/$$', BrandView.as_view(), name='brand_detail'),
    url(r'^add_to_cart/(?P<watch_slug>[-\w]+)/$', AddToCart.as_view(), name='add_to_cart'),
    url(r'^cart/$', CartCart.as_view(), name='cart'),
    # url(r'^all_brands_test/$', AllBrandsTest.as_view(), name='all_brands_test'),
    # url(r'^finish/$', 'core.views.closed_order', name='finish'),
    url(r'^(?P<slug>[-\w]+)/$', WatchView.as_view(), name='watch_detail'),
    url(r'^\w+/(?P<slug>[-\w]+)/$', WatchView.as_view(), name='watch_detail'),
   
    
    
    
    
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)