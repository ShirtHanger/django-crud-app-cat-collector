from django.db import models # Imports models class so you can create API classes
from django.urls import reverse 

# Create your models here.


""" 
#More model field types
https://docs.djangoproject.com/en/5.0/ref/models/fields/#model-field-types 
"""

""" 

These field types are important for several reasons:

Validation: Django uses the field types to apply automatic data validation in forms, 
ensuring that data conforms to the expected format before it’s processed or stored.

Form Rendering: The field type also determines the default HTML widget used in forms.

Much easier form creation than react!
"""

class Cat(models.Model): #References model class, new API schema!
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250) # textField is better for longer text fields
    age = models.IntegerField()
    
    # Override class object nonsense, just return the cat's name
    def __str__(self):
        return self.name
    
    # Method gets the URL for a particular cat instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('cat-detail', kwargs={'cat_id': self.id})