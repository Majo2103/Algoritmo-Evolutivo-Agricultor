
vegetales = { #diccionario de vegetales que contine todos los posibles vegetales y su información
    "jitomate": {
        "nombre": "Jitomate",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 15.00,
        "peso_m2": 8
    },

    "cebolla": {
        "nombre": "Cebolla",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Otoño/Invierno",
        "cuidado": "Bajo",
        "precio_por_kilo": 7.5,
        "peso_m2": 4
    },

    "maiz": {
        "nombre": "Maíz",
        "agua_necesaria": "Alta",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 3.5,
        "peso_m2": .5
    },

    "pepino": {
        "nombre": "Pepino",
        "agua_necesaria": "Alta",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 7.5,
        "peso_m2": 10
    },
    "chile": {
        "nombre": "Chile",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 5.5,
        "peso_m2": 3
    },
    "pimiento": {
        "nombre": "Pimiento",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Media",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 4.5,
        "peso_m2": 2

    },
    "zanahoria": {
        "nombre": "Zanahoria",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Otoño/Invierno",
        "cuidado": "Moderado",
        "precio_por_kilo": 2,
        "peso_m2": 5
    },
    "lechuga": {
        "nombre": "Lechuga",
        "agua_necesaria": "Alta",
        "cantidad_de_luz": "Media",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 4,
        "peso_m2": .5
    },
    "papa": {
        "nombre": "Papa",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 3,
        "peso_m2": 5
    }

    
}


class Vegetal:
    def __init__(self, nombre, sol, agua, temporada, tiempo_crecimiento, mano_obra, precio_kilo, porcentaje,peso_m2):
        self.nombre = nombre #nombre del vegetal
        self.sol = sol #cantidad de luz que necesita el cultivo: plena luz, sombra
        self.agua = agua #cantidad de agua que necesita el cultivo: Alta, Baja, Moderada
        self.temporada = temporada #temporada en la que crece: "Otoño/Invierno" o "Primavera/Verano"
        #checar que tan viable es ver tiempo
        #self.tiempo_crecimiento = tiempo_crecimiento 
        self.mano_obra = mano_obra #cuidado : Moderado, Alto, Bajo
        self.precio_kilo = precio_kilo #double
        self.porcentaje = porcentaje #double
        self.peso_m2 = peso_m2 #double

class Genotipo:
    def __init__(self, cultivos = []): #recibe un arreglo de vegetales
        self.cultivos = cultivos  