from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Complaint
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions,EntitiesOptions, RelationsOptions


natural_language_understanding = NaturalLanguageUnderstandingV1(
   version='2018-11-16',
   iam_apikey='sgggLr1OhziffHvNtMnrcXAZdrwlhRdk_khhWV1BFK_o',
   url='https://gateway-fra.watsonplatform.net/natural-language-understanding/api'
)


def recognize(input_text):
    response = natural_language_understanding.analyze(
       text=input_text,
       features=Features(
           entities=EntitiesOptions(model ='73914a25-4c07-4174-923e-74852b373117')))
    return(response.result['entities'])


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
		curr_complaint = Complaint.objects.create(
			user=request.user,
			title=request.POST['title'],
			meta_description=request.POST['meta_description'],
			description=request.POST['description'])

		result = recognize(request.POST['description'])

		context = {
			'result': result,
			'curr_complaint': curr_complaint
		}
		return render(request, 'index/dashboard.html', context)
		
	context = {
		'complaints': complaints
	}
	return render(request, 'index/dashboard.html', context)



def LoginView(request):
	if request.user.is_authenticated:
		return render(request, 'index/dashboard.html', {})
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('index:dashboard')
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