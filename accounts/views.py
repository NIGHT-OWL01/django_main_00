from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
	if request.method=='POST':
		u_name=request.POST.get('username')
		f_name=request.POST.get('first_name')
		l_name=request.POST.get('last_name')
		email=request.POST.get('email')
		pass1=request.POST.get('password1')
		pass2=request.POST.get('password2')

		user=User.objects.create_user(username=u_name,password=pass1,email=email, first_name=f_name,last_name=l_name,)
		user.save();
		
		print('user saved!')
		return redirect('playwithmodels:Home')
	else:
		return render(request, 'accounts/register.html')
def login(request):
	if request.method=='POST':
		u_name=request.POST.get('username')
		password=request.POST.get('password')
		

		user=auth.authenticate(username=u_name,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('playwithmodels:Home')
		else:
			return redirect('accounts:login')
	else:
		return render(request, 'accounts/login.html')

def logout(request):
	if request.method=='GET':
		auth.logout(request)
	return redirect('playwithmodels:Home')
		