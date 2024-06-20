from library.models import *
from django.contrib import admin


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn", "qty", "price" )


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("book", "qty", "price", "total_price", "created_at")
    readonly_fields = ("price", "total_price")


# admin.register(Book, BookAdmin)
# admin.site.register(Book)
from django.contrib import admin

# Register your models here.
