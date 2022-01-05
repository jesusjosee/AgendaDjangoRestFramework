<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('personas/', views.ListaPersonas.as_view(), name='personas'),
    path('api/personas/list/', views.PersonListApiView.as_view(), name='listado-personas' ),
    path('api/personas/create/', views.PersonCreateApiView.as_view(), name='crear-persona' ),
    path('api/personas/detail/<pk>/', views.PersonDetailApiView.as_view(), name='detail-persona' ),
    path('api/personas/delete/<pk>/', views.PersonDeleteApiView.as_view(), name='delete-person' ),
    path('api/personas/update/<pk>/', views.PersonUpdateApiView.as_view(), name='update-person' ),
    path('api/personas/update-retrieve/<pk>/', views.PersonRetrieveUpdateApiView.as_view(), name='update-person-data' ),
    path('api/personas/lista-serializer/', views.PersonSerialzerList.as_view() ),
    path('api/personas/lista-serializer2/', views.PersonSerialzerList2.as_view(), name='listado-nuevo-campo' ),
    path('api/reuniones/', views.ReunionSerializerList.as_view(), name='reuniones' ),
    path('api/personas/list-manytomany/', views.PersonaSerialzerWithManyToManyApi.as_view(), name='personas-many-to-many' ),
    path('api/reuniones-method/', views.ReunionApiViewMethod.as_view(), name='reuniones-method' ),
    path('api/reuniones-link/', views.ReunionApiListLink.as_view(), name='reuniones-link' ),
    path('api/personas/paginacion/', views.PersonListPaginationApi.as_view(), name='personas-paginacion' ),

]

=======
#
from django.urls import path, re_path
#
from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        'personas/',
        views.ListaPersonas.as_view(),
        name='personas'
    ),
    path(
        'api/persona/lista/',
        views.PersonListApiView.as_view(),
    ),
    path(
        'lista/',
        views.PersonListView.as_view(),
        name='lista'
    ),
    path(
        'api/persona/search/<kword>/',
        views.PersonSearchApiView.as_view(),
    ),
    path(
        'api/persona/create/',
        views.PersonCreateView.as_view(),
    ),
    path(
        'api/persona/detail/<pk>/',
        views.PersonDetailView.as_view(),
        name='detalle'
    ),
    path(
        'api/persona/delete/<pk>/',
        views.PersonDeleteView.as_view(),
    ),
    path(
        'api/persona/update/<pk>/',
        views.PersonUpdateView.as_view(),
    ),
    path(
        'api/persona/modificar/<pk>/',
        views.PersonRetriveUpdateView.as_view(),
    ),
    #
    path(
        'api/personas/',
        views.PersonApiLista.as_view(),
    ),
    path(
        'api/reuniones/',
        views.ReunionApiLista.as_view(),
    ),
    path(
        'api/reuniones-link/',
        views.ReunionApiListaLink.as_view(),
    ),
    path(
        'api/personas/paginacion/',
        views.PersonPaginationLits.as_view(),
    ),
    path(
        'api/reunion/por-job/',
        views.ReunionByPersonJob.as_view(),
    ),
]
>>>>>>> 89156801c47ecc5338cfa111715812ae1a6be81c
