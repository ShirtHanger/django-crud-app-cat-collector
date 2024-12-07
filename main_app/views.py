from django.shortcuts import render, redirect
# Import login functionality
from django.contrib.auth.views import LoginView
# Import Class Based View CRUD stuff
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Default view templates
from django.views.generic import ListView, DetailView

# For login-signup stuff
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# For login protected routes
from django.contrib.auth.decorators import login_required 
# Import the mixin for class-based view protection
from django.contrib.auth.mixins import LoginRequiredMixin

# Import Cat Model
from .models import Cat, Toy
# Import form for new feedings for cat
from .forms import FeedingForm

# Create your views here.

# Import HttpResponse to send text-based responses
# Obeslete when you make a proper home page
from django.http import HttpResponse

# Define the home view function
class Home(LoginView):
    # Returns main_app/templates/home.html
    template_name = 'home.html'

# Now let's define an about page
def about(request):
    # Returns html file from main_app/templates/about.html
    return render(request, 'about.html')

""" CATS PAGES """

# INDEX PAGE
""" 
def cat_index(request): # Shows ALL cats in database
    # Render the cats/index.html template with the cats data
    # Turns it into a dictionary with a single key, 'cats'
    cats = Cat.objects.all()  # look familiar?
    return render(request, 'cats/index.html', {'cats': cats})
 """

@login_required
def cat_index(request): # Shows just the logged user's cats
    cats = Cat.objects.filter(user=request.user)
    # You could also retrieve the logged in user's cats like this
    # cats = request.user.cat_set.all()
    return render(request, 'cats/index.html', { 'cats': cats })

# SHOW PAGE
@login_required
def cat_detail(request, cat_id): # Grabs a specific cat by Django ID
    cat = Cat.objects.get(id=cat_id)
    
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id')) # Fetch toys this cat DOESNT have
    
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    
    return render(request, 'cats/detail.html', {
        'cat': cat, # Get specific cat
        'feeding_form': feeding_form, # Get all feedings associated with specific cat
        'toys': toys_cat_doesnt_have # Get all toys that DONT belong to this cat
    })
    
# ADD A FEEDING METHOD
@login_required
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


# SIGN UP FUNCTIONALITY
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in and redirect them
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
    # In Javascript


""" These will automatically handle CRUD form logic! """
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    # fields = '__all__' # Shows form of all properties, including owned user
    # This works too but above is more efficient...
    # But since there are users and toys, we need to hide the "User" and "Toys " properties
    fields = ['name', 'breed', 'description', 'age']
    
    # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
        # Automatically assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    
class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    # Disallow renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = '/cats/'
    
""" Toy list styles """
    
class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy
    
# Toy CRUD

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'

# Cat-Toy association and removal
@login_required
def associate_toy(request, cat_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)

@login_required
def remove_toy(request, cat_id, toy_id):
    # Look up the cat
    # Look up the toy
    # Remove the toy from the cat
    Cat.objects.get(id=cat_id).toys.remove(toy_id)
    return redirect('cat-detail', cat_id=cat_id)
