from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def confirmation(request):
    if request.method == "POST":
        register = request.POST.get("register")
        password = request.POST.get('password')
        
        return render(request, "confirmation.html")

    return render(request, "confirmation.html")
