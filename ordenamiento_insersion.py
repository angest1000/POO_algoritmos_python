import random

def ordenamiento_insercion(lista):
    iteraciones = 0
    for i in range(1,len(lista)):
        j = i
        while lista[j] < lista[j-1] and j > 0:  #O(n) * O(n) = O(n*n) = O(n**2)
            lista[j],lista[j-1] = lista[j-1],lista[j]
            j -= 1
            # print(lista)
            iteraciones +=1
    return lista,iteraciones


def ordenamiento_burbuja(lista):
    tam_list = len(lista)
    iteraciones = 0 
    for i in range(tam_list):
        # print(f'iteraciones {iteraciones}')
        for j in range(0,tam_list-i-1): #O(n) * O(n) = O(n*n) = O(n**2)
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
            iteraciones += 1
        # print(lista)
    return lista,iteraciones

def main():
    tamanio_lista = int(input('De que tamaño ser la lista: '))
    lista = [random.randint(0,tamanio_lista) for i in range(tamanio_lista)]
    print(f'Lista:\n {lista}')
    lista_ord_ins = ordenamiento_insercion(lista)
    lista_ord_bur = ordenamiento_burbuja(lista)

    print(f'Lista Ordenada:\n {lista_ord_ins[0]}')
    print(f'Iteraciones {lista_ord_ins[1]}')
    print(f'Iteraciones {lista_ord_bur[1]}')
    # print(lista_ord_bur[0])

if __name__ == '__main__':
    main()