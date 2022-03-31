from django.shortcuts import render

# Create your views here.


def index(req):
    my_dict = {'user_name': "Roni Jack Vituli", 'email': "Roni@gmail.com"}
    return render(req, 'index.html', context=my_dict)
