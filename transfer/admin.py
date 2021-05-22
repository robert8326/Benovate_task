from django.contrib import admin
from transfer.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['date_joined', 'last_login']
    list_filter = ('is_staff', 'bill', 'is_active', 'inn',)
    list_display = ('username', 'inn', 'bill')
    date_hierarchy = 'date_joined'
