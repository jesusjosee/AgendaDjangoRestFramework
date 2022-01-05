<<<<<<< HEAD
from re import template
from typing import List
from django.shortcuts import render

from django.views.generic import ListView

#modelos
from .models import Person, Reunion

#rest_framework
from rest_framework.generics import (
     CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView,
    RetrieveUpdateAPIView, UpdateAPIView
)

# 
from .serializers import ( PersonSerializer, PersonaSerializer, 
                            PersonaSerializer2, ReunionSerializer, PersonaSerializerManyToMany,
                            ReunionSerializer2, ReunionSerializerLink, PersonPagination)

class ListaPersonas(ListView):
    """ Listar personas en una vista normal de django """
=======
from django.shortcuts import render

from django.views.generic import ListView, TemplateView
#
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

#
from .models import Person, Reunion
#
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2,
    ReunionSerializer,
    PersonaSerializer3,
    ReunionSerializerLink,
    PersonPagination,
    CountReunionSerializer
)



class ListaPersonas(ListView):
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
    template_name = "persona/personas.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()

<<<<<<< HEAD
class PersonListApiView(ListAPIView):
    """ Listar todas las personas en una url (endpoint) mediante una api """
=======

class PersonListApiView(ListAPIView):

>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
<<<<<<< HEAD
    

class PersonCreateApiView(CreateAPIView):
    """ Esta api sirve para crear nuevos registros """
    serializer_class = PersonSerializer

class PersonDetailApiView(RetrieveAPIView):
    """ Esta vista muestra un solo registro como el detailView pero es un RetrieveAPIView """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonDeleteApiView(DestroyAPIView):
    """ Esta vista api sirve para eliminar un registro de la base de datos """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonUpdateApiView(UpdateAPIView):
    """ UpdateApiView actualiza pero sin traer informacion, se tiene que llenar todos 
    los campos nuevamente """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonRetrieveUpdateApiView(RetrieveUpdateAPIView):
    """ RetrieveUpdateAPIView actualiza y trae la informacion almacenada en la base de datos """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

#
class PersonSerialzerList(ListAPIView):
    """ Listar Personas en una api, con un campo adicional que es activo que no tiene la db """

    serializer_class = PersonaSerializer
    def get_queryset(self):
        return Person.objects.all()
    
class PersonSerialzerList2(ListAPIView):
    """ Listar Personas en una api, con un campo adicional que es activo que no tiene la db """

    serializer_class = PersonaSerializer2
    def get_queryset(self):
        return Person.objects.all()

class ReunionSerializerList(ListAPIView):
    """ Listar todas las Reuniones en una api con un campo Foreign Key """

    serializer_class = ReunionSerializer

    def get_queryset(self):
        return Reunion.objects.all()
    
class PersonaSerialzerWithManyToManyApi(ListAPIView):
    """ Listar todas las personas en una api con un campo many to many """

    serializer_class = PersonaSerializerManyToMany
=======


class PersonListView(TemplateView):
    template_name = 'persona/lista.html'
    

class PersonSearchApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        # filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )


class PersonCreateView(CreateAPIView):
    
    serializer_class = PersonSerializer


class PersonDetailView(RetrieveAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonApiLista(ListAPIView):
    """
        Vista para interactuar con serializadores
    """

    # serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer3
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c

    def get_queryset(self):
        return Person.objects.all()

<<<<<<< HEAD
class ReunionApiViewMethod(ListAPIView):
    """ Listar todas las reuniones en una api con un metodo nuevo que creamos """

    serializer_class = ReunionSerializer2
=======

class ReunionApiLista(ListAPIView):

    serializer_class = ReunionSerializer
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c

    def get_queryset(self):
        return Reunion.objects.all()

<<<<<<< HEAD
class ReunionApiListLink(ListAPIView):
    """ Listar todas las reuniones en una api con un link para un campo foreing key en vez de
    serializar todo """

=======

class ReunionApiListaLink(ListAPIView):
    
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()

<<<<<<< HEAD
class PersonListPaginationApi(ListAPIView):
    """ Listar todas las personas con una paginacion 
    Se debe crear un serializador que haga la paginacion
    """
    serializer_class = PersonSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()
=======

class PersonPaginationLits(ListAPIView):
    """
        lista personas con paginacion
    """

    serializer_class = PersonaSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()


class ReunionByPersonJob(ListAPIView):

    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
