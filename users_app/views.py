from ast import Return
import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(req):
    user_name = "Roni Jack Vituli"
    email = "Roni@gmail.com"
    add = "Gome 15"
    my_dict = {'user_name': user_name, 'email': email, 'address': add}
    return render(req, 'index.html', context=my_dict)


def help(req):
    user = "Roni"
    my_dict = {'name': user}
    return render(req, 'help.html', context=my_dict)
