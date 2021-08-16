from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models
from .models import ProductImage,Ciudades,Cities
from mptt.admin import MPTTModelAdmin

admin.site.register(Ciudades,MPTTModelAdmin)

class ProductImageInLine(admin.TabularInline):
    model=ProductImage

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    inlines=[ProductImageInLine]