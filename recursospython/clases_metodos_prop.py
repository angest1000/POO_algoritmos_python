#Tutorial extraido de: 
# https://recursospython.com/guias-y-manuales/clases-metodos-magicos-y-propiedades/

#Ejemplo:
from functools import total_ordering, wraps
import operator

#Decorador para evitar que se agreguen valores 
# no int a nuestra instancia tiempo
def _int_requerido(f):
    @wraps(f)
    def wrapper(self, value):
        if not isinstance(value,int):
            raise TypeError('Se requiere un valor int')
        return f(self,value)
    return wrapper

def _time_required(f):
    @wraps(f)
    def wrapper(self,other):
        if not isinstance(other,Tiempo):
            raise TypeError('Solo se pueden operar instancias Tiempo')
        return f(self,other)
    return wrapper

def _balance(a,b):
    if b >= 0:
        while b >=60:
            a += 1
            b -= 60
    elif b < 0:
        while b < 0:
            a -= 1
            b += 60
    return a,b

#El decorador total_ordering construira las demas operaciones
# con base en las que ya escribimos
@total_ordering
class Tiempo: #Horas, minutos, segundos
    def __init__(self,h=0,m=0,s=0):
        self.h = h
        self.m = m
        self.s = s

    def __repr__(self):
        return f'<Tiempo {self.h:2}:{self.m:02}:{self.s:02}>'

    def _operacion(self,other,method):
        h = method(self.h,other.h)
        m = method(self.m,other.m)
        s = method(self.s,other.s)
        return Tiempo(h,m,s)

    @_time_required
    def __add__(self,other):
        return self._operacion(other,operator.add)

    @_time_required
    def __sub__(self,other):
        return self._operacion(other,operator.sub)

    # Agregando la comparacion ==
    @_time_required
    def __eq__(self,other):
        return (self.h == other.h 
                and self.m == other.m 
                and self.s == other.s)

    #Ahora agregando la comparacion a < b:
    @_time_required
    def __lt__(self,other):
        if self.h < other.h:
            return True
        if self.h > other.h:
            return False
        if self.m < other.m:
            return True
        if self.m > other.m:
            return False
        return self.s < other.s
    
    @property
    def h(self):
        return self._h

    @h.setter
    @_int_requerido
    def h(self,value):
        self._h = value

    @property
    def m(self):
        return self._m

    @m.setter
    @_int_requerido
    def m(self,value):
        self._m = value
        self._h, self._m = _balance(self._h,self._m)

    @property
    def s(self):
        return self._s

    @s.setter
    @_int_requerido
    def s(self,value):
        self._s = value
        self._m,self._s = _balance(self._m,self._s)

# a = Tiempo("Hola mundo",23,10)
# a.h = "Hola mundo"
# a = Tiempo(14,23,10)
# a = Tiempo(2,80,95)
# print('a: ',a.h,a.m,a.s)
# print('a:',a)
# b = Tiempo(m=30)
# print('b: ',b.h,b.m,b.s)

# print(a) 
# Antes de definir __repr__: <__main__.Tiempo object at 0x7f6ab4ad8f90>
# Despues de definir __repr__: <Tiempo 14:23:10>

#Agregando el metodo __add__ para sumar dos instancias tiempo
# a = Tiempo(2,16,48)
# b = Tiempo(3,51,22)
# print(a+b)
# print(b-a)

#Probando el decorador para evitar que se sumen 
# instancias Tiempo con otros objetos
# a=Tiempo(2,16,48)
# print(a+10)

#Probando el comparador ==
# print(Tiempo(2,16,48) == Tiempo(2,16,48))
# print(Tiempo(2,16,48) == Tiempo(8,16,21))

#Probando el comparador a < b:
# print(Tiempo(2,16,48) < Tiempo(2,16,48))
# print(Tiempo(2,16,48) < Tiempo(8,16,21))
# print(Tiempo(2,16,48) < Tiempo(2,16,21))

#Probando todos los comparadores:

a = Tiempo(2,16,48)
b = Tiempo(8,16,21)
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
