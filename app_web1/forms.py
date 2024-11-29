from django import forms 
from .models import CustomPokemon, Game

class CustomPokemonForm(forms.ModelForm):
    class Meta:
        model = CustomPokemon 
        fields = '__all__' 

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'  