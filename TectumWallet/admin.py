from django.contrib import admin
from .models import Wallet, Transaction
# Register your models here.
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to' , "amount" , "date_time")
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Transaction,TransactionAdmin)
