#Decomposicion
# Modelando un automovil

def Automovil:
    def __init__(self,nombre,modelo,marca,color,transmision = 'Estandar',puertas):
        self.nombre = nombre
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.transmision = transmision
        self.puertas = puertas
        self.Asientos = Asientos(numero_asientos=5,material='Piel')
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros = 4)

    def acelerar(self,tipo='despacio'):
        if tipo == 'rapida'
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self._estado = 'en_movimiento'


class Motor:
    def __init__(self,cilindros, tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self,cantidad):
        pass

class Stereo:
    def __init__(self,radio='si',aux='si'):
        self.radio = radio
        self.aux = aux

    def tocar_radio(self,frecuencia='fm',estacion,volumen):
        if Stereo.radio == 'si':
            return f'Tocar la estacion {estacion} de {frecuencia} en {volumen} de volumen'
        else:
            return 'No tienes ni radio xD'

    def escuchar_dispositivo_externo(self,dispositivo,volumen):
        if Stereo.aux = 'si':
            return f'Escuchando musica en {dispositivo} en {volumen} de volumen'
        else:
            return 'Tu stereo no cuenta con Aux'

class Asientos:
    def __init__(self,numero_asientos,material):
        self.numero_asientos = numero_asientos
        self.material = material
        self._relleno = 'esponja_industrial'
    
    def reclinar(self,num_asiento,reclinar='si'):
        if reclinar == 'si':
            return f'Asiento {num_asiento} reclinado'
        else:
            return f'Asiento {num_asiento} derecho'
