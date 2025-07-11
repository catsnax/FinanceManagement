from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_type', 'amount', 'user', 'transaction_date']
    list_filter = ['transaction_type', 'user', 'transaction_date']
    search_fields = ['user__username, user__email']
    date_hierarchy = 'transaction_date'
    raw_id_fields = ['user']
    show_facets = admin.ShowFacets.ALWAYS