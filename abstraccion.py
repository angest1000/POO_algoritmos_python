#Se debe pensar que interfaz se le va a dar
# al usuario, para saber que metodos y atributos
# son publicos o privados

class Lavadora:
    def __init__(self):
        pass

    def lavar(self,temperatura='caliente'):
        self._llenar_tanque_agua(temperatura)
        self._annadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_agua(self,temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _annadir_jabon(self):
        print('Annadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()