from django import forms
from django.contrib.auth.models import User
from core.models import NameBrand, Watches

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class FilterForm(forms.Form):


    price_from = forms.FloatField(label="Цена от", required=False)
    price_to = forms.FloatField(label="Цена до", required=False)

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

    

    ordering = forms.ChoiceField(required=False, label="Сортировать по:", choices=[
        ["title", "По алфавиту"],
        ["price", "По возрастанию цены"],
        ["-price", "По уменьшению цены"],
    ])

    brand_form = forms.ModelMultipleChoiceField(queryset=NameBrand.objects.all(), required=False, label="Бренды", widget=forms.CheckboxSelectMultiple)
  
    MEN = 0
    WOMEN = 1
    UNISEX = 2

    GENDER_CHOICES = (
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (UNISEX, 'Unisex')
    )

    gender_form = forms.MultipleChoiceField(required=False, label="Пол",
        widget=forms.CheckboxSelectMultiple, choices=GENDER_CHOICES)

    SWISS = 0
    EUROPE = 1
    JAPAN = 2

    COUNTRY_CHOICES = (
        (SWISS, 'Швейцарские'),
        (EUROPE, 'Европейские'),
        (JAPAN, 'Японские')
    )

    made_form = forms.MultipleChoiceField(choices=COUNTRY_CHOICES, required=False, label="Производитель",
        widget=forms.CheckboxSelectMultiple)

    KVARTZ = 0
    MECHAN = 1
    MECHAN_AVTO = 2
    AVTOKVARTZ = 3
    KVARTZ_MECHAN_AVTO = 4


    MECHANISM_CHOICES = (
        (KVARTZ, 'Кварцевый'),
        (MECHAN, 'Механический'),
        (MECHAN_AVTO, 'Механический с автоподзаводом'),
        (AVTOKVARTZ, 'Автокварцевый'),
        (KVARTZ_MECHAN_AVTO, 'Кварцевый + механический с автоподзаводом')
    )

    mechanism_form = forms.MultipleChoiceField(choices=MECHANISM_CHOICES, required=False, label="Тип механизма",
        widget=forms.CheckboxSelectMultiple)

    ALUM = 0
    GOLD = 1
    KERAM = 2
    KERAM_STEEL = 3
    METALL = 4
    METALL_GOLD = 5
    METALL_POLIMER = 6

    KORPUS_CHOICES = (
        (ALUM, 'Алюминий'),
        (GOLD, 'Золото'),
        (KERAM, 'Керамика'),
        (KERAM_STEEL, 'Керамика+сталь'),
        (METALL, 'Металл'),
        (METALL_GOLD, 'Металл+позолота'),
        (METALL_POLIMER, 'Металл-полимер')
    )

    korpus_form = forms.MultipleChoiceField(choices=KORPUS_CHOICES, required=False, label="Тип корпуса",
        widget=forms.CheckboxSelectMultiple)

    def save(self):
        print(self.cleaned_data)
        print(self.cleaned_data.pop('gender_form'))
       
        # gender_list = []
        # for gen in self.cleaned_data.pop('gender_form'):
        #     new_gen = int(gen)
        #     gender_list.append(new_gen)
        print(type(self.cleaned_data.pop('gender_form')))
        qs = Watches.objects.filter(price__gte=self.cleaned_data.pop('price_from'),
                                    price__lte= self.cleaned_data.pop('price_to')
                                    # ordering = self.cleaned_data.pop('ordering'), 
                                    # namebrand__in = self.cleaned_data.pop('brand_form')
                                    #gender__in = gender_list,  
                                    #made_by= self.cleaned_data.pop('made_form'), 
                                    #mechanism= self.cleaned_data.pop('mechanism_form')
                                    # korpus=self.cleaned_data.pop('korpus_form')
            )
        # print(qs)
        return qs
    

