from django.shortcuts import render

finches = [
    {'name': 'Finneus', 'breed': ' European Goldfinch', 'description': 'Black and yellow', 'age': 3},
  {'name': 'Felicia', 'breed': 'Hawfinch', 'description': 'Black and orange', 'age': 2},
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })