from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import CustomUser
from accounts.views import login_user_manager
from attendances.models import WorkPointRecord
from django.urls import reverse
# Create your views here.


def employee_list(request):
    list_employees = CustomUser.objects.all()
    return render(request, 'employee_list.html', {'list_employees': list_employees})

def list_time_records(request, pk):
    user = CustomUser.objects.get(pk=pk)
    last_records = WorkPointRecord.objects.filter(user__pk=pk).order_by('-created_at')[:5]
    
    return render(request, 'time_records_list.html', {'last_records': last_records, 'user': user})

def record_point_validation(request, pk):
    point_record = get_object_or_404(WorkPointRecord, pk=pk)
    point_record.valid = True
    point_record.save()
    messages.success(request, 'Registro validado com sucesso!')
    user_pk = point_record.user.id
    return redirect(reverse("list-time-records", args=[user_pk]))

def record_point_delete(request ,pk):
    point_record = get_object_or_404(WorkPointRecord, pk=pk)
    user_pk = point_record.user.id
    point_record.delete()
    messages.success(request, 'Registro deletado com sucesso!')
    return redirect(reverse("list-time-records", args=[user_pk]))

def record_point_update(request, pk): 
    point_record = get_object_or_404(WorkPointRecord, pk=pk)
    user_pk = point_record.user.id
    date_str = request.POST.get('date')
    time_str = request.POST.get('time')
    print(date_str, time_str)
    
    # Aqui a lógica para atualizar com base nos dados que vem do formulário a data e em seguida o horário
    if date_str and time_str:
        new_datetime_str = f'{date_str} {time_str}'
        new_datetime = datetime.strptime(new_datetime_str, "%Y-%m-%d %H:%M")
        

        point_record.update_at = new_datetime - timedelta(hours=3)
        point_record.save()
    
    return redirect(reverse("list-time-records", args=[user_pk]))


def dashboard_view(request):
    register = request.POST.get("register")
    password = request.POST.get("password")
    five_last_records = WorkPointRecord.objects.all().order_by('-created_at')[:5]
    
    if request.method == 'POST':
        user = login_user_manager(request=request, register=register, password=password)
        if user:
            return render(
                request,
                "dashboard_control.html",
                {"page": "dashboard", "last_records": five_last_records},
            )
        else:
            messages.error(request,'Credenciais ou permissão inválida')
            return redirect('home')

    # Condição para um get via endereço
    if not request.user.is_authenticated:
        messages.error(request,'Você precisa estar logado')
        return redirect('home')
    
    # Renderiza em um get se tiver um user logado, pois já passou nas validações acima
    return render(
        request,
        "dashboard_control.html",
        {"page": "dashboard", "last_records": five_last_records},
    )

    # return render(
    #     request,
    #     "dashboard_control.html",
    #     {"page": "dashboard", "last_records": five_last_records},
    #

    # if request.method == "POST":
    #     try:
    #         user = CustomUser.objects.get(registration=register)
    #         # Pegar o usuário

    #         # Verifica a senha se esta errada
    #         if not user.check_password(password):
    #             # Se a senha for incorreta,
    #             # Inserir mensagem a ser renderizado
    #             messages.error(request, "Senha inválida")
    #             return redirect("home")

    #         # Verificar se é gerente
    #         if not user.is_manager:
    #             messages.error(request, "Perfil sem permissão")
    #             return redirect("home")

    #         # Pegar os ultimos 5 registros do dia
    #         five_last_records = WorkPointRecord.objects.all()[:5]

    #         # Tudo dando certo retornará
    #         return render(request, "dashboard_control.html", {'page': 'dashboard', 'last_records': five_last_records})

    #     except CustomUser.DoesNotExist:
    #         messages.error(request, "Usuário não identificado")
    #         # Inserir mensagem a ser exibido
    #         return redirect("home")

    # # Garantir que tenha o usuário para entrar nesta poágina, caso queira acessar pela URL no método GET
    # try:
    #     user_registrado = CustomUser.objects.get(registration=register)
    #     if user_registrado:
    #         return render(request, "dashboard_control.html", {'page':'dashboard'})

    # except CustomUser.DoesNotExist:
    #     messages.error(request, "Necessário informar suas credenciais")
    #     # Inserir mensagem a ser exibido
    #     return redirect("home")


def filter_record_by_date(request):
    start_date = request.POST.get('startDate')
    end_date = request.POST.get('endDate')
    register = request.POST.get('register')

    user = CustomUser.objects.get(registration=register)
    records_user = user.point_records.all()

    # records_filtred = records_user.filter(created_at__range=(start_date, end_date))
    
    print(start_date, end_date, register)
    return render(request, 'filter_time_records_list.html')
