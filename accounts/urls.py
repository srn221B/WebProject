
from django.urls import include,path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    #allauth package include
    path('',include('allauth.urls')),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'),name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),name='password_change_done'),
    path('signup_account/',views.SignupView.as_view(),name='account_signup')
]
