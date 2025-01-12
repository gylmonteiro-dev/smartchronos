from django.shortcuts import render, get_object_or_404, redirect
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
        except CustomUser.DoesNotExist:
            # Inserir mensagem a ser exibido
            return redirect("home")
        
        if not user.check_password(password):
            # Inserir mensagem a ser renderizado
            return redirect("home")
        
        # Retornar o tipo do ultimo ponto
        end_register = WorkPointRecord.objects.filter(user__registration=register).order_by("-created_at").first()
        end_type = end_register.type_point
        date_time = end_register.created_at

    return render(request, "confirmation.html", {'user': user, 'end_type': end_type})


def register(request):
    number_registration = request.POST.get('registration')
    # Resgatar o usuário
    user = CustomUser.objects.get(registration=number_registration)

    # Conferir o ultimo tipo de ponto
    end_register = WorkPointRecord.objects.filter(
        user__registration=number_registration
    ).order_by("-created_at").first()


    # Criar o registro de ponto baseado no ultimo tipo de registro realizado
    if(end_register.type_point == None or end_register.type_point == "O"):
        WorkPointRecord.objects.create(user=user, type_point='I')
    else:
        WorkPointRecord.objects.create(user=user, type_point="O")

    return render(request, "home.html")
