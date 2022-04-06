from django.contrib import admin
from .models import Book, Comment

class CommentAdmin(admin.TabularInline):

    model = Comment

class BookAdmin(admin.ModelAdmin):

    model = Book
    inlines = [
        CommentAdmin
    ]
    list_display = ("title", "author",)


admin.site.register(Book, BookAdmin)
