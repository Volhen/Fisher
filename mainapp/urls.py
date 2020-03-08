from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.index, name='index'),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('blog/', mainapp.blog, name='blog'),
    path('about/', mainapp.about, name='about'),
]