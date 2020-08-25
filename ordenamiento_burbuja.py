# 6 5 3 1 8 7 2 4

import random

def ordenamiento_burbuja(lista):
    tam_list = len(lista) - 1
    paso = 0 
    while tam_list > 0:
        print(f'Paso {paso}')
        for i in range(tam_list):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
            print(lista)
            paso += 1
        tam_list -= 1
    return lista

if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño sera la lista?: '))
    
    lista = [random.randint(0,100) for i in range(tamanio_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)