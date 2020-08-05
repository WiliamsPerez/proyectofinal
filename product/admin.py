from django.contrib import admin
from .models import Product, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

class ProductAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('name', 'description', 'price', 'product_categories')

	def product_categories(self, obj):
		return ", ".join([c.name for c in obj.categories.all().order_by("name")])
	product_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)