from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "games/index.html")