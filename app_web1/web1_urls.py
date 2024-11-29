from django.urls import path, include
from app_web1 import views

app_name = 'app_web1'

urlpatterns = [
    path('', views.CustomPokemonView.as_view(), name='list'),
    path('create/', views.CustomPokemonCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.CustomPokemonUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.CustomPokemonDelete.as_view(), name='delete'),

    path('games/', include([
        path('', views.GamesView.as_view(), name='game_list'),
        path('detail/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    ]))
]
