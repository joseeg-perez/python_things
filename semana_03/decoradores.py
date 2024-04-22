#Funcion dentro de variable

def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(1))

#Funciones anidadas

def plus_one(number):
    def add_one(number):
        return number + 1
    
    result = add_one
    return result(number)

print(plus_one(2))

#Funcion como argumento

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 3
    return function(number_to_add)

print(function_call(plus_one))

#Funcion como retorno
def hello_function():
    def say_hi():
        return "Hi"
    
    return say_hi

hello = hello_function()
print(hello())

#Acceso a los parametros de la funcion externa por parte de la funcion
#anidada

def print_message(message):
    def message_sender():
        print(message)

    message_sender()

print_message("Hola")

#########################DECORADORES#########################
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    
    return wrapper

@uppercase_decorator
def say_hi():
    return "Hello there!"

print(say_hi())

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    
    return wrapper

#Decoradores anidados (se ejecutan de abajo a arriba)

@split_string
@uppercase_decorator
def say_bye():
    return "bye bye"

print(say_bye())

#Decoradores con argumentos

def decorator_with_arguments(function):
    def wrapper_with_arguments(arg1, arg2):
        print(f"My arguments are: {arg1} {arg2}")
        #Llama a la funcion orignal
        function(arg1, arg2)

    return wrapper_with_arguments

@decorator_with_arguments
def say_name(first_name, last_name):
    print(f"{first_name}, {last_name}")

say_name( "Jose", "Perez" )

#*arg sirve para cuando una funcion recibe muchos argumentos 
# se envian como una lista
def read_arguments(*args):
    for i in args:
        print(i)

read_arguments("jose", "maria", "luis", "andrea")

# **kwarg para pasar lista de argumentos con clave: valor
def read_arguments_kwarg(**kwarg):
    for key, value in kwarg.items():
        print(f"{key}: {value}")

read_arguments_kwarg(name='Jose', last_name="Perez")