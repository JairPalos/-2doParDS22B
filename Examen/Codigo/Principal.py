from receta import receta 
from Doctor import Doctor
from Paciente import Paciente
from Medicamentos import Medicamentos

def par():
    print( " datos de  receta")
    print("\n")
    idReceta=input('Ingresa el id: ')
    institucion=input('Ingresa la institucion:')

    re=receta(idReceta,institucion)
    receta.Verifica()
    receta.Entrega()

def do():
    print("\n")
    print( " datos de  Doctor")
    print("\n")


    idD= input('Ingresa el id: ')   
    nombre=input('Ingresa el nombre: ')
    Cedula=input('Ingresa el cedula: ')
    doc=Doctor(idD,nombre,Cedula)
    ##doc.Diagnosticar()
    #doc.Recetando()

def df():
    
    print("\n")
    print( " datos de  Paciente")
    print("\n")

    idD= input('Ingresa el id: ')
    nombreP=input('Ingresa el nombre: ')

    pa=Paciente(idD,nombreP)
    #pa.Sintomas()
    #pa.Pago()


def me():
    print("\n")
    print( " datos de  Medicamento")
    print("\n")

    folio= input('Ingresa el folio: ')
    qui=input('Ingresa quimico: ')

    #me=Medicamentos(folio,qui)
    #me.Efectividad()
    #me.Tiempo()

par()
do()
df()
me()