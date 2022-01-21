from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product


# @login_required(login_url='user-login')
# def index(request):
#     return render(request, 'dashboard/index.html')
#
#
# @login_required(login_url='user-login')
# def staff(request):
#     return render(request, 'dashboard/staff.html')
#
#
# @login_required(login_url='user-login')
# def product(request):
#     return render(request, 'dashboard/product.html')
#
#
# @login_required(login_url='user-login')
# def order(request):
#     return render(request, 'dashboard/order.html')

@login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')


@login_required
def product(request):
    return render(request, 'dashboard/product.html')


@login_required
def order(request):
    return render(request, 'dashboard/order.html')