from django.shortcuts import render, redirect

# Import Class Based View CRUD stuff
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Import Cat Model
from .models import Cat
# Import form for new feedings for cat
from .forms import FeedingForm

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
    
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    
    # Return both singular cat and all feedings associated with singular cat
    return render(request, 'cats/detail.html', {
        # include the cat and feeding_form in the context
        'cat': cat, 'feeding_form': feeding_form
    })
    
# CREATE FEEDING METHOD

def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST) # Captures feeding data, preps for database
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)




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