class Duck:
    __name = ''

    def __init__(self, name = None) -> None:
        type(self).__name = name

    def say_name(self):

        if self.__name: 
            print('Hello, my name is', self.__name)
        else:
            print('Hello Im a Duck without name :(')

    @property #Buena practica para los getters
    def name(self,): 
        return self.__name
    
    @name.setter #Buena practica para los setters
    def name(self, name):
        self.__name = name

    @staticmethod #Decorador
    def say_bye():
        print('Bye Bye')

    
joseDuck = Duck('jose')
joseDuck.say_name()

#print(Duck.__dict__) #permite ver los atributos de una clase

#Llamando al metodo estatico
Duck.say_bye()