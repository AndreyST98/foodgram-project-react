from django.contrib import admin

from .models import Ingredient, IngredientAmount, Recipe, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color',)
    list_filter = ('slug',)
    search_fields = ('slug',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)
    search_fields = ('name',)


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'cooking_time',)
    filter_horizontal = ['tags', 'ingredients']
    search_fields = ('name',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientAmount)
admin.site.register(Recipe, RecipesAdmin)
