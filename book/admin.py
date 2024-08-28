from django.contrib import admin
from django.db.models import F
from .models import Author, Book,Profile,Person
from django.contrib.auth.models import User
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['id','title']
    list_filter = ['authors']
    search_fields = ['authors']
    actions = ['add_pages']

    def add_pages(self, request, queryset):
        updated = queryset.update(pages_count=F('pages_count') + 2)
        self.message_user(
            request, f"{updated} books pages added with two"
        )

    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    sortable_by = ['name']

admin.site.register(Profile)
admin.site.register(Person)

