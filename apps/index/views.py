from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from .models import Complaint
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			status = 2 
			context = {
				'status' : status,
				'form': form
			}
			return render(request, 'index/index.html', context);
		else:
			status = 3
			context = {
				'form': form,
				'status': status
			}
			return render(request, 'index/index.html', context)

	else:
		form = RegistrationForm()
	context = {
		'form': form
	}
	return render(request, 'index/index.html', context)


def dashboard(request):
	complaints = Complaint.objects.all()
	print('asdsa',complaints)
	context = {
		'complaints': complaints
	}
	return render(request, 'index/dashboard.html', context)



def LoginView(request):
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, 'index/dashboard.html', {})
	form = RegistrationForm()
	context = {
		'form': form
	}
	return render(request, 'index/index.html', context)