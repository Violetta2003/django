from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from user.forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse



def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('OK')
                else:
                    return HttpResponse('Not OK')
            else:
                return HttpResponse('Неверные данные')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'data': LoginForm()})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return HttpResponse('OK')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'user/register.html', {'data': user_form})