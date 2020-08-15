class CasillaDeVotacion:
    def __init__ (self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None
    
    def __repr__(self):
        return f'<CasillaDeVotacion,  identificador: ({self._identificador}),pais: ({self._pais})>'

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self,region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self._pais}.')

casilla = CasillaDeVotacion(123,['Ciudad de Mexico','Morelos'])
print('casilla: ',type(casilla))
print('Casilla: ',casilla)
print('casilla.identificador: ',casilla._identificador)
print('casilla.region: ',casilla.region)
casilla.region = 'Ciudad de Mexico'
print('casilla.region: ',casilla.region)
casilla.region = 'Bogota'
print('casilla.region: ',casilla.region)
