from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mensaje

@login_required
def inbox(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha')
    return render(request, 'messaging/inbox.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request, destinatario_id):
    destinatario = get_object_or_404(User, pk=destinatario_id)
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            Mensaje.objects.create(
                remitente=request.user,
                destinatario=destinatario,
                contenido=contenido
            )
            return redirect('conversacion', user_id=destinatario_id)
    return render(request, 'messaging/enviar.html', {'destinatario': destinatario})

@login_required
def conversacion(request, user_id):
    otro_user = get_object_or_404(User, pk=user_id)
    mensajes = Mensaje.objects.filter(
        remitente=request.user, destinatario=otro_user
    ) | Mensaje.objects.filter(
        remitente=otro_user, destinatario=request.user
    )
    mensajes = mensajes.order_by('fecha')
    return render(request, 'messaging/conversacion.html', {'mensajes': mensajes, 'otro_user': otro_user})
