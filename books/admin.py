from django.contrib import admin

from books.models import Book,Review


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class BookAdmin(admin.ModelAdmin):
    pass