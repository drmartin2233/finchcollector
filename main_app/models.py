from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color= models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})


# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    #M:M
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f'{self.name} ({self.id})' 
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add choices field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
        )
    # Create a finch_id FK
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of Field.choice
        return f"{self.get_meal_display()} on {self.date}" 
    
    #changes default sort
    class Meta:
        ordering = ['-date']