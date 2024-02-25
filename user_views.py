from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect  # たぶん、直前に開いていたページのままにするため
  # 追加してみた1
from user_management.models import Post, Like, Shop, Item, Cart, CartItem, PostCart, PostCartItem 
# 消してみた


def account_view(request):
    request.session['url_tab_latest'] = 'account'
    return render(request, 'account.html')

# 追2

def edit_account_info_view(request):
    return render(request, edit_account_info_view)

# リモートで直接編集してみたよ
