from django.urls import path
from .views import index 
from .views import language, project, project_language, translations, list_project_language, list_translations
from .views import create_language, create_project, create_project_language, create_translations
from .views import tela_update_language, tela_update_project, tela_update_projectlanguage, tela_update_translations
from .views import update_language, update_project, update_projectlanguage, update_translations

from .views import ListLanguage, ListProject
# , ListTranslations
# from .views import UpdateLanguage, UpdateProject, UpdateProjectLanguage, UpdateTranslations 
from .views import DeleteLanguage, DeleteProject, DeleteProjectLanguage, DeleteTranslations

# from .generate_csv import load_projects, generate_csv 
from .generate_file import load_projects, generate_csv, generate_file 



#     ..... Lista de endereços "rotas" do App translate...
urlpatterns = [
    path("", index, name='index'),                  # ...página principal do App translate.

    path("export_translations", load_projects, name='export_translations'), 
    path("generate_csv", generate_csv, name='generate_csv'),     
    # path("generate_file", generate_file, name='generate_file'),     
    
    path("list_language", ListLanguage.as_view(), name='list_language'), 
    path("list_project", ListProject.as_view(), name='list_project'), 
    path("list_translations", list_translations, name='list_translations'),    
    path("list_project_language", list_project_language, name='list_project_language'),    

    path("insert_language", language, name='insert_language'), 
    path("insert_project", project, name='insert_project'),    
    path("insert_project_language", project_language, name='insert_project_language'),    
    path("insert_translations", translations, name='insert_translations'),    

    path("language/create", create_language, name='create_language'),  
    path("project/create", create_project, name='create_project'),    
    path("project_language/create", create_project_language, name='create_project_language'),    
    path("translations/create", create_translations, name='create_translations'),    

    path("tela_update_language/<str:id>", tela_update_language, name='tela_update_language'), 
    path("tela_update_project/<str:id>", tela_update_project, name='tela_update_project'), 
    path("tela_update_projectlanguage/<str:id>", tela_update_projectlanguage, name='tela_update_projectlanguage'), 
    path("tela_update_translations/<str:id>", tela_update_translations, name='tela_update_translations'), 
    
    path("language/update/<str:id>", update_language, name='update_language'), 
    path("update_project/<str:id>", update_project, name='update_project'), 
    path("update_project_language/<str:id>", update_projectlanguage, name='update_projectlanguage'), 
    path("update_translations/<str:id>", update_translations, name='update_translations'), 

    path("delete_language/<str:pk>", DeleteLanguage.as_view(), name='delete_language'), 
    path("delete_project/<str:pk>", DeleteProject.as_view(), name='delete_project'), 
    path("delete_project_language/<str:pk>", DeleteProjectLanguage.as_view(), name='delete_project_language'), 
    path("delete_translations/<str:pk>", DeleteTranslations.as_view(), name='delete_translations'), 
]
