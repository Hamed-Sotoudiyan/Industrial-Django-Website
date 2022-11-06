from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def LoginFunction(request):
    if request.method=='POST':
        # if username is not None:
            # if password is not None:
        username_from_template = request.POST.get('username')
        password_from_template = request.POST.get('password')
        user = authenticate(request,username=username_from_template,password=password_from_template)
        if user is not None:
            login(request,user)
            return redirect('Users:Profile')
                # else:
            # else:
        # else:

    return render(request, 'Users/LoginFunction.html')


def Profile(request):
    if request.method=='POST':
        logout(request)
        return redirect('Users:LoginFunction')
    return render(request, 'Users/Profile.html')
