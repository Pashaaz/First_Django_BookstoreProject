from django.contrib import admin

from Books.models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'isbn_code')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
