from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from core.models import Watches, Orders
from django.views.generic.list import ListView

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


class Profile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        #ser_profile=User.objects.filter()

        # context['published'] = user_posts.filter(
        #     is_published=True)
        # context['not_published'] = user_posts.filter(
        #     is_published=False
        # )
        return context


class Order(ListView):
    model = Orders
    template_name = 'orders.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



