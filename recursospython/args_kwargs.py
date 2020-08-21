# Argumentos en funciones(*args y **kwargs)
#Codigo extraido del siguiente enlace:
#https://recursospython.com/guias-y-manuales/argumentos-args-kwargs/

#Argumentos convencionales (arguments(args))
#Argumentos sujetos a un nombre especifico (Keyword arguments(kwargs))

# ej:

# def f(a,b,c):
#     return a + b * c

# # print(f(2,5))
# # print(f())
# print(f(2,5,3))

# def h(a,b=4,c=2):
#     return a + b * c

# # print(h(1))
# # print(h(1,5,6))
# # print(h())
# print(h(1,c=10))
# print(h(1,b=5))
# print(h(1,5))
# print(h(1,c=10,b=6))
# print(h(1,6,10))

# def a(c=None):
#     return 100

# def b(n=a()):
#     return n+50

# print(b())
def f(*args):
    return args
print(f(1,5,True,False,"Hola Mundo"))

def f(**kwargs):
    return kwargs
print(f(a=1,b=True,h=50,z="Hola mundo"))

# args y kwargs solo son usados por convencion

def f(*args, **kwargs):
    return args,kwargs

args,kwargs = f(True,False,3.5,mensaje = "Año final",anio = 2020)
print(args)
print(kwargs)

def f(a,b,c):
    return a * b ** c

argumentos= (5,10,2)
print(f(*argumentos))
print(f(5,10,2))

def f(mensaje="Hola",nombre=None):
    print("{0}, {1}!".format(mensaje,nombre))

kwargs = {"mensaje": "Hola", "nombre": "mundo"}
print(f(**kwargs))

