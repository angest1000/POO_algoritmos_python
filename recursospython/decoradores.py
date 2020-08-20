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
    def new_function(*args, **kwargs):
        print(f"Funcion {f.__name__}() llamada!")
        return f(*args, **kwargs)
    return new_function
# Con los argumentos *args y **kwargs nuestro
# decorador se puede usar en cualquier funcion
# que tenga cualquier numero de argumentos
@debug
def add(a,b):
    return a+b

# #Equivalente a esto:
# def add(a,b):
#     return a+b
# add = debug(add)
print(add(7,5))

@debug
def neg(n):
    return n * -1

print(neg(5))

@debug
def operaciones(a,b,c,d):
    return a * b + c - d

print(operaciones(1,5,10,2))