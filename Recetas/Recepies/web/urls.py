from django.urls import path
from . import views



urlpatterns =[
  path('',views.index, name='index'),
  path('recetas_listado/', views.RecetasListView.as_view(), name='recetas_listado'),
  path('agregar/', views.RecetasCreateView.as_view(), name='agregar'),
  path('detalle/<int:pk>/', views.RecetasDetailView.as_view(), name='detalle'),
  path('editar/<int:pk>/', views.RecetasUpdateView.as_view(), name='editar'),
  path('borrar/<int:pk>/', views.RecetasDeleteView.as_view(), name='borrar' )
 
]