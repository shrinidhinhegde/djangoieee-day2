from django.shortcuts import render

def home(request):
    name = 'Changed'
    return render(request, 'index.html', {'name100': name})

def result(request):
    num_1 = int(request.POST.get('num1'))
    num_2 = int(request.POST.get('num2'))
    total = num_1+num_2
    return render(request, 'result.html', {'tot': total})
