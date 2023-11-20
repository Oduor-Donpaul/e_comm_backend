from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required

app_name = 'account'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    #path('login/', CustomLoginView.as_view(), name='account_login'),
    #path('password_change/', login_required(PasswordChangeView.as_view()), name='password_change'),
]
   