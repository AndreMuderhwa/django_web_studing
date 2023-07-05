from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from . models import *
from . forms import *
# Create your views here.

def index(request):
    fondateurs=Fondateur.objects.all()
    context={"fondateurs":fondateurs}

    return render(request,"index.html",context)

# def ajouterFondateur(request):
#     if request.method=="POST":
#         name=request.POST.get('nom')
#         firstname=request.POST.get('postnom')
#         lastname=request.POST.get('prenom')
#         descript=request.POST.get('description')
#         dateNaiss=request.POST.get('date')
#         photoFondat=request.FILES['photo']
#         Fondateur.objects.create(nom=name,postnom=firstname,prenom=lastname,
#                                  dateNaissance=dateNaiss,description=descript,photo=photoFondat)
#         return redirect("home")
def ajouterFondateur(request):
    form=FondateurForm()
    if request.method=="POST":
        f=FondateurForm(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            return redirect("home")
    code={"formulaire":form}

    return render(request,"ajouter_fondateur.html",code)

def updateFondateur(request,pk):
    obj=Fondateur.objects.get(id_fondateur=pk)
    form=FondateurForm()
    form=FondateurForm(instance=obj)
    if request.method=="POST":
        form=FondateurForm(request.POST,request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={"formulaire":form}
    
    return render(request,"ajouter_fondateur.html",context)

def deleteFondateur(request,pk):
    obj=Fondateur.objects.get(id_fondateur=pk)
    if request.method=="POST":
        obj.delete()
        return redirect('home')
    context={"fondateur":obj}
    return render(request,"supprimer.html",context)
##############################################################################################################


def registerUser(request):
    if request.method=="POST":
        user=request.POST.get("username")
        pwd=request.POST.get("password")
        first=request.POST.get("firstname")
        last=request.POST.get("lastname")
        mail=request.POST.get("email")
        if user != None and pwd != None:
            User.objects.create_user(username=user,password=pwd,first_name=first,
                                     last_name=last,email=mail)
            return redirect("/login")
    return render(request,"register_user.html")


def login_view(request):
    return render(request,"login.html")