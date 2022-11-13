from django.contrib import admin

# Register your models here.
from .models import Family #import the Person model
from .models import Animal
# Register your models here.
admin.site.register(Family)
admin.site.register(Animal)

