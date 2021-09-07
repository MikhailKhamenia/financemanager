from django.contrib import admin
from .models import Transactions, TransactionsPermissions
# Register your models here.

admin.site.register(Transactions)
admin.site.register(TransactionsPermissions)
