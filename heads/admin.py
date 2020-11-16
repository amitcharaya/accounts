from django.contrib import admin


from .models import *


@admin.register(AccountHeads)
class AccountHeadsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register((Account))
class AccountAdmin(admin.ModelAdmin):
    list_display=['name']


@admin.register(CustomerID)
class CustomerIdAsmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(InterestTable)
class InterestTableAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(InterestTableVersion)
class InterestTableAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Transaction)
class InterestTableAdmin(admin.ModelAdmin):
    list_display = ['transaction_id']