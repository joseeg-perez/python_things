#Problema del diamante

class Animal:
    def hacer_sonido(self):
        print('Soy un animal.')


class Perro(Animal):
    def hacer_sonido(self):
        print('Soy un perro.')

class Gato(Animal):
    def hacer_sonido(self):
        print('Soy un gato.')

class Cachorro(Gato, Perro): #De izquierda a derecha
    pass


cachorrito = Cachorro()
#Como el cachorro hereda de gato y de perro
#y ambos tienen implementado el metodo hacer_sonido
#se toma el del gato
cachorrito.hacer_sonido()