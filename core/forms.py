from django import forms
from django.contrib.auth.models import User
from core.models import NameBrand, Watches, Order, OrderPosition

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class FilterForm(forms.Form):


    # price_from = forms.FloatField(label="Цена от", required=False)
    # price_to = forms.FloatField(label="Цена до", required=False)

    # def clean(self):
    #     if self.cleaned_data['price_from'] > self.cleaned_data['price_to']:
    #         raise forms.ValidationError("Price from cant be greater then Price to")
    #         return self.cleaned_data

    # def clean_price_from(self):
    #     if self.cleaned_data.get('price_from', 0) < 0:
    #         raise forms.ValidationError(
    #             "Price from should be positive.")
    #     return self.cleaned_data['price_from']

   

    # def clean_price_to(self):
    #     if self.cleaned_data.get('price_to', 0) < 0:
    #         raise forms.ValidationError(
    #             "Price from should be positive.")
    #     return self.cleaned_data['price_to']

    

    # ordering = forms.ChoiceField(required=False, label="Сортировать по:", choices=[
    #     ["title", "По алфавиту"],
    #     ["price", "По возрастанию цены"],
    #     ["-price", "По уменьшению цены"],
    # ])

    # brand_form = forms.ModelChoiceField(queryset=NameBrand.objects.all(),
    #     label="Бренды", widget=forms.CheckboxSelectMultiple, empty_label=None, required=False)
    MEN = 'M'
    WOMEN = 'W'
    UNISEX = 'U'

    GENDER_CHOICES = (
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (UNISEX, 'Unisex')
    )

    gender_form = forms.ChoiceField(required=False, label="Пол",
        widget=forms.CheckboxSelectMultiple, choices=GENDER_CHOICES)

    # SWISS = 0
    # EUROPE = 1
    # JAPAN = 2

    # COUNTRY_CHOICES = (
    #     (SWISS, 'Швейцарские'),
    #     (EUROPE, 'Европейские'),
    #     (JAPAN, 'Японские')
    # )

    # made_form = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False, label="Производитель",
    #     widget=forms.CheckboxSelectMultiple)

    # KVARTZ = 0
    # MECHAN = 1
    # MECHAN_AVTO = 2
    # AVTOKVARTZ = 3
    # KVARTZ_MECHAN_AVTO = 4


    # MECHANISM_CHOICES = (
    #     (KVARTZ, 'Кварцевый'),
    #     (MECHAN, 'Механический'),
    #     (MECHAN_AVTO, 'Механический с автоподзаводом'),
    #     (AVTOKVARTZ, 'Автокварцевый'),
    #     (KVARTZ_MECHAN_AVTO, 'Кварцевый + механический с автоподзаводом')
    # )

    # mechanism_form = forms.ChoiceField(choices=MECHANISM_CHOICES, required=False, label="Тип механизма",
    #     widget=forms.CheckboxSelectMultiple)

    # ALUM = 0
    # GOLD = 1
    # KERAM = 2
    # KERAM_STEEL = 3
    # METALL = 4
    # METALL_GOLD = 5
    # METALL_POLIMER = 6

    # KORPUS_CHOICES = (
    #     (ALUM, 'Алюминий'),
    #     (GOLD, 'Золото'),
    #     (KERAM, 'Керамика'),
    #     (KERAM_STEEL, 'Керамика+сталь'),
    #     (METALL, 'Металл'),
    #     (METALL_GOLD, 'Металл+позолота'),
    #     (METALL_POLIMER, 'Металл-полимер')
    # )

    # korpus_form = forms.ChoiceField(choices=KORPUS_CHOICES, required=False, label="Тип корпуса",
    #     widget=forms.CheckboxSelectMultiple)

    def save(self):
        print(self.cleaned_data)
    


class OrderingForm(forms.Form):

    NAME = 0
    PRICE = 1
    # - PRICE = 2
    

    SORT_CHOICES = (
        (NAME, 'По алфавиту'),
        (PRICE, 'По возрастанию цены'),
        # (- PRICE, 'По уменьшению цены'),
    )

    ordering = forms.ChoiceField(choices=SORT_CHOICES, label="Сортировать по:")

class AddToChartForm(forms.Form):
    watches = forms.ModelChoiceField(Watches.objects.all())

class OrderForm(forms.Form):
    class Mete:
        model = Order
        fields = '__all__'

class OrderPositionForm(forms.Form):
    class Meta:
        model = OrderPosition
        fields = '__all__'


OrderPosisionFormset = forms.inlineformset_factory(
    Order,
    OrderPosition,
    OrderPositionForm,
    extra = 0
 )