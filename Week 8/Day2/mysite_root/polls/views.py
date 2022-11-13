from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    return render(request, "polls/template/hello.html",)

from .models import Animal, Family

# Create your views here.
def show_family(request, id):
    family_selected = Family.objects.get(id=id)
    return render(request, 'family.html', {'family': family_selected})
def show_animal(request, id):
    animal_selected = Animal.objects.get(id=id)
    return render(request, 'animal.html', {'animal': animal_selected})
def show_animals(request):
    animals = Animal.objects.all()
    return render(request, 'animals.html', {'animal': animals})