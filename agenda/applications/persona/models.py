#
<<<<<<< HEAD
from re import VERBOSE
from model_utils.models import TimeStampedModel
#
from django.db import models

class Hobby(TimeStampedModel):
    """ Modelo para registrar pasatiempos """

    hobby = models.CharField(verbose_name='Pasa tiempo', max_length=50)
=======
from model_utils.models import TimeStampedModel
#
from django.db import models
#
from .managers import ReunionManager

#
class Hobby(TimeStampedModel):
    """  pasa tiempos  """
    hobby = models.CharField(
        'Pasa tiempo', 
        max_length=50,
    )
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c

    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'
<<<<<<< HEAD

    def __str__(self):
        return self.hobby
    


#
=======
    
    def __str__(self):
        return self.hobby



>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )
    hobbies = models.ManyToManyField(Hobby)

<<<<<<< HEAD

=======
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.full_name

<<<<<<< HEAD
class Reunion(TimeStampedModel):
    """ Model para reunion """
    persona = models.ForeignKey(Person, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField(verbose_name='Asunto Reunion', max_length=100)

    class Meta:
        verbose_name = 'Reunion'
        verbose_name_plural = 'Reuniones'

    def __str__(self):
        return self.asunto
    
=======


class Reunion(TimeStampedModel):
    """  Modelo para reunion  """

    persona = models.ForeignKey(
        Person, 
        on_delete=models.CASCADE
    )
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField(
        'Aunto de Reunion',
        max_length=100
    )

    objects = ReunionManager()

    class Meta:
        verbose_name = 'Reunion'
        verbose_name_plural = 'Reunion'
    
    def __str__(self):
        return self.asunto
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
