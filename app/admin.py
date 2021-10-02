from django.contrib import admin
from .models import *
# Register your models here.


class CustomerAdin(admin.ModelAdmin):
    list_display = ['mobile']

admin.site.register(Customer,CustomerAdin)
admin.site.register(Temp)
admin.site.register(ImageUpload)
admin.site.register(Trademan)
admin.site.register(TradeType)
admin.site.register(BookTradeMan)