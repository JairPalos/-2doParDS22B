class receta:

    def __init__(self,idReceta,institucion) :
        self.idReceta=idReceta
        self.institucion=institucion


    def Verifica():
        print("Se verifico con exito!!!!")

    def Entrega():
        print("Se entrego  con exito!!!!")

    def ImprimirR(idReceta,institucion):
        print("El ID  de la receta es: " )
        print(idReceta)
        print("\n")
        print("La institucion es:" )
        print(institucion)