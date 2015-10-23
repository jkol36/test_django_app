from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.




def logout_view(request):
	auth.logout(request)
	return redirect("Home")
