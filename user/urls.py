from django.urls import include,path

from . import views

app_name = 'users'

urlpatterns = [
    #allauth package include
    #path('',include('allauth.urls')),
    path('login/', views.Account_login.as_view(), name='account_login'),
    path('logout/',views.Account_logout.as_view(),name='account_logout'),
    path('account_information/',views.Account_information.as_view(),name='account_information')
]
