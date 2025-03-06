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
    # Rota para interface administrativa do Django
    path('admin/', admin.site.urls),

    # Rotas relacionadas aos projetos
    path('projetos/form/', form_projetos, name='get_projeto_form'),  # Obter formulário para projetos
    path('projetos/listar/', listar_projetos, name='listar_projetos'),  # Listar todos os projetos
    path('projetos/cadastrar/', cadastrar_projeto, name='cadastrar_projeto'),  # Cadastrar novo projeto
    path('projetos/inativar/', inativar_projeto, name='inativar_projeto'),  # Inativar um projeto existente
    path('projetos/editar/', editar_projeto, name='editar_projeto'),  # Editar informações de um projeto
    path('projetos/visualizar/', visualizar_projeto, name='visualizar_projeto'),  # Visualizar detalhes de um projeto
    path('projetos/equipe/', equipe_projeto, name='equipe_projeto'),  # Ver equipe associada a um projeto
    path('projetos/equipe/atualizar/', atualizar_equipe, name='atualizar_equipe'),
    # Atualizar informações da equipe do projeto

    # Rotas relacionadas aos colaboradores
    path('colaboradores/listar/', listar_colaboradores, name='listar_colaboradores'),  # Listar todos os colaboradores
    path('colaboradores/cadastrar/', cadastrar_colaboradores, name='cadastrar_colaborador'),
    # Cadastrar novo colaborador
    path('colaboradores/visualizar/', visualizar_colaboradores, name='visualizar_colaborador'),
    # Ver detalhes de um colaborador
    path('colaboradores/editar/', editar_colaboradores, name='editar_colaboradores')
    # Editar informações de um colaborador
]
