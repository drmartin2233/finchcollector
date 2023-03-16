from django.shortcuts import render
from .models import Finch
# finches = [
#     {'name': 'Finneus', 'breed': ' European Goldfinch', 'description': 'Black and yellow', 'age': 3},
#   {'name': 'Felicia', 'breed': 'Hawfinch', 'description': 'Black and orange', 'age': 2},
# ]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    print(finches)
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render (request, 'finches/detail.html', { 'finch': finch })