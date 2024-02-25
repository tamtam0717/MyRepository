from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect  # たぶん、直前に開いていたページのままにするため
from user_management.models import Post, Like, Shop, Item, Cart, CartItem, PostCart, PostCartItem 
from decimal import Decimal


def account_view(request):
    request.session['url_tab_latest'] = 'account'
    return render(request, 'account.html')
