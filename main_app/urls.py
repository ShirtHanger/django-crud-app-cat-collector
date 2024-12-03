from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [ # Routes will be added here
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for cats index
  path('cats/', views.cat_index, name='cat-index'),
]

""" 
The above code defines a root path using an empty string and maps it to the view.home 
view function that does not exist yet - making the server unhappy. 
We’ll remedy this with a new view in the next step.

The name='home' kwarg is technically optional but will come in 
handy for referencing the URL 
in other parts of the app, especially from 
within templates, so we will always use it.
"""
