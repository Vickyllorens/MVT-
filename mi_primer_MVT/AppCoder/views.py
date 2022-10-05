from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiares
from django.template import loader 
# Create your views here.

def mostrar_familiares(request):
    template=loader.get_template("templatefamilia.html")
    fam_1=Familiares(nombre="Estefania",edad=53,tipo="madre",profesion="medica",fecha_de_nacimiento="19-11-1968")
    fam_2=Familiares(nombre="Belen",edad=21,tipo="hermana",profesion="estudiante",fecha_de_nacimiento="14-4-2001")
    fam_3=Familiares(nombre="Pablo",edad=53,tipo="padre",profesion="vendedor",fecha_de_nacimiento="23-3-1969")
    fam_4=Familiares(nombre="Alejandro",edad=8,tipo="hermano",profesion="estudiante de primario",fecha_de_nacimiento="19-12-2013")
    
    
    dict_de_contexto={
        "fam1nombre":fam_1.nombre,
        "fam1edad": fam_1.edad,
        "fam1tipo":fam_1.tipo,
        "fam1profesion": fam_1.profesion,
        "fam1fechanac":fam_1.fecha_de_nacimiento,
        "fam2nombre":fam_2.nombre,
        "fam2edad": fam_2.edad,
        "fam2tipo":fam_2.tipo,
        "fam2profesion": fam_2.profesion,
        "fam2fechanac":fam_2.fecha_de_nacimiento,
        "fam3nombre":fam_3.nombre,
        "fam3edad": fam_3.edad,
        "fam3tipo":fam_3.tipo,
        "fam3profesion": fam_3.profesion,
        "fam3fechanac":fam_3.fecha_de_nacimiento,
        "fam4nombre":fam_4.nombre,
        "fam4edad": fam_4.edad,
        "fam4tipo":fam_4.tipo,
        "fam4profesion": fam_4.profesion,
        "fam4fechanac":fam_4.fecha_de_nacimiento,
    } 
    
    res=template.render(dict_de_contexto)
    return HttpResponse(res)
