from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('enviar/<int:destinatario_id>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('conversacion/<int:user_id>/', views.conversacion, name='conversacion'),
]
