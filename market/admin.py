from django.contrib import admin
from .models import Books, Author, Category
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price')
    search_fields = ('name', 'author')
    filter_horizontal = ('category',)


admin.site.register(Books, BooksAdmin)
admin.site.register(Author)
# admin.site.register(CoverType)
admin.site.register(Category)
