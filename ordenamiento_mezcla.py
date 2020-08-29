import random

def ordenamiento_mezcla(lista,iteraciones):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        iteraciones += 1
        print(iteraciones)
        print(izquierda,'*'*5,derecha)
        # Llamada recursiva en cada mitad
        ordenamiento_mezcla(izquierda,iteraciones)
        ordenamiento_mezcla(derecha,iteraciones)

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
            print(iteraciones)
            

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
            iteraciones += 1
            print(iteraciones)

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
            iteraciones += 1
            print(iteraciones)
        print(f'Izquierda {izquierda}, Derecha {derecha}')
        print(lista)
        print('-'*50)
    return lista, iteraciones

def main():
    tamanio_lista = int(input('De que tamaño ser la lista: '))
    lista = [random.randint(0,tamanio_lista) for i in range(tamanio_lista)]
    print(f'Lista:\n {lista}')
    iteraciones = 0
    lista_ordenada = ordenamiento_mezcla(lista,iteraciones)

    print(f'Lista Ordenada:\n {lista_ordenada[0]}')
    print(f'Iteraciones {lista_ordenada[1]}')
    

if __name__ == '__main__':
    main()