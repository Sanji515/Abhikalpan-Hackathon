from django.shortcuts import render
from accounts.forms import RegistrationForm
# Create your views here.

def index(request):

	return render(request, 'index/index.html', {})


def dashboard(request):

	return render(request, 'index/dashboard.html', {})


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/index');

	else:
		form = RegistrationForm()
		args = {'form':form}
		return render(request, 'index/index.html', args) ;
