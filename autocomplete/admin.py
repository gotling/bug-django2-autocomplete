from django.contrib import admin

from .models import Item, LineItem, Category


class LineItemInline(admin.TabularInline):
    model = LineItem
    extra = 1

    autocomplete_fields = ('category',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    inlines = [
        LineItemInline
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

