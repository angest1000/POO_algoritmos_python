import random
import matplotlib.pyplot as plt

def ordenamiento_mezcla(lista):
    global iteraciones
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        iteraciones += 1
        # print(iteraciones)
        # print(izquierda,'*'*5,derecha)
        # Llamada recursiva en cada mitad
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        #Iteradores para recorrer las 2 sublistas
        i = 0
        j = 0
        #iteradior para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
            iteraciones += 1
            # print(iteraciones)
            # print(f'Lista {lista} ***Iz: {izquierda} *** Der: {derecha}')
            

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
            iteraciones += 1
            # print(iteraciones)
            # print(f'Lista {lista} ***Iz: {izquierda}')

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
            iteraciones += 1
        #     print(iteraciones)
        #     print(f'Lista {lista} ***Der: {derecha}')
        # print(f'Izquierda {izquierda}, Derecha {derecha}')
        # print(lista)
        # print('-'*50)
    return lista, iteraciones

def main():
    global iteraciones
    tamanio_lista = int(input('De que tamaño ser la lista: '))
    # lista = [random.randint(0,tamanio_lista) for i in range(tamanio_lista)]
    iteraciones_ord_mez = []
    tam_lis = []
    for j in range(tamanio_lista):

        lista = sorted([i for i in range(j)],reverse=True)
        # print(f'Lista:\n {lista}')
        iteraciones = 0
        lista_ordenada = ordenamiento_mezcla(lista)

        # print(f'Lista Ordenada:\n {lista_ordenada[0]}')
        # print(f'tamanio: {j} Iteraciones: {lista_ordenada[1]}')
        tam_lis.append(j)
        iteraciones_ord_mez.append(lista_ordenada[1])

    plt.scatter(tam_lis,iteraciones_ord_mez,label="Ordenamiento por Mezclas")
    plt.title('Iteraciones que necesita\n el algoritmo de ordenamiento por mezclas en el peor escenario')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Iteraciones')
    plt.legend(loc=2)
    plt.show()
if __name__ == '__main__':
    main()