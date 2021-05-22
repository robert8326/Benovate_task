from django.urls import path
from transfer.views import TransferView

urlpatterns = [
    path('', TransferView.as_view(), name='transfer')
]
