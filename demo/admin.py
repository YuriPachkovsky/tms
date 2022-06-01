from curses import tigetflag
from django.contrib import admin
from .models import TextPost, Author
from django.utils.safestring import mark_safe
# Register your models here.admin.TabularInline


def set_default_title(modeladmin, request, queryset):
    queryset.update(title='New Title')


class TextPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'mybasecontent', 'created', 'author', 'preview')
    list_filter = ('created', 'author')
    search_fields = ('title', 'content','author__name')
    readonly_fields = ('preview',)
    
    actions = [set_default_title]

    def preview(self, obj):
        if obj.image_content:
            return mark_safe('<img src="{}" width="100" />'.format(obj.image_content.url))
        return mark_safe('<span>No image</span>')

    def mybasecontent(self, obj):
        return obj.base_content()


class inlineTextPost(admin.StackedInline):
    model = TextPost
    extra = 1
    


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    inlines = [inlineTextPost]




admin.site.register(TextPost, TextPostAdmin)
admin.site.register(Author, AuthorAdmin)
