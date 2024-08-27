from django.urls import path
from translate.views import index, register

#     ..... Lista de endereços "rotas" do App translate...
urlpatterns = [
    path("", index, name='index'),     #página principal do App translate.
    path("register/", register, name='register'),    
]
