<<<<<<< HEAD
from django.db.models import fields
from .models import Hobby, Person, Reunion

from rest_framework import serializers, pagination

from applications.persona import models

class PersonSerializer(serializers.ModelSerializer):
    """ ModelSerializer trabaja con un modelo, similar al formulario ModelForm """
    class Meta:
        model = Person
        fields = ('__all__')
        #fields = ('id', 'full_name', 'job', 'email', 'phone')

class PersonaSerializer(serializers.Serializer):
    """
    Serializer trabaja sin un modelo , similar al forms.Form 
    EL atributo activo no esta en base de datos del modelo Person, por lo tanto, para que funcione
    en este serializador debe estar como required=False o default=False, sino no funcionará la vista     
    """

=======
#
from rest_framework import serializers, pagination
#
from .models import Person, Reunion, Hobby


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


class PersonaSerializer(serializers.Serializer):
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
<<<<<<< HEAD
    activo = serializers.BooleanField(required=False)

class PersonaSerializer2(serializers.ModelSerializer):
    """ Este serializador es ModelSerializer pero tambien se le puede añadir un campo extra,
    convirtiendolo en default=false """
=======
    #
    activo = serializers.BooleanField(required=False)


class PersonaSerializer2(serializers.ModelSerializer):
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c

    activo = serializers.BooleanField(default=False)

    class Meta:
        model = Person
        fields = ('__all__')
<<<<<<< HEAD
    

class ReunionSerializer(serializers.ModelSerializer):
    """ 
    Este serializador tiene un modelo con un campo Foreing key y para mostrar datos
    de ese modelo (en vez de solo el id) , se debe hacer lo sgte. que es declarar el campo persona
    a un seriazador que ya existe, para ese modelo.
    """
=======



class ReunionSerializer(serializers.ModelSerializer):
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c

    persona = PersonSerializer()

    class Meta:
        model = Reunion
<<<<<<< HEAD
        fields = ('id','fecha', 'hora', 'asunto', 'persona')


class HobbySerializer(serializers.ModelSerializer):
    """ 
    Serializador para el modelo Hobby
    """

=======
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )


class HobbySerializer(serializers.ModelSerializer):
    
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
    class Meta:
        model = Hobby
        fields = ('__all__')

<<<<<<< HEAD
class PersonaSerializerManyToMany(serializers.ModelSerializer):
    """ 
    Este serializador tiene un modelo con un campo Many to Many y para mostrar datos
    de ese modelo (en vez de solo el id) , se debe hacer lo sgte. que es declarar el campo 
    """
=======

class PersonaSerializer3(serializers.ModelSerializer):
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c

    hobbies = HobbySerializer(many=True)

    class Meta:
        model = Person
<<<<<<< HEAD
        fields = ('id', 'full_name', 'job', 'email', 'phone', 'hobbies', 'created')
        
class ReunionSerializer2(serializers.ModelSerializer):
    """ 
    Este serializador tiene la particularidad de que se le ha agregado un metodo creado por 
    nosotros mismos el cual le llamaremos fecha_hora, se debe añadir el los fields
    """
=======
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
        )


class ReunionSerializer2(serializers.ModelSerializer):
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c

    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
<<<<<<< HEAD
        fields = ('id','fecha', 'hora', 'asunto', 'persona', 'fecha_hora')

    #funcion que va a crear un nuevo campo
=======
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora',
        )
    
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
    def get_fecha_hora(self, obj):
        return str(obj.fecha) + ' - ' + str(obj.hora)


<<<<<<< HEAD
class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):
    """ 
        Este Serializador envia la data de un campo foreignKey mediante una URL en vez de serializar
        toda la informacion, evitando asi que la consulta sea demasiado pesada,para lo cual 
        se tiene que crear un extra-kwargs y añadir una URL de un detailView,
    """

    class Meta:
        model = Reunion
        fields = ('id','fecha', 'hora', 'asunto', 'persona')

        extra_kwargs = {
        'persona' : {'view_name':'detail-persona', 'lookup_field':'pk'}
       }
    
    # persona es el campo foreing Key
    # view_name hace referencia al nombre de una url de tipo DetailView
    # lookup_field hace referencia al pk de esa url DetailView


class PersonPagination(pagination.PageNumberPagination):
    """ Serializador que hace la paginacion """
    page_size = 5
    max_page_size = 100
=======

class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )
        extra_kwargs = {
            'persona': {'view_name': 'persona_app:detalle', 'lookup_field': 'pk'}
        }


class PersonPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100


class CountReunionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
