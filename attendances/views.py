from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from accounts.models import CustomUser
from .models import WorkPointRecord

# Create your views here.
def home(request):
    return render(request, 'home.html')

def confirmation(request):
    if request.method == "POST":
        register = request.POST.get("register")
        password = request.POST.get('password')
        
        try:
            # Pegar o usuário
            user = CustomUser.objects.get(registration=register)

            # Verifica a senha se esta errada
            if not user.check_password(password):
                # Inserir mensagem a ser renderizado
                messages.error(request, 'Senha inválida')
                return redirect("home")
            
        except CustomUser.DoesNotExist:
            messages.error(request, 'Usuário não identificado')
            # Inserir mensagem a ser exibido
            return redirect("home")
        
        
        # Retornar o tipo do ultimo ponto
        end_register = WorkPointRecord.objects.filter(user__registration=register).order_by("-created_at").first()
        if end_register:
            end_type = end_register.type_point
        # Caso queira retornar o ultimo registro
            date_time = end_register.created_at
        else:
            end_type = 'Sem registro'
        
        

    return render(request, "confirmation.html", {'user': user, 'end_type': end_type})


def register(request):
    number_registration = request.POST.get('registration')
    # Resgatar o usuário
    user = CustomUser.objects.get(registration=number_registration)

    # Conferir o ultimo registro ponto
    end_register = WorkPointRecord.objects.filter(
        user__registration=number_registration
    ).order_by("-created_at").first()

    # Criar o registro de ponto baseado no ultimo tipo de registro realizado
    if(end_register == None or end_register.type_point == "O"):
        WorkPointRecord.objects.create(user=user, type_point='I')
        messages.success(request, 'Entrada registrada com sucesso')
    else:
        WorkPointRecord.objects.create(user=user, type_point="O")
        messages.success(request, "Saída registrada com sucesso")

    return redirect("home")
