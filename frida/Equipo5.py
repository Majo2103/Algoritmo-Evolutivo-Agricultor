#Equipo 5
# Integrantes: María José Velázquez (200078), Frida Márquez (202919), Gerardo Guerrero (203214)
# Description: Este archivo contiene la implementación de un algoritmo evolutivo para la optimización de la distribución de cultivos en un campo agrícola.

import random
import numpy as np

'''Diccionario que contiene información sobre diversos tipos de vegetales. 
   Cada vegetal está representado por una clave (nombre del vegetal) y un diccionario de atributos:
     - 'nombre': Nombre común del vegetal.
     - 'agua_necesaria': Cantidad de agua necesaria para su óptimo crecimiento.
     - 'cantidad_de_luz': Cantidad de luz solar necesaria.
     - 'temporada': Temporada principal de crecimiento del vegetal.
     - 'cuidado': Mano de obra necesaria para el crecimiento del vegetal. 
     - 'precio_por_kilo': Precio promedio por kilogramo del vegetal en el mercado.
     - 'peso_m2': Producción del vegetal por metro cuadrado.''' 

vegetales = { 
    "jitomate": {
        "nombre": "Jitomate",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 30,
        "peso_m2": 2
    },

    "cebolla": {
        "nombre": "Cebolla",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Otoño/Invierno",
        "cuidado": "Bajo",
        "precio_por_kilo": 30,
        "peso_m2": 4
    },

    "maiz": {
        "nombre": "Maíz",
        "agua_necesaria": "Alta",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 30,
        "peso_m2": .5
    },

    "pepino": {
        "nombre": "Pepino",
        "agua_necesaria": "Alta",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 30,
        "peso_m2": 10
    },
    "chile": {
        "nombre": "Chile",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 30,
        "peso_m2": 3
    },
    "pimiento": {
        "nombre": "Pimiento",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Media",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 50,
        "peso_m2": 2

    },
    "zanahoria": {
        "nombre": "Zanahoria",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Otoño/Invierno",
        "cuidado": "Moderado",
        "precio_por_kilo": 10,
        "peso_m2": 5
    },
    "lechuga": {
        "nombre": "Lechuga",
        "agua_necesaria": "Alta",
        "cantidad_de_luz": "Media",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 20,
        "peso_m2": .5
    },
    "papa": {
        "nombre": "Papa",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 40,
        "peso_m2": 5
    },
    "calabaza": {
        "nombre": "Calabaza",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 15,
        "peso_m2": 6
    },
    "espinaca": {
        "nombre": "Espinaca",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Media",
        "temporada": "Otoño/Invierno",
        "cuidado": "Bajo",
        "precio_por_kilo": 25,
        "peso_m2": 2
    },
    "nopal": {
        "nombre": "Nopal",
        "agua_necesaria": "Baja",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Todo el año",
        "cuidado": "Bajo",
        "precio_por_kilo": 20,
        "peso_m2": 7
    },
    "ajo": {
        "nombre": "Ajo",
        "agua_necesaria": "Baja",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Otoño/Invierno",
        "cuidado": "Bajo",
        "precio_por_kilo": 80,
        "peso_m2": 3
    },
    "betabel": {
        "nombre": "Betabel",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Otoño/Invierno",
        "cuidado": "Moderado",
        "precio_por_kilo": 30,
        "peso_m2": 4
    },
    "albahaca": {
        "nombre": "Albahaca",
        "agua_necesaria": "Baja",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Bajo",
        "precio_por_kilo": 120,
        "peso_m2": 1.5
    }   
}

class Vegetal:
    def __init__(self, nombre, cantidad_de_luz, agua_necesaria, temporada, cuidado, precio_por_kilo, peso_m2):
        # Constructor de la clase Vegetal, inicializa un nuevo objeto con características específicas de un vegetal.
        self.nombre = nombre  
        self.cantidad_de_luz = cantidad_de_luz  
        self.agua_necesaria = agua_necesaria  
        self.temporada = temporada  
        self.cuidado = cuidado  
        self.precio_por_kilo = precio_por_kilo  
        self.peso_m2 = peso_m2  

    def __eq__(self, other):
        # Método especial para comparar este objeto con otro, considerando la igualdad basada en el nombre del vegetal.
        if isinstance(other, Vegetal):  
            return self.nombre == other.nombre  
        return False  

    def __hash__(self):
        # Método que devuelve un valor hash para el objeto, permitiendo su uso en estructuras de datos que utilizan hashing, como los diccionarios.
        return hash(self.nombre)  

    def __repr__(self):
        # Método que devuelve una representación en cadena del objeto para su visualización en consola.
        return self.nombre  
    
class Genotipo:
    def __init__(self, cultivos={}):
        # Constructor de la clase Genotipo, inicializa un nuevo objeto que representa un genotipo con un conjunto de vegetales.
        self.cultivos = cultivos  # Inicializa un diccionario de cultivos, donde cada clave es un objeto Vegetal y el valor es el porcentaje de espacio que ocupa.
        self.utilidad = 0  # Inicializa la utilidad del genotipo como 0.

    def __str__(self):
        # Método especial que define la representación en cadena de un objeto Genotipo, utilizado cuando se imprime el objeto.
        utilidad_formateada = '${:,.0f}'.format(self.utilidad)  # Formatea la utilidad a formato monetario con separadores de miles.
        cadena = 'Utilidad: ' + utilidad_formateada + '\n'  
        for cultivo in self.cultivos:
            # Itera sobre cada cultivo en el diccionario y agrega su nombre y porcentaje a la cadena de salida.
            cadena += str(cultivo) + ': ' + str(round(self.cultivos[cultivo], 3) * 100) + '%\n'
        return cadena  # Devuelve la cadena construida con la utilidad y los detalles de los cultivos.

    def __repr__(self):
        # Método que define cómo se representa el objeto Genotipo en la consola, útil para debugging y logging.
        return self.__str__()  


def generar_numeros_random(n, min_gap=0.05):
    n = n + 1  # Ajusta n para el cálculo de los cortes, considerando que el último corte siempre será 1.0.
    if n < 1:
        return []  # Retorna una lista vacía si no es posible generar ningún número (n < 1).
    if n == 1:
        return [1.0]  # Retorna una lista con un solo número, 1.0, si n es exactamente 1.

    cuts = [0]  # Inicia la lista de cortes con 0, el punto de inicio para el primer corte.
    while len(cuts) < n:
        # Genera un nuevo corte sumando un mínimo garantizado (min_gap) más un valor aleatorio.
        next_cut = cuts[-1] + min_gap + random.random() * (1 - cuts[-1] - (n - len(cuts)) * min_gap)
        if next_cut <= 1.0:
            cuts.append(next_cut)  # Añade el nuevo corte si es menor o igual a 1.0.

    cuts[-1] = 1.0  # Asegura que el último corte sea exactamente 1.0.

    numeros_random = [cuts[i] - cuts[i - 1] for i in range(1, len(cuts))]  # Calcula los intervalos entre cortes como números aleatorios.

    return numeros_random  # Retorna la lista de números aleatorios generados.

lista_cultivos = vegetales  # Asigna el diccionario de vegetales a la variable lista_cultivos.

def crear_combinacion_aleatoria(n, lista_cultivos):
    genotipo = {}  # Inicializa un diccionario vacío para el genotipo.
    random_numbers = generar_numeros_random(n)  # Genera una lista de números aleatorios que suman 1.
    cultivos = list(lista_cultivos.copy())  # Crea una copia de la lista de cultivos para poder modificarla.
    
    for i in range(n):
        # Itera n veces para seleccionar cultivos y asignarles porcentajes aleatorios.
        cultivo = random.choice(cultivos)  # Elige un cultivo aleatorio de la lista.
        cultivos.remove(cultivo)  # Elimina el cultivo elegido de la lista para evitar repetición.
        porcentaje = random.choice(random_numbers)  # Elige un porcentaje aleatorio de la lista de números.
        random_numbers.remove(porcentaje)  # Elimina el porcentaje elegido para evitar repetición.
        cultivo = lista_cultivos[cultivo]  # Obtiene los detalles del cultivo seleccionado.
        vegetal = Vegetal(cultivo["nombre"], cultivo["cantidad_de_luz"], cultivo["agua_necesaria"],
                          cultivo["temporada"], cultivo["cuidado"], cultivo["precio_por_kilo"], cultivo["peso_m2"])
        genotipo[vegetal] = porcentaje  # Asigna el porcentaje al vegetal en el genotipo.
    return genotipo  # Retorna el genotipo creado.

def inicializar_poblacion(min_cultivos, tam_poblacion, lista_cultivos):
    poblacion = []  # Inicializa una lista vacía para la población.
    for _ in range(tam_poblacion):
        # Itera para cada miembro de la población que se desea inicializar.
        n = random.randint(min_cultivos, len(lista_cultivos))  # Determina al azar cuántos cultivos tendrá este genotipo.
        genotipo = crear_combinacion_aleatoria(n, lista_cultivos)  # Crea un genotipo aleatorio.
        genotipo = Genotipo(genotipo)  # Convierte el diccionario de cultivos en un objeto Genotipo.
        poblacion.append(genotipo)  # Añade el nuevo genotipo a la población.
    return poblacion  # Retorna la población inicializada.


def evaluar(genotipo:Genotipo = {}, m2 = int, sol = str, agua = str, temp = str):
    # Evalúa la utilidad de un genotipo dado en un ambiente específico.
  
    if genotipo.utilidad != 0:  # Si el genotipo ya ha sido evaluado, devuelve la utilidad previamente calculada.
        return genotipo.utilidad

    utilidad_total = 0  # Inicializa la utilidad total acumulada para este genotipo.
    for cultivo in genotipo.cultivos:
        # Calcula el ingreso potencial de cada cultivo en el genotipo.
        ingreso = cultivo.peso_m2 * m2 * genotipo.cultivos[cultivo] * cultivo.precio_por_kilo

        costo = 0  # Inicializa el costo total para este cultivo.
        # Establece un costo base de mano de obra por metro cuadrado.
        base_mano_obra = 4  # Costo base de mano de obra por metro cuadrado.
        if cultivo.cuidado == 'Bajo':
            base_mano_obra *= 0.5
        if cultivo.cuidado == 'Alto':
            base_mano_obra *= 1.5

        costo_mano_obra = base_mano_obra * m2  # Calcula el costo total de mano de obra.
        costo += costo_mano_obra  # Acumula el costo de mano de obra al costo total.

        probabilidad = probabilidad_crecimiento(cultivo, sol, agua, temp)  # Calcula la probabilidad de éxito del cultivo.
        utilidad = ingreso - costo  # Calcula la utilidad neta después de costos.
        utilidad_esperada = utilidad * probabilidad  # Ajusta la utilidad por la probabilidad de éxito.
        utilidad_total += utilidad_esperada  # Suma la utilidad ajustada a la utilidad total del genotipo.

    genotipo.utilidad = utilidad_total  # Asigna la utilidad total calculada al genotipo.
    return utilidad_total  # Devuelve la utilidad total calculada para este genotipo.

def probabilidad_crecimiento(cultivo, sol, agua, temp):
    # Calcula la probabilidad de crecimiento exitoso de un cultivo dadas las condiciones ambientales.
    prob = 1  # Inicializa la probabilidad base como 1 (100%).

    # Ajusta la probabilidad basada en la correspondencia entre la necesidad de agua del cultivo y la disponibilidad actual.
    if agua != cultivo.agua_necesaria:
        if cultivo.agua_necesaria == 'Alta':
            if agua == 'Baja':
                prob *= 0.3
            if agua == 'Moderada':
                prob *= 0.7
        if cultivo.agua_necesaria == 'Baja':
            if agua == 'Alta':
                prob *= 0.3
            if agua == 'Moderada':
                prob *= 0.7
        if cultivo.agua_necesaria == 'Moderada':
            prob *= 0.7

    # Ajusta la probabilidad según si la temporada actual coincide con la temporada óptima del cultivo.
    if temp != cultivo.temporada:
        prob *= 0.6

    # Ajusta la probabilidad según si la cantidad de luz actual coincide con la necesidad de luz del cultivo.
    if sol != cultivo.cantidad_de_luz:
        prob *= 0.8

    return prob  # Devuelve la probabilidad ajustada.


def seleccionar(poblacion, m2, sol, agua, temp, porcentaje=0.3):
    # Evalúa y ordena la población de genotipos según su utilidad en un ambiente específico.

    # Crea un diccionario que mapea cada genotipo a su utilidad evaluada según las condiciones ambientales dadas.
    utilidades = {individuo: evaluar(individuo, m2, sol, agua, temp) for individuo in poblacion}

    # Convierte el diccionario a una lista de tuplas y ordena descendientemente por utilidad.
    poblacion_ordenada = list(utilidades.items())
    poblacion_ordenada.sort(key=lambda x: x[1], reverse=True)
    
    # Calcula el número de genotipos a seleccionar basado en el porcentaje especificado.
    num_seleccionados = int(len(poblacion) * porcentaje)
    
    # Obtiene las sublistas de genotipos seleccionados y no seleccionados basándose en el número calculado.
    seleccionados = poblacion_ordenada[:num_seleccionados]
    seleccionados = [individuo[0] for individuo in seleccionados]  # Extrae solo los genotipos de la lista de tuplas.
    
    no_seleccionados = poblacion_ordenada[num_seleccionados:]
    no_seleccionados = [individuo[0] for individuo in no_seleccionados]  # Extrae solo los genotipos de la lista de tuplas.
    
    # Devuelve las listas de genotipos seleccionados y no seleccionados.
    return seleccionados, no_seleccionados



def normalizar(genotipo):
    # Normaliza las proporciones de cultivos en un genotipo para que sumen 1.
    suma_total = sum(genotipo.cultivos.values()) 
    genotipo.cultivos = {cultivo: prop / suma_total for cultivo, prop in genotipo.cultivos.items()}


def cruza_genotipos(min_cult, genotipo1, genotipo2, variacion=0.12):
    # Cruza dos genotipos para producir descendientes con variabilidad genética.
    todos_los_cultivos = set(genotipo1.cultivos.keys()).union(set(genotipo2.cultivos.keys())) # Obtiene todos los cultivos presentes en ambos genotipos.
    
    # Inicializar descendientes con todos los cultivos a 0
    cultivos_descendiente1 = {}
    cultivos_descendiente2 = {}
    
    # Combinar y variar los cultivos de ambos genotipos
    for cultivo in todos_los_cultivos:
        prop1 = genotipo1.cultivos.get(cultivo, 0)
        prop2 = genotipo2.cultivos.get(cultivo, 0)
        mid = (prop1 + prop2) / 2
        
        # Calcular nueva proporción basada en una media ponderada y una variación
        nueva_prop1 = mid + random.uniform(-variacion, variacion)
        nueva_prop2 = mid + random.uniform(-variacion, variacion)
        
        if nueva_prop1 > 0.05:
            cultivos_descendiente1[cultivo] = nueva_prop1
        if nueva_prop2 > 0.05:
            cultivos_descendiente2[cultivo] = nueva_prop2
    
    # Asegurar el mínimo de cultivos
    while len(cultivos_descendiente1) < min_cult:
        cultivo_extra = random.choice(list(todos_los_cultivos))
        cultivos_descendiente1[cultivo_extra] = 0.05 + random.uniform(0, 0.1)
    
    while len(cultivos_descendiente2) < min_cult:
        cultivo_extra = random.choice(list(todos_los_cultivos))
        cultivos_descendiente2[cultivo_extra] = 0.05 + random.uniform(0, 0.1)
    
    # Crear instancias de Genotipo para los descendientes
    descendiente1 = Genotipo(cultivos=cultivos_descendiente1)
    descendiente2 = Genotipo(cultivos=cultivos_descendiente2)

    # Normalizar los descendientes para que las proporciones sumen 1
    normalizar(descendiente1)
    normalizar(descendiente2)
    
    return descendiente1, descendiente2 # Devolver los descendientes generados

def algoritmo_evolutivo(min_cult, pob_inicial, num_generaciones, m2, sol, agua, temp):
    # Define un algoritmo evolutivo que optimiza una población de genotipos bajo condiciones ambientales específicas.

    # Inicializa la población con una cantidad definida de individuos.
    poblacion = inicializar_poblacion(min_cult, pob_inicial, lista_cultivos)
    
    # Ejecuta el ciclo evolutivo para el número especificado de generaciones.
    for _ in range(num_generaciones):
        # Selecciona una subpoblación de individuos basados en su rendimiento y condiciones dadas.
        seleccionados, no_seleccionados = seleccionar(poblacion, m2, sol, agua, temp)
        
        # Re-inicializa la mitad de la población que no fue seleccionada para introducir variabilidad.
        no_seleccionados = inicializar_poblacion(min_cult, int(pob_inicial * 0.5), lista_cultivos)
        
        # Combina los seleccionados con los nuevos no seleccionados para formar la próxima generación.
        nueva_generacion = seleccionados + no_seleccionados
        
        # Complementa la nueva generación hasta alcanzar el tamaño inicial de la población.
        while len(nueva_generacion) < pob_inicial:
            # Selecciona dos genotipos al azar de los seleccionados para cruzar.
            genotipo1 = random.choice(seleccionados)
            genotipo2 = random.choice(seleccionados)
            
            # Cruza los genotipos seleccionados para crear dos descendientes.
            descendiente1, descendiente2 = cruza_genotipos(min_cult, genotipo1, genotipo2)
            
            # Añade los descendientes a la nueva generación.
            nueva_generacion.append(descendiente1)
            nueva_generacion.append(descendiente2)
        
        # Actualiza la población con la nueva generación formada.
        poblacion = nueva_generacion
            
    # Devuelve el mejor genotipo de la última selección.
    return seleccionados[0]



class ParametrosAlgoritmo:
    def __init__(self, pob_inicial, num_generaciones):
        # Constructor de la clase que inicializa los parámetros del algoritmo evolutivo.
        self.pob_inicial = pob_inicial  # Número inicial de individuos en la población.
        self.num_generaciones = num_generaciones  # Número total de generaciones a ejecutar.

    def __str__(self):
        # Método que devuelve una representación en cadena de los parámetros actuales del algoritmo.
        return f"pob_inicial: {self.pob_inicial}, num_generaciones: {self.num_generaciones}"


def evaluar_parametros(parametros, min_cult, m2, sol, agua, temp, k=5):
    # Función para evaluar y optimizar los parámetros de un algoritmo evolutivo a través de múltiples ejecuciones.
    while True:
        utilidades = []
        for i in range(k):
            # Ejecuta el algoritmo evolutivo 'k' veces para obtener diferentes muestras de desempeño.
            top = algoritmo_evolutivo(min_cult, parametros.pob_inicial, parametros.num_generaciones, m2, sol, agua, temp)
            utilidades.append(top)
        
        # Calcula la utilidad media y la desviación estándar de las utilidades observadas.
        utilidad_media = np.mean([c.utilidad for c in utilidades])
        desv_estandar_utilidad = np.std([c.utilidad for c in utilidades])
        # Calcula el coeficiente de variación para determinar la estabilidad de las utilidades.
        cv = desv_estandar_utilidad / utilidad_media
            
        if cv < 0.01:
            # Si el coeficiente de variación es menor que 0.01, considera los parámetros como óptimos y finaliza.
            return utilidades[0], parametros
        else:
            # Si no, muta los parámetros para intentar encontrar una configuración más estable.
            mutar_parametros(parametros)

    
def mutar_parametros(parametros):
    # Modifica aleatoriamente los valores de `pob_inicial` y `num_generaciones` dentro de un rango.
    parametros.pob_inicial = max(parametros.pob_inicial + random.randint(-10, 50), parametros.pob_inicial)
    parametros.num_generaciones = max(parametros.num_generaciones + random.randint(-10, 50), parametros.num_generaciones)

    
def meta_algoritmo_evolutivo(min_cult, m2, sol, agua, temp):
    # Inicializa los parámetros del algoritmo evolutivo aleatoriamente y evalúa su eficacia.
    parametros = ParametrosAlgoritmo(random.randint(50, 100), random.randint(1, 100))
    # Devuelve el resultado de evaluar los parámetros, buscando optimizarlos.
    return evaluar_parametros(parametros, min_cult, m2, sol, agua, temp, k=5)


def ejecutar_meta_algoritmo_interactivo():
    # Muestra un mensaje de bienvenida y solicita la entrada de datos ambientales para iniciar la optimización.
    print("\nBienvenido al sistema de optimización de algoritmo evolutivo para cultivos.")
    print("Por favor, introduce los siguientes parámetros ambientales para comenzar la optimización:")

    while True:  # Inicia un bucle para solicitar y validar las entradas del usuario.
        try:
            # Solicita al usuario que introduzca el área en metros cuadrados disponible para cultivos.
            m2 = float(input("\nIntroduce el área en metros cuadrados (m2) disponible para los cultivos: "))
            # Solicita al usuario que especifique la cantidad de luz solar que recibe el campo.
            sol = input("Introduce la cantidad de luz solar que recibe el campo (Pleno sol o Media): ")
            # Solicita al usuario que especifique la cantidad de agua disponible.
            agua = input("Introduce la cantidad de agua que recibe el campo (Baja, Moderada o Alta): ")
            # Solicita al usuario que especifique la temporada en la que desea plantar.
            temp = input("Introduce la temporada en la que te gustaría plantar los vegetales (Primavera/Verano u Otoño/Invierno): ")

            # Valida las entradas para asegurarse de que son aceptables según los criterios definidos.
            if sol not in ['Pleno sol', 'Media'] or agua not in ['Baja', 'Moderada', 'Alta'] or temp not in ['Primavera/Verano', 'Otoño/Invierno']:
                # Informa al usuario si alguna entrada es incorrecta y solicita la reintroducción de los datos.
                print("Algunos de los valores introducidos son inválidos. Por favor, intenta de nuevo asegurándote de que la cantidad de luz solar, la disponibilidad de agua y la temporada estén correctamente especificadas.")
                continue  # Repite el bucle si las entradas no son válidas.

            break  # Sale del bucle si todas las entradas son válidas.

        except ValueError:
            # Captura y maneja errores si el usuario introduce un tipo de dato incorrecto para el área.
            print("Has introducido un valor inválido para el área. Por favor, introduce un número válido.")

    # Anuncia que se va a mostrar la mejor distribución de cultivos después de ejecutar el meta algoritmo.
    print("\nLa mejor distribución de cultivos para tu campo es:")
    # Ejecuta el meta algoritmo con los parámetros validados.
    mejores_parametros = meta_algoritmo_evolutivo(3, m2=m2, sol=sol, agua=agua, temp=temp)
    
    # Muestra los mejores parámetros resultantes de la optimización.
    print(mejores_parametros[0])

# Llama a la función para iniciar el proceso interactivo.
ejecutar_meta_algoritmo_interactivo()
