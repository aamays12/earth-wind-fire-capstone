from django.shortcuts import render, redirect

def assistant(request):
	if request.user.groups.filter(name="Scheduler").exists() or request.user.groups.filter(name="Admin").exists() or request.user.is_staff:
		return render(request, 'assistant/assistant.html')
	else:
		return redirect("/")