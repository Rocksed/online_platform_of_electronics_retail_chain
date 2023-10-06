from django.contrib import admin

from .models import FactoryElements, ElementsRetail, ElementsIE


def clear_debt(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0)


clear_debt.short_description = "Очистить задолженность перед поставщиком"


@admin.register(FactoryElements)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name_of_factory', 'country']
    list_filter = ['country']
    actions = [clear_debt]


@admin.register(ElementsRetail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ['retailer_name', 'country', 'supplier']
    list_filter = ['country']
    actions = [clear_debt]


@admin.register(ElementsIE)
class ElementsIEAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'supplier']
    list_filter = ['country']
    actions = [clear_debt]
