from django import forms


class OrderForm(forms.Form):
    ''' делает обязательные поля ввода '''
    name = forms.CharField(max_length=200, required=False) # делает нейм необязательным
    phone = forms.CharField(max_length=200)