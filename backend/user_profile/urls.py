from django.urls import path
from .views import UserProfileView, edit_user_profile, account
from accounts.views import CustomLoginView

app_name = 'user_profile'

urlpatterns = [
    path('<int:pk>/', UserProfileView.as_view(), name='detail'),
    path('<int:user_profile_id>/edit/', edit_user_profile, name='update'),
    path('account/', account, name='account'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
]