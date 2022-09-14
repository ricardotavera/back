from django.urls import path
from .views import UsuarioView, ModalidadView, ReportsView, CaisView

urlpatterns=[ 
    path('usuarios/', UsuarioView.as_view(), name='usuarios_list' ),
    path('usuarios/<int:id>', UsuarioView.as_view(), name='usuarios_process' ),

    path('modalidades/', ModalidadView.as_view(), name='modalidades_list' ),
    path('modalidades/<int:id>', ModalidadView.as_view(), name='modalidades_process' ),

    path('reportes/', ReportsView.as_view(), name='reportes_list' ),
    path('reportes/<int:id>', ReportsView.as_view(), name='reportes_process' ),

    path('cais/', CaisView.as_view(), name='Cais_list' ),
    path('cais/<int:id>', CaisView.as_view(), name='Cais_process' ),

]