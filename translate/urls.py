from django.urls import path
from translate.views import index, register, change, export, project, language, proj_lang, create_language, create_project
from translate.views import RegisterList

#     ..... Lista de endereços "rotas" do App translate...
urlpatterns = [
    path("", index, name='index'),                  # ...página principal do App translate.
    path("language", language, name='language'), 
    path("language/create", create_language, name='create_language'),        
    path("project", project, name='project'),    
    path("project/create", create_project, name='create_project'),    
    path("proj_lang", proj_lang, name='proj_lang'),    
    path("register", register, name='register'),    
    path("change", change, name='change'),    
    path("export", export, name='export'), 
    path("list", RegisterList.as_view(), name='list'), 
]
