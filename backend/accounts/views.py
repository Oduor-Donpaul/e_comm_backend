from django.shortcuts import render
from allauth.account.views import SignupView, LoginView

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
    
