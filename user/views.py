from django.shortcuts import redirect,render
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm

# Create your views here.
#Login function
class Account_login(View):
    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            # ログイン済みだった場合　トップ画面にリダイレクト
            return redirect('/')
        else:
            form = LoginForm(request.POST)
            return render(request,'registration/login.html',{'form':form,})

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request,user)
            return render(request,'home.html')
        response = render(request,'registration/login.html',{'form':form})
        return response


#Logout function
class Account_logout(View):
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            # ログイン済みだった場合
            return self.post(*args,**kwargs)
        else:
            return redirect('/')

    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(request)
        return redirect('home')

class Account_information(View):
    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            # ログイン済みだった場合　トップ画面にリダイレクト
            form = LoginForm(request.POST)
            return render(request, 'account/account.html', {'form': form, })
        else:
            return redirect('/')