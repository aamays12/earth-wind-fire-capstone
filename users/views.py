from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import UserRegisterForm

def register(request):
	authenticate = request.user.is_authenticated
	if authenticate:
		return redirect('login_success')
	elif request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			group = form.cleaned_data.get('groups')
			user = form.save()
			user.is_active = False
			user.save()
			user.groups.add(group)
			messages.success(request, f'Account request sent for {username}! Please contact your root_user.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})
	
def login_success(request):

	#Redirects users based on what group they are in
	if request.user.is_staff:
		return redirect("/admin/")
	elif request.user.groups.filter(name="Admin").exists():
		# user is an admin
		return redirect("/adtaa/")
	elif request.user.groups.filter(name="Scheduler").exists():
		# user is a scheduler
		return redirect("/assistant/")