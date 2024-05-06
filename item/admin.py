from django.contrib import admin
from .models import Item, MenuItemExtra, MenuItemExtraItem
# Register your models here.

admin.site.register(Item)
admin.site.register(MenuItemExtra)
admin.site.register(MenuItemExtraItem)


