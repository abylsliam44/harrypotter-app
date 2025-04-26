from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('houses/', views.houses, name='houses'),  # List of Hogwarts houses
    path('characters/', views.characters, name='characters'),  # List and search characters
    path('characters/<slug:slug>/', views.character_detail, name='character_detail'),  # Character detail view
    path('favorites/', views.favorites, name='favorites'),  # User's favorite characters
    path('chat/<slug:name>/', views.chat_with_character, name='chat_with_character'),  # Chat with a character
    path('quiz/', views.quiz, name='quiz'),  # Harry Potter quiz
]
