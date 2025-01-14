from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

# Create your views here.
def create_user(request):
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