import email
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from accounts.form import UserForm
from accounts.models import Student, Lecturer
from django import forms
# Create your views here.


def index(request):
    return render(request, 'accounts/thankYou.html')


def log_in(request):
    return render(request, 'accounts/LogIn.html')


def signUp(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
       
        if form.is_valid():
          
            if form.data['role'] == 'student':
                
                student = Student(name=form.cleaned_data['name'],email=form.cleaned_data['email'],password = form.cleaned_data['password'])
                student.save()
                return redirect('accounts:thank-you')

            elif form.data['role'] == 'lecturer':
                lecturer = Lecturer()
                return redirect(reverse('accounts:thank-you'))
        
        return render(request, 'accounts/signup.html',{
        'user': form
        })
                    
    return render(request, 'accounts/signup.html',{
        'user': form
    })




def thankyou(request):
    return render(request,"accounts/thankYou.html")