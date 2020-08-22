# Big O Notation

#Ley de la suma

def f(n):
    for i in range(n): 
        print(i)        # n pasos

    for i in range(n):
        print(i)        # n pasos

# O(n) + O(n) = O(n + n) = O(2n) = O(n)

#Ley de la suma

def f(n):
    for i in range(n):
        print(i)        #n pasos

    for i in range(n*n):
        print(i)        #n*n = n^2 pasos

# O(n) + O(n * n) = O(n + n^2) = O(n^2)

#Ley de la multiplicacion

def f(n):
    for i in range(n):      #n pasos
        for j in range(n):  #n pasos
            print(i,j)      #n*n pasos

#O(n) * O(n) = O(n * n) = O(n^2)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) * fibonacci(n-2) 

#O(2**n)
