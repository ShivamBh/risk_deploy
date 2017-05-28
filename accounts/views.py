from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext

from .forms import LoginForm,UserForm, ProfileForm
from .models import Profile

# Create your views here.

def register(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = ProfileForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			registered = True

			return render(request, 'home.html', {})

	else:
		user_form = UserForm()
		profile_form = ProfileForm()
	return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



def user_login(request):
	current_user = request.user

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request, 'home.html', {})
				else :
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid account')
	else:
		form = LoginForm()

	return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('accounts/login/')

def home(request):

	return render(request, 'home.html', {})