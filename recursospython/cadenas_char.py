# Cadenas de caracteres
# Codigo extraido del siguiente enlace:
# https://recursospython.com/guias-y-manuales/formateo-de-cadenas/


nombre = "Juan"
print("Tu nombre es %s " %nombre)
# %s: cadena
# %d: entero
# %f: flotante

# apellido = "Perez"
# sexo = "Masculino"
# print("Tu nombre es: " + nombre + ". Apellido: " + apellido + ". Sexo: " + sexo + ".")

edad = 20
print("Tienes %d años." %edad)

altura = 1.75
print("Tu nombre es %s. Tienes %d años. Mides %f metros." % (nombre,edad,altura))


# Para agregar el signo '%' en una cadena se pone de la siguiente manera:
probabilidad = 70
print("Hay una probabilidad de %d%%" %probabilidad)

# Si utilizas %s pero no es str, se transforma en str:
print("Tienes %s años. Mides %s metros." % (edad,altura))

# Equivalente a :
print("Tienes %s años. Mides %s metros." % (str(edad),str(altura)))

#Mostrando solo 2 decimales:
a = 3.141592
print("a es %.2f" % a)

altura = 1.75
print("Mides %.6f metros." % altura)

#agregando + antes de d, los valores positivos tendran
# su signo:
for i in range(-3,4):
    print("%+d" %i)

#Imprimir hexadecimales:
for i in range(15):
    print("dec:%d hex:%x pref_ex:%#x manual: 0x%X" %(i,i,i,i))

#Definiendo el largo del valor:
for nombre in ("Juan","Pedro","Francisco"):
    print("%9s" % nombre)

for n in (1,10,100):
    print("%3d" % n)

# Añadiendo ceros:
for n in (1,10,100):
    print("%03d" % n)