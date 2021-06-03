from django.contrib import admin
from .models import products
from .models.category import Category
from .models.customer import Customer


# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(products.Product , AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)


