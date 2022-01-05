<<<<<<< HEAD
import requests
from django.shortcuts import render


# Create your views here.

def hello(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()
    print(users)

    return render(request , 'home/consumir-api.html', {'users' : users})

def home(request):
    return render(request, 'home/index.html')
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
