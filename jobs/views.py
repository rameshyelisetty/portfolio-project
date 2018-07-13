from django.shortcuts import render
from .models import Job
# Create your views here.

def jobshome(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'title': 'Jobs Home', 'jobs': jobs, })
