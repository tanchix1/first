from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    #thepassword = 'testing'
    characters = list("abcdefghlmnopqrst")
    length = int(request.GET.get('lenght'))
    #global thepassword
    thepassword = ""
    if request.GET.get("uppercase"):
        characters.extend("ABCDEFGHLMNOPQRSTWYXZ")

    if request.GET.get("numbers"):
        characters.extend("0123456789")

    if request.GET.get("simbols"):
        characters.extend("!@#$%^&*()")

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})
def information(request):
    return render(request, 'generator/information.html')
