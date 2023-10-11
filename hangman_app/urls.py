from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default landing page
    path('game/new/', views.new_game, name='new_game'),
    path('game/<int:game_id>/', views.game_state, name='game_state'),
    path('game/<int:game_id>/guess/<str:letter>/', views.guess, name='guess'),
]
