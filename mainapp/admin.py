from django.contrib import admin
from .models import *
from django import forms


class CategoryChoiceField(forms.ModelChoiceField):
    pass


class NotebookAdmin(admin.ModelAdmin):
    """
    Class representing choice field for form in notebook adding
    """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return CategoryChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):
    """
    Class representing choice field for form in smartphones adding
    """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return CategoryChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
