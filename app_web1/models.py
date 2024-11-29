from django.db import models
from django.utils.html import mark_safe

# Create your models here. 
class Pokemon(models.Model):
    TYPE_CHOICES = [
        ('grass', 'Grass'),
        ('fire', 'Fire'),
        ('water', 'Water'),
        ('electric', 'Electric'),
        ('psychic', 'Psychic'),
        ('ice', 'Ice'),
        ('bug', 'Bug'),
        ('rock', 'Rock'),
        ('ghost', 'Ghost'),
        ('dragon', 'Dragon'),
        ('fairy', 'Fairy'),
        ('fighting', 'Fighting'),
        ('normal', 'Normal'),
        ('poison', 'Poison'),
        ('steel', 'Steel'),
        ('dark', 'Dark'),
        ('flying', 'Flying'),
        ('ground', 'Ground')
    ]

    name = models.CharField(max_length=100)
    type_primary = models.CharField(max_length=20, choices=TYPE_CHOICES)
    type_secondary = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True, blank=True)
    number = models.IntegerField()
    gen = models.IntegerField()
    image = models.FileField(upload_to='pokemons/')

    def __str__(self):
        return self.name
    
    def formatted_number(self):
        return str(self.number).zfill(4)
    
    def img(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="width: 50px; height: auto;" />')
        return "No Image"
    
class CustomPokemon(models.Model):
    TYPE_CHOICES = [
        ('grass', 'Grass'),
        ('fire', 'Fire'),
        ('water', 'Water'),
        ('electric', 'Electric'),
        ('psychic', 'Psychic'),
        ('ice', 'Ice'),
        ('bug', 'Bug'),
        ('rock', 'Rock'),
        ('ghost', 'Ghost'),
        ('dragon', 'Dragon'),
        ('fairy', 'Fairy'),
        ('fighting', 'Fighting'),
        ('normal', 'Normal'),
        ('poison', 'Poison'),
        ('steel', 'Steel'),
        ('dark', 'Dark'),
        ('flying', 'Flying'),
    ]

    name = models.CharField(max_length=100)
    type_primary = models.CharField(max_length=20, choices=TYPE_CHOICES)
    type_secondary = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True, blank=True)
    number = models.IntegerField()
    image = models.FileField(upload_to='custom_pokemons/')

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    image = models.FileField(upload_to='games/')


    def __str__(self):
        return self.name
    
    def img(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="width: 50px; height: auto;" />')
        return "No Image"
