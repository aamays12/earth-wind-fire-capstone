from django.shortcuts import render, redirect

def home(request):
	authenticate = request.user.is_authenticated
	if authenticate:
		return redirect('login_success')
	else:
		return render(request, 'home/index.html')