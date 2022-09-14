from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import  Usuario, Modalidad, Reports, Cais
from .serializer import ReportSerializer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import json

from django.template import loader
from django.http import HttpResponse

#Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Modelos



# Create your views here.



class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
          if (id > 0):
            usuarios = list(Usuario.objects.filter(id=id).values())
            if len(usuarios) > 0:
                usuario =  usuarios[0]
                datos = {'message': "Success", 'company': usuario}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)
          else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'message': "Success", 'companies': usuarios}
            else:
                datos = {'message': "Companies not found..."}
            return JsonResponse(datos)
    

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Usuario.objects.create(userName=jd['userName'], email=jd['email'], totalReports=jd['totalReports'],pswd=jd['pswd'] )
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        pass

    def delete(self, request, id):
       pass 

class ModalidadView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
          if (id > 0):
            modalidades = list(Modalidad.objects.filter(id=id).values())
            if len(modalidades) > 0:
                modalidad =  modalidades[0]
                datos = {'message': "Success", 'modalidad': modalidad}
            else:
                datos = {'message': "modalidad not found..."}
            return JsonResponse(datos)
          else:
            modalidades = list(Modalidad.objects.values())
            if len(modalidades) > 0:
                datos = {'message': "Success", 'metodos': modalidades}
            else:
                datos = {'message': "modalidad not found..."}
            return JsonResponse(datos)
    

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Modalidad.objects.create(nombre=jd['nombre'] )
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        pass

    def delete(self, request, id):
       pass 


class ReportsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
          if (id > 0):
            reportes = list(Reports.objects.filter(id=id).values())
            if len(reportes) > 0:
                reporte =  reportes[0]
                datos = {'message': "Success", 'reportes': reporte}
            else:
                datos = {'message': "reportes not found..."}
            return JsonResponse(datos)
          else:
            reportes = list(Reports.objects.values())
            if len(reportes) > 0:
                datos = {'message': "Success", 'reportes': reportes}
            else:
                datos = {'message': "reportes not found..."}
            return JsonResponse(datos)
    

    def post(self,request,*args, **kwargs):
        # print(request.body)
      #  jd = json.loads(request.body)
        # print(jd)
       
       # Reports.objects.create(dia=jd['dia'],hora=jd['hora'], descripcion=jd['descripcion'],getLat=jd['getLat'],getLng=jd['getLng'],modalidad=jd['modalidad'])

        #datos = {'message': "Success"}
        #return JsonResponse(datos)
        


        data = JSONParser().parse(request)
        serializer =ReportSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)




class CaisView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
          if (id > 0):
            caiss = list(Cais.objects.filter(id=id).values())
            if len(caiss) > 0:
                cai =  caiss[0]
                datos = {'message': "Success", 'cai': cai}
            else:
                datos = {'message': "cai not found..."}
            return JsonResponse(datos)
          else:
            caiss = list(Cais.objects.values())
            if len(caiss) > 0:
                datos = {'message': "Success", 'cai': caiss}
            else:
                datos = {'message': "cainot found..."}
            return JsonResponse(datos)