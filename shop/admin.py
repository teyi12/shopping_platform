from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        # Führen Sie benutzerdefinierte Logik vor dem Löschen aus
        print(f"Produkt wird gelöscht: {obj.name}")
        super().delete_model(request, obj)



admin.site.register(Category)
