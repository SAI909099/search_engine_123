from django.contrib import admin

from apps.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
