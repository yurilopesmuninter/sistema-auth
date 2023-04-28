from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('plataforma/', views.plataforma, name="plataforma"),
    path('redefinir_senha/', views.redefinir_senha, name="redefinir_senha"),
    path('logout/', views.logout, name="logout" )
]