from django.shortcuts import render

def books(request):
    return render(request, "index.html")
