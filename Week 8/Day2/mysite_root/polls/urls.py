from django.urls import path,include #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('family/<int:id>', views.show_family, name='family'), 
    path('animals/<int:id>', views.show_animals, name='animals'),
    path('animal', views.show_animal, name='animal')
]

