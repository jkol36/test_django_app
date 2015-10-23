from django.shortcuts import render, redirect
from django.contrib import auth
from test_django_app.core.profiles.forms import ProfileCreationForm
from django.contrib import messages
# Create your views here.


def Home(request):
	if request.user.is_authenticated():
		return redirect('Dashboard')
	elif request.POST:
		print request.POST
		form = ProfileCreationForm(request.POST)
		if form.is_valid():
			profile = form.save()
			profile.set_password(request.POST['password'])
			profile.save()
			user = auth.authenticate(username=profile.username, password=request.POST['password'])
			if user:
				auth.login(request, user)
				return redirect("Dashboard")
			else:
				print "no user"
				return render(request, 'home.html', {"auth_error": "Something went wrong", "ProfileCreationForm":ProfileCreationForm})
		else:
			for t,z in form.errors.items():
				print t+z.as_text()
				messages.error(request, t +z.as_text())
	return render(request, 'home.html', {"ProfileCreationForm":ProfileCreationForm})

