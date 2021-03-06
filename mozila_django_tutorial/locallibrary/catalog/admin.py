from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ('date_of_birth', "date_of_death")]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', "due_back")
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


# Register your models here.
#admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)


#admin.site.register(Book)
#admin.site.register(BookInstance)