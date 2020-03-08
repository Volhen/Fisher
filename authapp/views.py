from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import FishUserLoginForm, FishUserRegisterForm, FishUserEditForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST':
        form = FishUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        auth.logout(request)
        form = FishUserLoginForm()

    context = {
        'title': 'вход в систему',
        'form': form,
        'next': next
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


# Для масштабирования
# def register(request):
#     if request.method == 'POST':
#         form = FishUserRegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('auth:login'))
#     else:
#         form = FishUserRegisterForm()

#     context = {
#         'title': 'регистрация',
#         'form': form
#     }

#     return render(request, 'authapp/register.html', context)


# def update(request):
#     if request.method == 'POST':
#         form = FishUserEditForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('auth:update'))
#     else:
#         form = FishUserEditForm(instance=request.user)

#     context = {
#         'title': 'редактирование',
#         'form': form
#     }

#     return render(request, 'authapp/update.html', context)
