from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, UpdateView
from .models import UserProfile
from .forms import UserProfileForm, ShippingAdressForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ShippingAdressForm

class UserProfileView(DetailView):
    model = UserProfile #model for retrieving data
    template_name = 'user_profile/profile_detail.html' #points to html template for rendering the data
    context_object_name = 'user_profile' #name of the variable to be used in template
    slug_url_kwarg = 'pk' #keyword argument for url


def edit_user_profile(request, user_profile_id):
    user_profile = get_object_or_404(UserProfile, pk=user_profile_id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile:detail', pk=user_profile.pk)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user_profile/profile_update.html', {'form':form, 'user_profile':user_profile})

@login_required
def account(request):
    return render(request, 'user_profile/my_account.html')
"""
def add_shipping_adress(request):
    if request.method == 'POST':
        form = ShippingAdressForm(request.POST)
        if form.is_valid():
            shipping_adress = form.save(commit=False)
            shipping_adress.save()
            form = ShippingAdressForm()
            return render(request, 'user_profile/add_shipping_adress.html', { 'form':form })
        
        else:

            form = ShippingAdressForm()

            return render(request, 'user_profile/add_shipping_adress.html', {'form': form})
"""

def add_shipping_adress(request):
    if request.method == 'POST':
        form = ShippingAdressForm(request.POST)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.save()
            form = ShippingAdressForm()  # Reset the form for a new entry
            return render(request, 'user_profile/shipping_adress_saved.html', {'form': form})

    # If the request method is not POST or the form is not valid, render the form page
    form = ShippingAdressForm()
    return render(request, 'user_profile/add_shipping_adress.html', {'form': form})