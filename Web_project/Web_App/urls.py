from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("ajouter_fondateur",views.ajouterFondateur,name="ajouter_fondateur"),
    path("modifier_fondateur/<str:pk>",views.updateFondateur,name="modifier_fondateur"),
    path("supprimer_fondateur/<str:pk>",views.deleteFondateur,name="supprimer_fondateur"),

    ##########################users
    path("register_user",views.registerUser,name="register_user"),
    path("login",views.login_view,name="login_user")
    
]