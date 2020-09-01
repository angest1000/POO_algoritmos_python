import random
import matplotlib.pyplot as plt

def contador():
    global i
    i += 1
    return i

def morral(tamanio_morral, pesos, valores, n):
    contador()
    if n == 0 or tamanio_morral == 0:
        return 0

    if pesos[n-1] > tamanio_morral:
        return morral(tamanio_morral,pesos,valores,n-1)
    
    return max(valores[n-1] + morral(tamanio_morral - pesos[n-1], pesos, valores, n-1)
                ,morral(tamanio_morral, pesos, valores, n-1))


if __name__ == '__main__':

    global i

    iter = []
    tam_val = []
    for j in range(1,15):
        valores = [random.randint(0,100) for i in range(j)]
        pesos = [random.randint(0,100) for i in range(j)]
        tamanio_morral = 10 * j

        n = len(valores)

        i = 0

        resultado = morral(tamanio_morral,pesos,valores,n)
        
        tam_val.append(n)
        iter.append(i)
        print('cuando N =',n, ' llama: ', i, '(2**(n+1)) - 1 = ',(2**(n+1)) - 1)
        print('el valor maximo seria: ',resultado)

    plt.scatter(tam_val,iter)
    plt.title('Iteraciones que necesita')
    plt.xlabel('Tamanio de lista')
    plt.ylabel('Iteraciones')
    plt.legend(loc=2)
    plt.show()