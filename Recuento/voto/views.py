from django.shortcuts import render

def resultado_global(request):
    return render(request,'global.html')

def consignas(request):
    return render(request,'consignas.html')
