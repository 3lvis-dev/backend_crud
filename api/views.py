# from django.shortcuts import render
import json
from sre_constants import SUCCESS
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Persona

# Create your views here.
class PersonasView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  # GET Method
  def get(self, request, id=0):
    if (id > 0):
      personas = list(Persona.objects.filter(id=id).values())
      
      if len(personas) > 0: 
        persona = personas[0]
        data = persona
      else: 
        data = {'message' : 'Person not found'}

      return JsonResponse(data)

    else:
      personas = list(Persona.objects.values())
      if len(personas) > 0:
        data = { 'personas' : personas }
      else:
        data = { 'message' : 'Personas not found' }

      return JsonResponse(data)


  # POST Method
  def post(self, request):
    jd = json.loads(request.body)
    Persona.objects.create(
      tipo_documento=jd['tipo_documento'],
      documento=jd['documento'],
      nombre=jd['nombre'],
      apellido=jd['apellido'],
      hobbie=jd['hobbie']
    )
    data = { 'message' : 'successfully registered' }
    
    return JsonResponse(data)


  # PUT Method
  def put(self, request, id):

    jd = json.loads(request.body)
    personas = list(Persona.objects.filter(id=id).values())

    if len(personas) > 0:
      persona = Persona.objects.get(id=id)
      persona.tipo_documento=jd['tipo_documento']
      persona.documento=jd['documento']
      persona.nombre=jd['nombre']
      persona.apellido=jd['apellido']
      persona.hobbie=jd['hobbie']
      persona.save()
      data = {'message' : 'updated data'}
    else:
      data = { 'message' : 'Persona not found' }

    return JsonResponse(data)


  # DELETE Method
  def delete(self, request, id):
    personas = list(Persona.objects.filter(id=id).values())
    if len(personas) > 0:
      Persona.objects.filter(id=id).delete()
      data = {'message' : 'Delete success'}
      print('{data} Eliminaste a esta persona')
    else:
      data = {'message' : 'Persona not found'}

    return JsonResponse(data)

