from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from authapp.models import FishUser
from mainapp.models import ProductCategory, Product
from adminapp.forms import(FishUserCreationAdminForm, 
                           FishUserUpdateAdminForm, 
                           FishUserCreationAdminForm, 
                           ProductCategoryEditForm,
                           ProductEditForm)

# ****************************************shopuser
@user_passes_test(lambda x: x.is_superuser)
def index(request):
    users_list = FishUser.objects.all().order_by('-is_active', '-is_superuser',
                                                 '-is_staff', 'username')
    context = {
        'title': 'админка/пользователи',
        'object_list': users_list
    }

    return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda x: x.is_superuser)
def shopuser_create(request):
    if request.method == 'POST':
        form = FishUserCreationAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = FishUserCreationAdminForm()
    context = {
        'title': 'пользователи/создание',
        'form': form
    }
    return render(request, 'adminapp/shopuser_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def shopuser_update(request, pk):
    current_user = get_object_or_404(FishUser, pk=pk)
    if request.method == 'POST':
        form = FishUserUpdateAdminForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = FishUserUpdateAdminForm(instance=current_user)
    context = {
        'title': 'пользователи/редактирование',
        'form': form
    }
    return render(request, 'adminapp/shopuser_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def shopuser_delete(request, pk):
    current_object = get_object_or_404(FishUser, pk=pk)
    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        current_object.is_active = False
        current_object.save()
        return HttpResponseRedirect(reverse('myadmin:index'))
    context = {
        'title': 'пользователи/удаление',
        'user_to_delete': current_object
    }
    return render(request, 'adminapp/shopuser_delete.html', context)


@user_passes_test(lambda x: x.is_superuser)
def shopuser_recover(request, pk):
    current_object = get_object_or_404(FishUser, pk=pk)
    if request.method == 'POST':
        current_object.is_active = True
        current_object.save()
        return HttpResponseRedirect(reverse('myadmin:index'))
    context = {
        'title': 'пользователи/восстановить',
        'user_to_recover': current_object
    }
    return render(request, 'adminapp/shopuser_recover.html', context)


# ****************************************category
@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    object_list = ProductCategory.objects.all().order_by('-is_active', 'name')
    context = {
        'title': 'админка/категории',
        'object_list': object_list
    }
    return render(request, 'adminapp/category_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def productcategory_create(request):
    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:categories'))
    else:
        form = ProductCategoryEditForm()
    context = {
        'title': 'категории/создание',
        'form': form
    }
    return render(request, 'adminapp/productcategory_form.html', context)


@user_passes_test(lambda x: x.is_superuser)
def productcategory_update(request, pk):
    current_object = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES, instance=current_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:categories'))
    else:
        form = ProductCategoryEditForm(instance=current_object)
    context = {
        'title': 'категории/редактирование',
        'form': form
    }
    return render(request, 'adminapp/productcategory_form.html', context)


@user_passes_test(lambda x: x.is_superuser)
def productcategory_delete(request, pk):
    current_object = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        current_object.is_active = False
        current_object.save()
        return HttpResponseRedirect(reverse('myadmin:categories'))
    context = {
        'title': 'категории/удаление',
        'object': current_object
    }
    return render(request, 'adminapp/productcategory_delete.html', context)


@user_passes_test(lambda x: x.is_superuser)
def productcategory_recover(request, pk):
    current_object = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        current_object.is_active = True
        current_object.save()
        return HttpResponseRedirect(reverse('myadmin:categories'))
    context = {
        'title': 'товары/восстановить',
        'object': current_object,
    }
    return render(request, 'adminapp/product_category_recover.html', context)

# ****************************************products
@user_passes_test(lambda x: x.is_superuser)
def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    object_list = category.product_set.all().order_by('-is_active', 'name')
    context = {
        'title': 'админка/продукт',
        'category': category,
        'object_list': object_list
    }
    return render(request, 'adminapp/product_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_create(request,pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:products',kwargs={'pk': pk}))
    else:
        form = ProductEditForm(initial={'category': category})
    context = {
        'title': 'товары/создание',
        'form': form,
        'category': category
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_update(request, pk):
    product_object = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:products',
                                                kwargs={'pk': product_object.category.pk}))
    else:
        form = ProductEditForm(instance=product_object)
    context = {
        'title': 'товары/редактирование',
        'form': form,
        'category': product_object.category
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_delete(request, pk):
    product_object = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product_object.is_active = False
        product_object.save()
        return HttpResponseRedirect(reverse('myadmin:products',
                                            kwargs={'pk': product_object.category.pk}))
    context = {
        'title': 'товары/удаление',
        'object': product_object,
        'category': product_object.category
    }
    return render(request, 'adminapp/product_delete.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_recover(request, pk):
    current_object = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        current_object.is_active = True
        current_object.save()
        return HttpResponseRedirect(reverse('myadmin:products',
                                                kwargs={'pk': current_object.category.pk}))
    context = {
        'title': 'товары/восстановить',
        'object': current_object,
        'category': current_object.category
    }
    return render(request, 'adminapp/product_recover.html', context)