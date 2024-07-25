from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

# Registro
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Enviar e-mail de ativação aqui se necessário
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'registration/login.html')

# Logout
def user_logout(request):
    logout(request)
    return redirect('index')
from .models import InventoryItem
from .forms import InventoryItemForm
from django.shortcuts import get_object_or_404

@login_required
def create_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('index')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/create_item.html', {'form': form})

@login_required
def edit_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk, user=request.user)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InventoryItemForm(instance=item)
    return render(request, 'inventory/edit_item.html', {'form': form})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'inventory/delete_item.html', {'item': item})

@login_required
def view_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    return render(request, 'inventory/view_item.html', {'item': item})
@login_required
def dashboard(request):
    items = InventoryItem.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'items': items})

