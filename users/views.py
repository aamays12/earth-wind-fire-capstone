from django.shortcuts import render, redirect
from django.core.mail import send_mail
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
			email = form.cleaned_data.get('email')
			group = form.cleaned_data.get('groups')
			user = form.save()
			user.is_active = False
			user.save()
			user.groups.add(group)
			messages.success(request, f'{username} has sent a request to register. If this is a legitimate user, please activate their account.')
			send_mail('Confirmation email', 'An e-mail has been sent to your Root User. This email will let them know that you have registered. You will receive an e-mail shortly to let you know when your account has been activated.', 'aaronmays423@gmail.com', [email], fail_silently=False)
			send_mail('A user has registered.', str(username)+' has recently registered under their e-mail, '+str(email)+', and is waiting for activation', 'aaronmays423@gmail.com', ['aamays@ualr.edu', 'jpdeer@ualr.edu'], fail_silently=False)
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