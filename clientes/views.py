from clientes.forms import ClienteForm
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Cliente, Endereço
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

# class AutoComplete(CreateView):
#     template_name = 'autocomplete.html'
#     model = Cliente
#     form_class = ClienteForm
#     success_url = reverse_lazy('autocomplete')
    
#     def form_valid(self, form):
#         return super().form_valid(form)
    
class AutoComplete(CreateView):
    template_name = 'autocomplete.html'
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('autocomplete')
    
def autocompletehtml5(request):
    context= {}
    context['dados'] = Endereço.objects.all
    return render(request, "autocomplete.html", context)
       

# def autocompletecliente(request):
#     query = request.GET.get('term')
#     query_set = Cliente.objects.filter(nome__icontains=query)
#     myList=[]
#     myList += [x.nome for x in query_set]
#     return JsonResponse(myList,safe=False)
