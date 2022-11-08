from django.contrib.auth import forms
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import messages
from .forms import CadastroUser, LoginUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='login')
def home(request):
    return render(request, 'page/index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        print(f'{username} --- {password1}')
        user = authenticate(request, username=username, password=password1)

        if(user):
            print('tá chegando aq????')
            login(request, user)
            return redirect('home')

    form = LoginUser()
    context = {'form':form}
    return render(request, 'page/login.html', context)


def cadastro(request):

    if request.method == "POST":
        form = CadastroUser(request.POST)
        if form.is_valid():

            form.save()
            print("Cadastro feito...")
            return redirect('login')

    form = CadastroUser()
    context = {'form':form}
    return render(request, 'page/form.html', context)


