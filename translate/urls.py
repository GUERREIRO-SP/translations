from django.urls import path
from .views import index, language, project, project_language, translations, list_project_language
from .views import create_language, create_project, create_project_language, create_translations 
from .views import ListLanguage, ListProject, ListTranslations
from .views import UpdateLanguage, UpdateProject, UpdateProjectLanguage, UpdateTranslations 
from .views import DeleteLanguage, DeleteProject, DeleteProjectLanguage, DeleteTranslations


#     ..... Lista de endereços "rotas" do App translate...
urlpatterns = [
    path("", index, name='index'),                  # ...página principal do App translate.
    path("list_language", ListLanguage.as_view(), name='list_language'), 
    path("list_project", ListProject.as_view(), name='list_project'), 
    path("list_translations", ListTranslations.as_view(), name='list_translations'),    
    path("list_project_language", list_project_language, name='list_project_language'),    

    path("insert_language", language, name='insert_language'), 
    path("insert_project", project, name='insert_project'),    
    path("insert_project_language", project_language, name='insert_project_language'),    
    path("insert_translations", translations, name='insert_translations'),    

    path("language/create", create_language, name='create_language'),  
    path("project/create", create_project, name='create_project'),    
    path("project_language/create", create_project_language, name='create_project_language'),    
    path("translations/create", create_translations, name='create_translations'),    

    path("update_language/<str:pk>", UpdateLanguage.as_view(), name='update_language'), 
    path("update_project/<str:pk>", UpdateProject.as_view(), name='update_project'), 
    path("update_project_language/<str:pk>", UpdateProjectLanguage.as_view(), name='update_project_language'), 
    path("update_translations/<str:pk>", UpdateTranslations.as_view(), name='update_translations'), 
   
    path("delete_language/<str:pk>", DeleteLanguage.as_view(), name='delete_language'), 
    path("delete_project/<str:pk>", DeleteProject.as_view(), name='delete_project'), 
    path("delete_project_language/<str:pk>", DeleteProjectLanguage.as_view(), name='delete_project_language'), 
    path("delete_translations/<str:pk>", DeleteTranslations.as_view(), name='delete_translations'), 
]
