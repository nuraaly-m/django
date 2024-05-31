from django.contrib import admin

from cloth.models import Cloth,TagCloth


# Register your models here.

@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    pass

@admin.register(TagCloth)
class TagClothAdmin(admin.ModelAdmin):
    pass
