from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, UpdateView
from .models import UserProfile
from .forms import UserProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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