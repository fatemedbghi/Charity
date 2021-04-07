from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User

def about_us(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'about_us.html', context=context)