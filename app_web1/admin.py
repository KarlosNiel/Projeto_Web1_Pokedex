from django.contrib import admin
from app_web1.models import Pokemon, Game

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_primary', 'type_secondary', 'number', 'gen', 'img')
    search_fields = ('name', 'type_primary', 'type_secondary', 'number', 'gen')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'img')
    search_fields = ('name', 'description', 'release_date')  