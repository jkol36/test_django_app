from django.shortcuts import render, redirect




def Dashboard(request):
	return render(request, "dashboard.html")