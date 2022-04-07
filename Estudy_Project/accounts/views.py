from django.shortcuts import render
from accounts.forms import NewStudentForm

# Create your views here.


def index(req):
    print("Hey hey hey")
    return render(req, 'accounts/thankYou.html')


def log_in(req):
    return render(req, 'accounts/LogIn.html')


def signUp(req):
    form = NewStudentForm()
    if req.method == 'POST':
        fullName = req.POST['name']
        email = req.POST['email']
        password = req.POST['pass']
        verify_pass = req.POST['re_pass']

        data = {'fullname': fullName,
                'email': email,
                'password': password,
                'verify_pass': password,
                }
        print(data)
        print("\n\n\n\n\n\n\n")
        if form.is_valid():
            form.save(commit=True)
            print("SUCCSESS")
            return index(req)
        else:
            print("ERROR!")

    return render(req, 'accounts/signup.html', {'form': form})
