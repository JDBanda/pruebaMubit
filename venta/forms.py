from django import forms

class SaleForm(forms.Form):
    amount = forms.FloatField()
    client_change = forms.FloatField()
