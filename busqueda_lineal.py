import random

def busqueda_lineal(lista,objetivo):
    match = False
    i=0
    
    for elemento in lista: #Complejidad O(n)
        if elemento == objetivo:
            match = True
            break
        i += 1
    return match,i


if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño sera la lista?: '))
    objetivo =  int(input('Introduzca el numero a buscar: '))

    lista = [random.randint(0,100) for i in range(tamanio_lista)]

    encontrado = busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado[0] else "no esta"} en la lista')
    print(f'Iteraciones: {encontrado[1]}')
    if encontrado[0]:
        print(f'Posicion: lista[{encontrado[1]}]')
        