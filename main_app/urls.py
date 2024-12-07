from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [ # Routes will be added here
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    
    # Cat display routes
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'), # Cat details, collects by ID.
    
    # Cat CRUD routes
    # CRUD form logic is handled automatically by Django
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'), # Create a cat on user end, 
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'), # Update
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'), # Delete
    
    # Cat feedings route
    path(
    'cats/<int:cat_id>/add-feeding/', 
    views.add_feeding, 
    name='add-feeding'
    ),
    
    # Toy display routes
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    path('toys/', views.ToyList.as_view(), name='toy-index'),
    
    # Toy CRUD routes
    path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
    
    # Cat-Toy Association/removal routes
    path('cats/<int:cat_id>/associate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),
    path('cats/<int:cat_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove-toy'),


    

    
    # Sign up route
    path('accounts/signup/', views.signup, name='signup'),

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
