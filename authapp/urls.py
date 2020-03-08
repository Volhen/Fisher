from django.urls import path, re_path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    # Для масштабирования
    # path('register/$', authapp.register, name='register'),
    # path('update/$', authapp.update, name='update'),
]
