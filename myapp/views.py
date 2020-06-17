from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    if not request.user.is_superuser:
        return render(request, 'home.html')
    else:
        return redirect('/admin/')