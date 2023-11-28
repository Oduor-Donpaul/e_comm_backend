"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import  CustomLoginView, CustomSignupView, CustomPasswordResetView
from accounts.views import HomePageView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from products.views import home, product_datail
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import blog_page, blog_detail
from user_profile.views import add_shipping_adress

app_name = 'profile'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('user_profile/', include('user_profile.urls')),
    path('accounts/password/reset/', CustomPasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('', home, name='home' ),
    path('password_change/', login_required(PasswordChangeView.as_view()), name='password_change'),
    path('product/<int:product_id>/', product_datail, name='product_datail'),
    path('blogs/', blog_page, name='blog_page'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('add_shipping_adress/', add_shipping_adress, name='add_shipping_adress'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)