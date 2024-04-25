
vegetales = {
    "jitomate": {
        "nombre": "Jitomate",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "tiempo_de_crecimiento": "60-90 días",
        "cuidado": "Moderado",
        "precio_por_kilo": "$10-$20",
    },
    "cebolla": {
        "nombre": "Cebolla",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Otoño/Invierno",
        "tiempo_de_crecimiento": "100-120 días",
        "cuidado": "Bajo",
        "precio_por_kilo": "$5-$10",
    },
    "maiz": {
        "nombre": "Maíz",
        "agua_necesaria": "Alta",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "tiempo_de_crecimiento": "60-100 días",
        "cuidado": "Moderado",
        "precio_por_kilo": "$2-$5",
    },
    "pepino": {
        "nombre": "Pepino",
        "agua_necesaria": "Alta",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "tiempo_de_crecimiento": "50-70 días",
        "cuidado": "Moderado",
        "precio_por_kilo": "$5-$10",
    },
    "chile": {
        "nombre": "Chile",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "tiempo_de_crecimiento": "60-90 días",
        "cuidado": "Moderado",
        "precio_por_kilo": "$3-$8",
    }
}


class Vegetal:
    def _init_(self, nombre, sol, agua, temporada, tiempo_crecimiento, mano_obra, precio_kilo):
        self.nombre = nombre
        self.sol = sol #cantidad de luz que necesita el cultivo
        self.agua = agua #cantidad de agua que necesita el cultivo
        self.temporada = temporada 
        self.tiempo_crecimiento = tiempo_crecimiento 
        self.mano_obra = mano_obra
        self.precio_kilo = precio_kilo

class Genotipo:
    def _init_(self, vegetales):
        self.vegetales = vegetales  # Lista de tuplas (Vegetal, porcentaje)