from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from core.models import Watches, Orders
from django.views.generic.list import ListView
from core.forms import FilterForm, UserForm

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    #def home(self, request):
        #return render(request, 'core/home.html', {})
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.all().order_by("-date_add")[:4]
        return context
    


class AboutUs(TemplateView):
    template_name = 'about_us.html'

    def about_us(self, request):
        return render(request, 'core/about_us.html', {})  

class Payment(TemplateView):
    template_name = 'payment.html'

    def payment(self, request):
        return render(request, 'core/payment.html', {}) 

class Delivery(TemplateView):
    template_name = 'delivery.html'

    def delivery(self, request):
        return render(request, 'core/delivery.html', {}) 

class Garanty(TemplateView):
    template_name = 'garanty.html'

    def garanty(self, request):
        return render(request, 'core/garanty.html', {}) 

class Contacts(TemplateView):
    template_name = 'contacts.html'

    def contactst(self, request):
        return render(request, 'core/contacts.html', {}) 

class Confidance(TemplateView):
    template_name = 'confidance.html'

    def confidance(self, request):
        return render(request, 'core/confidance.html', {})


class AllBrands(TemplateView):
    template_name = 'all_brands.html'

    def get_context_data(self, **kwargs):
        context = super(AllBrands, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.all()
        return context

class Men(TemplateView):
    template_name = 'men.html'

    def get_context_data(self, **kwargs):
        context = super(Men, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(gender=0)
        return context

class Women(TemplateView):
    template_name = 'women.html'

    def get_context_data(self, **kwargs):
        context = super(Women, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(gender=1)
        return context

class Unisex(TemplateView):
    template_name = 'unisex.html'

    def get_context_data(self, **kwargs):
        context = super(Unisex, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(gender=2)
        return context

class Swiss(TemplateView):
    template_name = 'swiss.html'

    def get_context_data(self, **kwargs):
        context = super(Swiss, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(made_by=0)
        return context

class Europe(TemplateView):
    template_name = 'europe.html'

    def get_context_data(self, **kwargs):
        context = super(Europe, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(made_by=1)
        return context

class Japan(TemplateView):
    template_name = 'japan.html'

    def get_context_data(self, **kwargs):
        context = super(Japan, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(made_by=2)
        return context

class Fashion(TemplateView):
    template_name = 'fashion.html'

    def get_context_data(self, **kwargs):
        context = super(Fashion, self).get_context_data(**kwargs)
        context['watches'] = Watches.objects.filter(fashion=True)
        return context

class Profile(TemplateView):
    template_name = 'profile.html'

    

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        
        return context

# class ProfileProfile(View):
    
#     def post(self, request):
#         form = UserForm(self.request.POST)
#         if form.is_valid():
#             user = User.objects.get(username=username)


class Order(ListView):
    model = Orders
    template_name = 'orders.html'


class FilterView(FormView):
    template_name = "filters.html"
    form_class = FilterForm



