from django.contrib import admin
from testing.models import *

# Register your models here.
# outer model
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')


# inner model
class ConstraintsInline(admin.TabularInline):
    extra = 0
    model = Constraints
    list_display = ('id', 'package','city','area','price')

class PriceInline(admin.TabularInline):
    extra = 0
    model = Price
    list_display = ('id', 'package','upper_limit' )

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    inlines = [PriceInline,ConstraintsInline]
    list_display = ('id', 'subcategory','vehicle','partial','capacity')





