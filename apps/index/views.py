from django.shortcuts import render
from account.forms import RegistrationForm
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index:index');

	else:
		form = RegistrationForm()

	context = {
		'form': form
	}
	return render(request, 'index/index.html', context)


def dashboard(request):

	return render(request, 'index/dashboard.html', {})
