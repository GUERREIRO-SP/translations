from django.urls import path
from translate.views import index, register, change, export
from translate.views import RegisterList

#     ..... Lista de endereços "rotas" do App translate...
urlpatterns = [
    path("", index, name='index'),     #página principal do App translate.
    path("register", register, name='register'),    
    path("change", change, name='change'),    
    path("export", export, name='export'), 
    path("list", RegisterList.as_view(), name='list'), 
]
