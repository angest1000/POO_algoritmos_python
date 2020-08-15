#Tutorial extraido de: 
# https://recursospython.com/guias-y-manuales/clases-metodos-magicos-y-propiedades/

#Ejemplo:

class Time:
    def __init__(self,h=0,m=0,s=0):
        self.h = h
        self.m = m
        self.s = s

    def __repr__(self):
        return f'<Time {self.h:2}:{self.m:02}:{self.s:02}>'

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self,value):
        if not isinstance(value,int):
            raise TypeError('Se requiere un valor int.')
        self._h = value

# a = Time("Hola mundo",23,10)
# a.h = "Hola mundo"
a = Time(14,23,10)
print('a: ',a.h,a.m,a.s)

# b = Time(m=30)
# print('b: ',b.h,b.m,b.s)

# print(a) 
# Antes de definir __repr__: <__main__.Time object at 0x7f6ab4ad8f90>
# Despues de definir __repr__: <Time 14:23:10>


