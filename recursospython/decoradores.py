#Decoradores:
#Codigo extraido del siguiente enlace:
#https://recursospython.com/guias-y-manuales/decoradores/


# #Creando un decorador:

# @decorador
# def func():
#     pass

# # Lo anterior es equivalente a:
# def func():
#     pass
# func = decorador(func)


def debug(f):
    def new_function(a,b):
        print("Funcion add() llamada!")
        return f(a,b)
    return new_function

@debug
def add(a,b):
    return a+b

# #Equivalente a esto:
# def add(a,b):
#     return a+b
# add = debug(add)

print(add(7,5))
