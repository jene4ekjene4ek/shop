from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View, DetailView, UpdateView
from django.views.generic.edit import FormView
from core.models import Watches, Order, NameBrand, Cart, CartItem
from django.views.generic.list import ListView
from .forms import UserForm, FilterForm, OrderPositionForm, OrderForm, AddToChartForm
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import WatchesFilterTest
from django.shortcuts import get_object_or_404
from django.db.models import Q
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

    def add_to_cart(self, request):
        order = get_order(request)
        if not order:
            order = Order.objects.create()
            request.session['order_id'] = order.id
        form = AddToChartForm(request.POST)
        if form.is_valid():
            watches = form.cleaned_data['watches']
            order_position, created = OrderPosition.objects.get_or_create(
                watches = watches,
                order = order
            )

            order.position.count +=1
            order.position.save()

        return redirect('cart')

    def get_order(self, request):
        order_id = request.session.get('order_id')
        order = None
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
            except Order.DoesNotExist:
                pass
        return order

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




# class Order(ListView):
#     model = Order
#     template_name = 'orders.html'


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

   


class BrandView(FormMixin, ListView):
    template_name = "brand.html"
    model = NameBrand, Watches
    form_class=FilterForm

    # def brand(self, request, namebrand_slug):
    #     brand = NameBrand.objects.get(slug=namebrand_slug)
    #     watches = Watches.objects.filters(namebrand=brand)
    #     # context = {
    #     #     'brand': brand,
    #     #     'watches': watches
    #     # }
    #     for watch in watches:
    #         print(watch)
    #     return render(request, 'core/brand.html', {})


        # return brand

    # def get_context_data(self, **kwargs):
    #     context=super(BrandView, self).get_context_data(**kwargs)
    #     context['brand'] = NameBrand.objects.filters(slug=namebrand_slug)
    #     context['watches'] = Watches.objects.filters(namebrand=brand)
    #     for watch in watches:
    #         print(watch)
    #     return context

    def get_brand(self):
        namebrand_id=self.kwargs.get('namebrand_id')
        namebrand = None
        if namebrand_id:
            brand = get_object_or_404(NameBrand, id=namebrand_id)
            self.namebrand = namebrand
        return brand

    def get_queryset(self, ):
        queryset = super().get_queryset()
        if self.namebrand:
            queryset = queryset.filter(namebrand=namebrand)
        return queryset

  
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

# class AllBrandsTest(TemplateView):
#     template_name = 'all_brands_test.html'
#     model = Watches
#     filer_class=WatchesFilterTest

    # def search(self, request):
    #     watch_list = Watches.objects.all()
    #     watches_filter = WatchesFilterTest(request.GET, queryset=watch_list)
    #     return render(request, 'all_brands_test.html', {'filter': watches_filter})

    # def get_context_data(self, **kwargs):
    #     context = super(AllBrandsTest, self).get_context_data(**kwargs)
    #     context['watches'] = Watches.objects.all()
    #     context['filter'] = WatchesFilterTest(request.GET, queryset=watches)
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super(AllBrands, self).get_context_data(**kwargs)
    #     context['watches'] = Watches.objects.all()
    #     context['form'] = self.get_form()
    #     return context

    


    

