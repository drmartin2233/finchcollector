from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm


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
    # Get toys does not have
    # create list of toy ids finch has
    id_list = finch.toys.all().values_list('id')
    # query for toy ids not in list to exclude
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    #instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have
    })
    
    return render (request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    # special string pattern Django will use
    # success_url = '/finches/{finch_id}' 
    # redirect to index page
    success_url = '/finches'

class FinchUpdate(UpdateView):
    model = Finch
    # disable renaming  by excluding name field
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class ToyList(ListView):
    model = Toy  

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys'

def add_feeding(request, finch_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate
    if form.is_valid():
        # don't save to db till assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)