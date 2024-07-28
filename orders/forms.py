from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    email = forms.EmailField(required=False)
    requires_delivery = forms.ChoiceField(choices=[("0", False), ("1", True)])
    delivery_address = forms.CharField(required=False)
    cash_on_delivery = forms.ChoiceField(choices=[("0", False), ("1", True)])