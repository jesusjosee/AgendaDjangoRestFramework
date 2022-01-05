from django.contrib import admin

<<<<<<< HEAD
from .models import Hobby, Person, Reunion
=======
from .models import Person, Hobby, Reunion
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c

admin.site.register(Person)
admin.site.register(Hobby)
admin.site.register(Reunion)
