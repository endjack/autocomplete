from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Cliente

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

def autocompletecliente(request):
    query = request.GET.get('term')
    query_set = Cliente.objects.filter(nome__icontains=query)
    myList=[]
    myList += [x.nome for x in query_set]
    return JsonResponse(myList,safe=False)
