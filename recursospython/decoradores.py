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
import pdb
from functools import wraps

def debug(f):#breakpoint=False):
    # def debug_decorator(f):
    @wraps(f)
    def new_function(*args, **kwargs):
        print(f"Funcion {f.__name__}() llamada!")
            # if breakpoint:
            #     pdb.set_trace()
        return f(*args, **kwargs)
    return new_function
    # return debug_decorator

# Con los argumentos *args y **kwargs nuestro
# decorador se puede usar en cualquier funcion
# que tenga cualquier numero de argumentos
# @debug(breakpoint=True)
# def add(a,b):
#     return a + b

# #Equivalente a esto:
# def add(a,b):
#     return a+b
# add = debug(add)

@debug
def neg(n):
    "Retorna el inverso de n."
    return n * -1

print(neg.__name__)
help(neg)
# print(add(7,5))

# @debug
# def operaciones(a,b,c,d):
#     return a * b + c - d

# print(operaciones(1,5,10,2))

# @debug(breakpoint=True)
# def func():
#     pass
# #Equivalente a :
# # def func():
# #     pass
# # func = debug(breakpoint=True)(func)

