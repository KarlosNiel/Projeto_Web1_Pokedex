from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from app_web1.models import Pokemon, CustomPokemon, Game


class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'  


class IndexView(LoginRequiredMixin, TemplateView):
    model = Pokemon
    template_name = 'index.html' 
    context_object_name = 'pokemons'
    login_url = 'login'

    

    def dispatch(self, request, *args, **kwargs):
        # Impedir que a página index seja armazenada em cache
        response = super().dispatch(request, *args, **kwargs)
        response['Cache-Control'] = 'no-store'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemons'] = Pokemon.objects.all().order_by('number')
        context['generations'] = list(range(1, 10))
        return context
    
class CustomPokemonView(LoginRequiredMixin, ListView):
    model = CustomPokemon
    queryset = CustomPokemon.objects.all()

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response['Cache-Control'] = 'no-store'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemons'] = CustomPokemon.objects.all().order_by('number')
        context['generations'] = list(range(1, 10))
        return context
    
class CustomPokemonCreate(LoginRequiredMixin, CreateView):
    model = CustomPokemon
    fields = '__all__'
    success_url = reverse_lazy('app_web1:list')
    
class CustomPokemonUpdate(LoginRequiredMixin, UpdateView):
    model = CustomPokemon
    fields = '__all__'
    success_url = reverse_lazy('app_web1:list')

class CustomPokemonDelete(LoginRequiredMixin, DeleteView):
    queryset = CustomPokemon.objects.all()
    success_url = success_url = reverse_lazy('app_web1:list')

class GamesView(LoginRequiredMixin, ListView):
    model = Game
    queryset = Game.objects.all()
    paginate_by = 6
    

    def dispatch(self, request, *args, **kwargs):
        # Impedir que a página index seja armazenada em cache
        response = super().dispatch(request, *args, **kwargs)
        response['Cache-Control'] = 'no-store'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.all().order_by('release_date')
        return context
    
class GameDetailView(LoginRequiredMixin, DetailView):
    model = Game
    queryset = Game.objects.all()

