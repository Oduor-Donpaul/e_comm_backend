from typing import Any
from django.db import models
from django.shortcuts import render
from allauth.account.views import SignupView, LoginView, PasswordResetView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import DetailView, UpdateView
from .models import CustomUser
from django.views.generic import TemplateView

class CustomSignupView(SignupView):
    template_name = 'account/signup.html'#path to custom view

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return response

class CustomPasswordResetView(PasswordResetView):
    template_name = 'account/reset_password.html'

class HomePageView(TemplateView):
    template_name = 'account/base.html'



