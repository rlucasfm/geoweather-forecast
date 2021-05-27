from django.shortcuts import render
from django.http import HttpResponse
from .models import Forecast

# Create your views here.
def index(request):
    f = Forecast.objects.order_by('-timestamp')[:1][0]
    data = {
        'cidade': f.cidade,
        'descricao': f.descricao,
        'temperatura': f.temperatura,
        'ultima_atualizacao': f.timestamp
    }
    
    return render(request, 'weather/index.html', data)