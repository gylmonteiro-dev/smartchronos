from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

# Create your views here.
def create_user(request):
    if request.user.is_authenticated and request.user.is_manager:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            registration = request.POST.get('registration')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            user = CustomUser(username=username, registration=registration, first_name=first_name, last_name=last_name)

            user.set_password(password)
            user.save()

            messages.success(request, f'Usuário {first_name}, cadastrado com sucesso')
            return redirect("home")

        return render(request, 'user.html')
    messages.error(request, f"Você não tem permissão para cadastrar usuários")
    return redirect("home")

def login_user_manager(request, register, password):
    user = CustomUser.objects.filter(registration=register).first()

    if user:
        user_authenticated = authenticate(request, username=user.username, password=password)

        # Garantia que o usuário está autenticado e é tem atributo válido de gerente
        if user_authenticated and user.is_manager:
            login(request, user)
            return user
    return None

def logout_user_manager(request):
    logout(request)
    return redirect('home')
