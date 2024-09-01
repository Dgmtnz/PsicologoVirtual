from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('send_message/', views.send_message, name='send_message'),
    path('speech_to_text/', views.speech_to_text, name='speech_to_text'),
    path('text_to_speech/', views.text_to_speech, name='text_to_speech'),
    path('end_day/', views.end_day, name='end_day'),
]