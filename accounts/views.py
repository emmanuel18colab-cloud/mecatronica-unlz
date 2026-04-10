from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import RegistroForm, PerfilForm
from .models import Perfil

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(usuario=user)
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})

@login_required
def perfil_view(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    return render(request, 'accounts/perfil.html', {'perfil': perfil})

@login_required
def perfil_edit(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil, user=request.user)
        if form.is_valid():
            form.save()
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil, user=request.user)
    return render(request, 'accounts/perfil_edit.html', {'form': form})

@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña cambiada correctamente')
            return redirect('perfil')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/cambiar_password.html', {'form': form})
