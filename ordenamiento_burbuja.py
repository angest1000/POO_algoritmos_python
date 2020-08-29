# 6 5 3 1 8 7 2 4

import random

def ordenamiento_burbuja(lista):
    tam_list = len(lista)
    paso = 0 
    for i in range(tam_list):
        # print(f'Paso {paso}')
        for j in range(0,tam_list-i-1): #O(n) * O(n) = O(n*n) = O(n**2)
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
            paso += 1
        # print(lista)
    return lista,paso

if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño sera la lista?: '))
    
    lista = [random.randint(0,100) for i in range(tamanio_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada[0])
    print(f'Numero de pasos: {lista_ordenada[1]}')