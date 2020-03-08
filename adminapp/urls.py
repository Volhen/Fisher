from django.urls import path
import adminapp.views as adminapp


app_name = 'adminapp'


urlpatterns = [
    path('', adminapp.index, name='index'),
    path('shopuser/create/', adminapp.shopuser_create, name='shopuser_create'),
    path('shopuser/update/<int:pk>/', adminapp.shopuser_update, name='shopuser_update'),
    path('shopuser/delete/<int:pk>/', adminapp.shopuser_delete, name='shopuser_delete'),
    path('shopuser/recover/<int:pk>/', adminapp.shopuser_recover, name='shopuser_recover'),

    path('categories/', adminapp.categories, name='categories'),
    path('productcategory/create/', adminapp.productcategory_create, name='productcategory_create'),
    path('productcategory/update/<int:pk>', adminapp.productcategory_update, name='productcategory_update'),
    path('productcategory/delete/<int:pk>', adminapp.productcategory_delete, name='productcategory_delete'),
    path('productcategory/recover/<int:pk>', adminapp.productcategory_recover, name='productcategory_recover'),

    path('products/<int:pk>/', adminapp.products, name='products'),
    path('products/create/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),
    path('products/recover/<int:pk>/', adminapp.product_recover, name='product_recover'),
    

    
]
