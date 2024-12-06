from django.db import models # Imports models class so you can create API classes
from django.urls import reverse 
from datetime import date

# Create your models here.

# Import the default User model
from django.contrib.auth.models import User

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


""" 

Limited choices for meals

fields.choices

https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
"""

# A tuple of 2-tuples added above our models
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Cat(models.Model): #References model class, new API schema!
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250) # textField is better for longer text fields
    age = models.IntegerField()
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Override class object nonsense, just return the cat's name
    def __str__(self):
        return self.name
    
    # Method gets the URL for a particular cat instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('cat-detail', kwargs={'cat_id': self.id})
    
# Cats have many feedings
class Feeding(models.Model):
    # The first optional positional argument overrides the label
    date = models.DateField('Feeding date')
    meal = models.CharField( # BLD (Breakfast, Lunch, Dinner)
        max_length=1, 
        # add the 'choices' field option from the MEALS tuple
        choices=MEALS,
        # set the default value for meal to be  Breakfast (B) by accessing tuple index
        default=MEALS[0][0]
    )
    
    # Add foreign key for the cat this feeding belongs to
    # Create a cat_id column for each feeding in the database
    
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE) 
    # This function will prevent the database from rolling into itself if you delete a cat that has feedings, 
    # it deletes the feedings too
    
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
    
    # Define default order of feedings
    class Meta:
        ordering = ['-date']  # Newest feedings appear first