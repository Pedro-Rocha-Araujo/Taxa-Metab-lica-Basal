from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'app_tmb/home.html')

def resultado(request):
    Usuario.objects.all().delete()
    
    novo_usuario = Usuario() 
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.altura = request.POST.get('altura')
    novo_usuario.peso = request.POST.get('peso')
    novo_usuario.sexo = request.POST.get('sexo')

    peso = float(novo_usuario.peso)
    altura = float(novo_usuario.altura)
    idade = int(novo_usuario.idade)

    if(novo_usuario.sexo == "Masculino"):
        novo_usuario.kcal = (88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade))
    if(novo_usuario.sexo == "Feminino"):
        novo_usuario.kcal = ((10 * peso) + (6.25 * altura) - (5 * idade) - 161)

    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'app_tmb/resultado.html', usuarios)
    