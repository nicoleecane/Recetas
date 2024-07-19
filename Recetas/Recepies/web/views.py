from django.shortcuts import render
from django.http import HttpResponse
from .models import Receta
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

context={
   'username': 'Gaston',
   'fecha_hoy':'7/12/2024'
}

def index(request):
   return render(request, 'web/index.html', context)


def recetas_listado(request):
   
   listado_recetas=[
      'Receta 1',
      'Receta 2',
      'Receta 3',
      'Receta 4',
      'Receta 5',
   ]
   
   context= {
      'listado_recetas': listado_recetas,
      'receta_activa': False
   }

   
   return render(request, 'web/recetas_listado.html', context)
   


def agregar(request):
   return render(request, 'web/agregar.html', context)


def editar(request):
   return render(request, 'web/editar.html', context)


def borrar(request):
   return render(request, 'web/borrar.html', context)

class RecetasListView(ListView):
    model = Receta
    context_object_name = 'listado_recetas'
    template_name = "web/recetas_listado.html"
    
    

class RecetasCreateView(CreateView):
    model = Receta
    template_name = 'web/agregar.html'
    context_object_name='agregar'
    fields = ('__all__')
    
    
    
    def get_success_url(self):
        return reverse_lazy('recetas_listado')
    
    
class RecetasDetailView(DetailView):
   model=Receta
   template_name='web/detalles.html'
   context_object_name='receta'
  
    
    
class RecetasUpdateView(UpdateView):
     model = Receta
     template_name = 'web/editar.html'
     fields= ('__all__')
     
   
     
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_id'] = self.object.pk
        return context
     
     
     def get_success_url(self):
        return reverse_lazy('recetas_listado')
     
     
     def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'La receta se actualizó correctamente.')
        return response
     
     

     
class RecetasDeleteView(DeleteView):
    model = Receta
    template_name = 'web/borrar.html'   
    success_url = reverse_lazy('recetas_listado')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_id'] = self.object.pk
        return context
    
 

