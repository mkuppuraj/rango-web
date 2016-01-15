from django.contrib import admin

from rango.models import Category, Page


class RangoPageAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'url')


class RangoCategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'views', 'likes')


admin.site.register(Category, RangoCategoryAdmin)
admin.site.register(Page, RangoPageAdmin)
