from django.shortcuts import render
from account.forms import RegistrationForm
from .models import Complaint
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
