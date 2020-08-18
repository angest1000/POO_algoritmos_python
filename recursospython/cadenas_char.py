# Cadenas de caracteres
# Codigo extraido del siguiente enlace:
# https://recursospython.com/guias-y-manuales/formateo-de-cadenas/

# Un nuevo metodo python 3.6:
nombre = "Juan"
edad = 20
altura = 1.75

print(f"Te llamas {nombre}, tienes {edad} años y mides {altura} metros.")
print(f"Tu nombre al reves es {nombre[::-1]}.")
print(f"Dentro de 5 años tendras {edad +5} años.")

#Intentando hacer lo anterior con el metodo recomendado:
print(f"Tu nombre es {nombre} y tienes {edad} años .".format(**locals()))

for nombre in ("Juan","Pedro","Francisco"):
    print(f"{nombre:>9}")

#El metodo recomendado:
# nombre = "Juan"
# edad = 20
# print("Tu nombre es {0} y tienes {1} años.".format(nombre,edad))
# print("Tienes {1} años y te llamas {0}.".format(nombre,edad))
# print("{0} {1} {0} {1} {1} {0} {0}".format(nombre,edad))

# #Se pueden omitir los numeros dentro de las llaves
# print("Tu nombre es {} y tienes {} años.".format(nombre,edad))

# # Definiendo nombre a los valores:
# print("Tu nombre es {a} y tienes {b} años.".format(a=nombre,b=edad))

# print("Tu nombre es {0} y tienes {1} años. Mides {altura} metros.".format(nombre,edad,altura=1.75))

# for i in range(-3,4):
#     print("{0:+}".format(i))

# for nombre in ("Juan","Pedro","Francisco"):
#     print("{0:>9}".format(nombre))

# #centrando los nombres:
# for nombre in ("Juan","Pedro","Francisco"):
#     print("{0:^9}".format(nombre))

# #Hexadecimal:
# for i in range(0,1000,100):
#     print("dec:{}, hex:0x{:X}".format(i,i))

# #Ambos son equivalentes:
# print("{:5}".format(10))
# print("{:{}}".format(10,5))

# #Imprimiendo llaves:
# print("{{}}".format())


# print("Tu nombre es %s " %nombre)
# %s: cadena
# %d: entero
# %f: flotante

# apellido = "Perez"
# sexo = "Masculino"
# print("Tu nombre es: " + nombre + ". Apellido: " + apellido + ". Sexo: " + sexo + ".")

# edad = 20
# print("Tienes %d años." %edad)

# altura = 1.75
# print("Tu nombre es %s. Tienes %d años. Mides %f metros." % (nombre,edad,altura))


# # Para agregar el signo '%' en una cadena se pone de la siguiente manera:
# probabilidad = 70
# print("Hay una probabilidad de %d%%" %probabilidad)

# # Si utilizas %s pero no es str, se transforma en str:
# print("Tienes %s años. Mides %s metros." % (edad,altura))

# # Equivalente a :
# print("Tienes %s años. Mides %s metros." % (str(edad),str(altura)))

# #Mostrando solo 2 decimales:
# a = 3.141592
# print("a es %.2f" % a)

# altura = 1.75
# print("Mides %.6f metros." % altura)

# #agregando + antes de d, los valores positivos tendran
# # su signo:
# for i in range(-3,4):
#     print("%+d" %i)

# #Imprimir hexadecimales:
# for i in range(15):
#     print("dec:%d hex:%x pref_ex:%#x manual: 0x%X" %(i,i,i,i))

# #Definiendo el largo del valor:
# for nombre in ("Juan","Pedro","Francisco"):
#     print("%9s" % nombre)

# for n in (1,10,100):
#     print("%3d" % n)

# # Añadiendo ceros:
# for n in (1,10,100):
#     print("%03d" % n)