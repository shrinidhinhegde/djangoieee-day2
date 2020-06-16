from django.shortcuts import render
from .models import Portfolio

def home(request):
    db_data = Portfolio.objects.all()
    return render(request, 'index.html', {'data': db_data[0]})
