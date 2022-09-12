from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
import json

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