from django.shortcuts import render

# Import Class Based View CRUD stuff
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Import Cat Model
from .models import Cat

# Create your views here.

# Import HttpResponse to send text-based responses
# Obeslete when you make a proper home page
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Returns main_app/templates/home.html
    return render(request, 'home.html')

# Now let's define an about page
def about(request):
    # Returns html file from main_app/templates/about.html
    return render(request, 'about.html')

# INDEX PAGE
def cat_index(request):
    # Render the cats/index.html template with the cats data
    # Turns it into a dictionary with a single key, 'cats'
    cats = Cat.objects.all()  # look familiar?
    return render(request, 'cats/index.html', {'cats': cats})

# SHOW PAGE
def cat_detail(request, cat_id): # Grabs a specific cat by Django ID
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})



""" THese will automatically handle CRUD form logic! """
class CatCreate(CreateView):
    model = Cat
    fields = '__all__' # Shows form of all properties
    # This works too but above is more efficient.
    # fields = ['name', 'breed', 'description', 'age']
    
class CatUpdate(UpdateView):
    model = Cat
    # Disallow renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'