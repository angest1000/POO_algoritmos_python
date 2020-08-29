import random
import matplotlib.pyplot as plt

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
    iteraciones_ins_sor=[]
    iteraciones_bub_sor=[]
    
    tam_de_lista = [i for i in range(2,1000,10)]

    for tamanio_lista in range(2,1000,10):
        # lista = sorted([i for i in range(tamanio_lista)],reverse=True)
        lista = [random.randint(0,tamanio_lista) for i in range(tamanio_lista)]
        
        lista_ord_ins = ordenamiento_insercion(lista)
        lista_ord_bur = ordenamiento_burbuja(lista)

        iteraciones_ins_sor.append(lista_ord_ins[1])
        iteraciones_bub_sor.append(lista_ord_bur[1])
        
    iteraciones_ins_sor = (tam_de_lista,iteraciones_ins_sor)
    iteraciones_bub_sor = (tam_de_lista,iteraciones_bub_sor)
    data = (iteraciones_ins_sor, iteraciones_bub_sor)
    colors = ("red", "green")
    groups = ("Ordenamiento por Insercion", "Ordenamiento de burbuja")
    size = (30,10)
    
    # Create plot
    fig = plt.figure()
    ax = fig.add_subplot()

    for data, color, group, size in zip(data, colors, groups,size):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=size, label=group)

    plt.title('Iteraciones que necesita cada algoritmo, en el peor escenario')
    plt.xlabel('Tamanio de lista')
    plt.ylabel('Iteraciones')
    plt.legend(loc=2)
    plt.show()

if __name__ == '__main__':
    main()