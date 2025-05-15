from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('temp/', views.index, name='index2'),
    path('puzzle_index/', views.index_json, name='index_json'),
    path('puzzles/', views.puzzles, name='puzzles'),
    path('game/', views.game, name='game'),
    path('save/', views.save, name='save'),
    path('rate_item/', views.rate_item, name='rate_item'),
]
