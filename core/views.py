from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View, DetailView, UpdateView
from django.views.generic.edit import FormView
from core.models import Watches, NameBrand, Cart, CartItem
from django.views.generic.list import ListView
from .forms import UserForm, FilterForm
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'


    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.all().order_by("-date_add")[:4]
        context['brands'] = context['brands'] = NameBrand.objects.all()[:18]
        return context


class AboutUs(TemplateView):
    template_name = 'about_us.html'



class Payment(TemplateView):
    template_name = 'payment.html'



class Delivery(TemplateView):
    template_name = 'delivery.html'



class Garanty(TemplateView):
    template_name = 'garanty.html'



class Contacts(TemplateView):
    template_name = 'contacts.html'



class Confidance(TemplateView):
    template_name = 'confidance.html'




class AllBrands(FormMixin, TemplateView):
    template_name = 'all_brands.html'
    form_class = FilterForm
    model = Watches

    

    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.all()
        #context['form'] = self.get_form()
        return context

    def post(self, request):
        form = FilterForm(request.POST)
        if form.is_valid():
            watches = form.save()
            return render(request, 'all_brands.html', {'form': form, 'watches': watches})
        print(form.errors)
        return render(request, 'all_brands.html', {'form': form})

    

class Men(AllBrands):
    template_name = 'men.html'


    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(gender=0)
        return context

class Women(AllBrands):
    template_name = 'women.html'
    
    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(gender=1)
        return context

class Unisex(AllBrands):
    template_name = 'unisex.html'

    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(gender=2)

        return context

class Swiss(AllBrands):
    template_name = 'swiss.html'
    
    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(made_by=0)
        return context

class Europe(AllBrands):
    template_name = 'europe.html'
    
    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(made_by=1)
        return context

class Japan(AllBrands):
    template_name = 'japan.html'
  
    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(made_by=2)
        return context

class Fashion(AllBrands):
    template_name = 'fashion.html'


    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(fashion=True)
        return context

class Sale(AllBrands):
    template_name = 'sale.html'


    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(discount__gt=0)
        return context

class PreOrder(AllBrands):
    template_name = 'preorder.html'


    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(status=False)
        return context

class Profile(FormView):
    template_name = 'profile.html'
    form_class = UserForm
    success_url = '/profile/'

    def form_valid(self, form):
        form.save()
        return super(Profile, self).form_valid(form)

    def get_form_kwargs(self):
        form_kwargs = super(Profile, self).get_form_kwargs()
        form_kwargs['instance'] = self.request.user
        return form_kwargs






class AddToCart(View):

     def add_to_cart_view(self, request, watch_slug):
        try:
            cart_id=request.session['cart.id']
            cart=Cart.objects.get(id=cart_id) 
            request.session['total'] = cart.items.count()
        except:
            cart=Cart()
            cart.save()
            cart_id=cart.id
            request.session['cart_id']=cart_id
            cart=Cart.objects.get(id=cart_id)

        watch = Watches.objects.get(slug=watch_slug)
        new_item = CartItem.objects.get_or_create(watch=watch, item_total=watch.price)
        cart = Cart.objects.first()
        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()
            return HttpResponseRedirect('/cart/')

class WatchView(DetailView, AddToCart):
    template_name = "watches.html"
    model = Watches

    def watch(self, request, watch_slug):
        watch = Watches.objects.get(slug=watch_slug)
        return render(request, 'core/watches.html', {})

   


class BrandView(FormView, ListView):
    template_name = "brand.html"
    model = NameBrand
    form_class=FilterForm
 


    def get_queryset(self):
        self.brand = get_object_or_404(NameBrand, slug=self.kwargs['namebrand_slug'])
        return NameBrand.objects.get(name=self.brand)

 

    def get_context_data(self, **kwargs):
        context = super(BrandView, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(namebrand=self.brand)
        context['brr'] = brand = NameBrand.objects.get(name=self.brand)
        return context

    def post(self, request):
        form = FilterForm(request.POST)
        if form.is_valid():
            watches = form.save()
            return render(request, 'brand.html', {'form': form, 'watches': watches})
        print(form.errors)
        return render(request, 'brand.html', {'form': form})

  
class CartCart(TemplateView):
    template_name = "cart.html"

    # def cart(self, request, watch_slug):
    #     try:
    #         cart_id=request.session['cart.id']
    #         cart=Cart.objects.get(id=cart_id) 
    #         request.session['total'] = cart.items.count()
    #     except:
    #         cart=Cart()
    #         cart.save()
    #         cart_id=cart.id
    #         request.session['cart_id']=cart_id
    #         cart=Cart.objects.get(id=cart_id)
    #     context = {
    #         'cart': cart
    #     }
    #     return render(self, 'cart.html', context)

    def get_context_data(self, **kwargs):
        
        context=super(CartCart, self).get_context_data(**kwargs)
        context['cart'] = Cart.objects.first()
        return context
 
    # def cart_view(self, request):
    #     cart = Cart.objects.first()
        # context = {
        #     'cart': cart
        # }
        # return render(self, 'cart.html', context)


    


    

