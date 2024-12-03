from django.shortcuts import render

# Create your views here.

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

# Now let's define an about page
def about(request):
    # Returns html file from main_app/templates/about.html
    return render(request, 'about.html')