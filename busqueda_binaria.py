import random

def busqueda_binaria(lista,comienzo,final,objetivo,iteraciones):
    print(f'Buscando {objetivo} en {lista[comienzo:final]}')
    if comienzo > final:
        return False,0,iteraciones + 1

    medio = (comienzo + final) //2 #Division entera

    if lista[medio] == objetivo:
        return True,medio,iteraciones + 1
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo,iteraciones + 1)
    else:
        return busqueda_binaria(lista, comienzo, medio-1, objetivo,iteraciones + 1)        
        
if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño sera la lista?: '))
    objetivo =  int(input('Introduzca el numero a buscar: '))
    lista = [random.randint(0,100) for i in range(tamanio_lista)]
    
    print('Lista sin ordenar: \n',lista)
    lista = sorted(lista)
    # print('\nLista ordenada:\n',lista,'\n')

    iteraciones = 0
    encontrado = busqueda_binaria(lista,0,len(lista),objetivo,iteraciones)
    print(f'El elemento {objetivo} {"esta" if encontrado[0] else "no esta"} en la lista')
    print(f'Iteraciones: {encontrado[2]}')
    if encontrado[0]:
        print(f'Posicion: lista[{encontrado[1]}]')
        

