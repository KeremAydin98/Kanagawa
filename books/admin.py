from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):

    model = Book
    list_display = ("title", "author",)


admin.site.register(Book, BookAdmin)
