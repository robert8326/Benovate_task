from django import forms

from transfer.models import User


def get_all_user():
    return User.objects.all()


class TransferForm(forms.Form):
    payer = forms.ChoiceField(choices=get_all_user())
    cost = forms.CharField(max_length=15)
    inn = forms.MultiValueField(fields=())
