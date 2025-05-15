from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'), #main page
    path('puzzle_index/', views.index_json, name='index_json'), #obtain puzzles
    path('puzzles/', views.puzzles, name='puzzles'), #puzzles
    path('game/', views.game, name='game'), #play the game
    path('save/', views.save, name='save'), #save the query
    path('rate_item/', views.rate_item, name='rate_item'), #save the rating
]
