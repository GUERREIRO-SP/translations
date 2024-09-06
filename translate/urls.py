from django.urls import path
from .views import index, language, project, project_language, translations, list_project_language
from .views import create_language, create_project, create_project_language, create_translations 
from .views import ListLanguage, ListProject, ListTranslations    

#     ..... Lista de endereços "rotas" do App translate...
urlpatterns = [
    path("", index, name='index'),                  # ...página principal do App translate.
    path("list_language", ListLanguage.as_view(), name='list_language'), 
    path("insert_language", language, name='insert_language'), 
    path("language/create", create_language, name='create_language'),  

    path("list_project", ListProject.as_view(), name='list_project'), 
    path("insert_project", project, name='insert_project'),    
    path("project/create", create_project, name='create_project'),    
    
    path("list_project_language", list_project_language, name='list_project_language'),    
    path("insert_project_language", project_language, name='insert_project_language'),    
    path("project_language/create", create_project_language, name='create_project_language'),    
    
    path("list_translations", ListTranslations.as_view(), name='list_translations'),    
    path("insert_translations", translations, name='insert_translations'),    
    path("translations/create", create_translations, name='create_translations'),    
]
