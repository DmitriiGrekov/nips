from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")