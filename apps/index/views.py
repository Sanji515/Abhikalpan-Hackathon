from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
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

@login_required
def dashboard(request):
	complaints = Complaint.objects.all()

	if request.method == 'POST':
		Complaint.objects.create(
			user=request.user,
			title=request.POST['title'],
			meta_description=request.POST['meta_description'],
			description=request.POST['description'])

		result = detect_sensitive_text(request.POST['description'])

		context = {
			'result': result
		}
		return render(request, 'index/dashboard.html', context)

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
	status = 4
	context = {
		'form': form,
		'status': status
	}
	return render(request, 'index/index.html', context)

def LogoutView(request):
	logout(request)
	form = RegistrationForm()
	context = {
		'form':form
	}
	return render(request, 'index/index.html', context)