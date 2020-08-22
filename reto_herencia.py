#Crear una clase con subclases

class Motocicleta:
    def __init__(self,nombre,marca,anio,cc,cilindros,capacidad_tanque,velocidad_ini,velocidad_fin):
        self.nombre = nombre
        self.marca= marca
        self.anio = anio        
        self.cc = cc
        self.cilindros = cilindros
        self.capacidad_tanque = capacidad_tanque
        self.velocidad_ini = velocidad_ini
        self.velocidad_fin = velocidad_fin

    def acelera(self,tiempo):
        return (self.velocidad_fin - self.velocidad_ini) / tiempo

    
class MotoDeportiva(Motocicleta):
    def __init__(self,nombre,marca,anio,cc,cilindros,capacidad_tanque,velocidad_ini,velocidad_fin):
        super().__init__(nombre,marca,anio,cc,cilindros,capacidad_tanque,velocidad_ini,velocidad_fin)

    def viaje_carretera(self,tiempo):
        if tiempo < 120 : 
            return 'La motocicleta rueda sin problemas'
        else:
            return 'Motor sobrecalentado'

    def ladear_en_curva(self):
        return 'Ladea sin problema'

    def caballito(self):
        return 'La motocicleta se levanta al acelerar'

class MotoCrusier(Motocicleta):
    def __init__(self,nombre,marca,anio,cc,cilindros,capacidad_tanque,velocidad_ini,velocidad_fin):
        super().__init__(nombre,marca,anio,cc,cilindros,capacidad_tanque,velocidad_ini,velocidad_fin)

    def viaje_carretera(self,tiempo):
        if tiempo < 300 : 
            return 'La motocicleta rueda sin problemas'
        else:
            return 'Motor sobrecalentado'
    

    def ladear_en_curva(self):
        return 'Se raspa el posapies'
        
class MotoDobleProposito(Motocicleta):
    def __init__(self,nombre,marca,anio,cc,cilindros,capacidad_tanque,velocidad_ini,velocidad_fin):
        super().__init__(nombre,marca,anio,cc,cilindros,capacidad_tanque,velocidad_ini,velocidad_fin)

    def viaje_carretera(self,tiempo):
        if tiempo < 300 : 
            return 'La motocicleta rueda sin problemas'
        else:
            return 'Motor sobrecalentado'

    def ladear_en_curva(self):
        return 'Ladea sin problema'

moto_Pedro = MotoCrusier('Iron 883','Harley Davidson',2012,883,2,12,0,80)
moto_Juan = MotoDeportiva('CBR1000','Honda',2018,1000,2,10,0,80)
moto_Angel = MotoDobleProposito('FZ','Yamaha',2015,153,1,10,0,75)
moto_Andres = MotoDobleProposito('XRE300','Honda',2020,300,1,13.5,0,110)
moto_Miguel = MotoCrusier('S40','Susuki',2019,650,1,9,0,85)

print('Moto de Pedro: '+moto_Pedro.nombre+' '+moto_Pedro.marca+' Aceleracion: ',moto_Pedro.acelera(tiempo=7))
print('Moto de Juan: '+moto_Juan.nombre+' '+moto_Juan.marca+' Aceleracion: ',moto_Juan.acelera(tiempo=6))
print('Moto de Angel: '+moto_Angel.nombre+' '+moto_Angel.marca+' Aceleracion: ',moto_Angel.acelera(tiempo=15))
print('Moto de Andres: '+moto_Andres.nombre+' '+moto_Andres.marca+' Aceleracion: ',moto_Andres.acelera(tiempo=12))
print('Moto de Miguel: '+moto_Miguel.nombre+' '+moto_Miguel.marca+' Aceleracion: ',moto_Miguel.acelera(tiempo=9))