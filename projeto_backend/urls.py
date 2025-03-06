"""
URL configuration for projeto_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projetos/form/', form_projetos, name='get_projeto_form'),
    path('projetos/listar/', listar_projetos, name='listar_projetos'),
    path('projetos/cadastrar/', cadastrar_projeto, name='cadastrar_projeto'),
    path('projetos/inativar/', inativar_projeto, name='inativar_projeto'),
    path('projetos/editar/', editar_projeto, name='editar_projeto'),
    path('projetos/visualizar/', visualizar_projeto, name='visualizar_projeto'),
    path('projetos/equipe/', equipe_projeto, name='equipe_projeto'),
    path('projetos/equipe/atualizar/', atualizar_equipe, name='atualizar_equipe'),
    path('colaboradores/listar/', listar_colaboradores, name='listar_colaboradores'),
    path('colaboradores/cadastrar/', cadastrar_colaboradores, name='cadastrar_colaborador'),
    path('colaboradores/visualizar/', visualizar_colaboradores, name='visualizar_colaborador'),
    path('colaboradores/editar/', editar_colaboradores, name='editar_colaboradores')

]
