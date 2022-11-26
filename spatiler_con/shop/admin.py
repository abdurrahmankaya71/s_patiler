from django.contrib import admin
from . models import Shop


@admin.register(Shop)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price') # listeleme - siralama
    list_filter = ('name','price') # filtreleme
    search_fields = ('name', 'price') # arama

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields={'slug':('name',)}

# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     prepopulated_fields={'slug':('name',)}