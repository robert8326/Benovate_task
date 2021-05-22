from django.http import HttpResponse

from transfer.forms import TransferForm
from django.shortcuts import render, redirect
from django.views import View

from transfer.models import User


class TransferView(View):
    def get(self, request):
        form = TransferForm()
        return render(request, 'transfer/forms.html', {'form': form})

    def post(self, request):
        form = TransferForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('/')
        form = TransferForm()
        return render(request, 'transfer/forms.html', context={'forms': form})
