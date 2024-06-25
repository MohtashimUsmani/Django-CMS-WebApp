from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filter import OrderFilter
from .models import Customer, Product, Tag, Order
from .forms import OrderForm, CreteUserForm, CustomerForm, ProductForm
from .decorators import unauthenticated_user, allowed_users, admin_only


@login_required(login_url='loginPage')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customer = customers.count()
    total_orders = orders.count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='pending').count()
    contex = {'orders': orders, 'customers': customers, 'total_customer': total_customer,
              'total_orders': total_orders, 'delivered': delivered, 'pending': pending
              }
    return render(request, 'dashboard.html', contex)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admins'])
def products(request):
    products = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'products': products, 'form': form}
    return render(request, 'products.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admins'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    contex = {'customer': customer, 'orders': orders, 'order_count': order_count, 'myFilter': myFilter}
    return render(request, 'customer.html', contex)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admins'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request, 'order_form.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admins'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'order_form.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admins'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'delete.html', context)


@unauthenticated_user
def register(request):
    form = CreteUserForm()
    if request.method == 'POST':
        form = CreteUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Register Successfully: ' + username)
            return redirect('loginPage')

    context = {'form': form}
    return render(request, 'registerPage.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'loginPage.html', context)


def logoutuser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customers'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()

    context = {'orders': orders, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending, 'customer':customer}
    return render(request, 'user.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customers'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'account_setting.html', context)