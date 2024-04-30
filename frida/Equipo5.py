#Equipo 5
# Integrantes: María José Velázquez (200078), Frida Márquez (202919), Gerardo Guerrero (203214)
# Description: Este archivo contiene la implementación de un algoritmo evolutivo para la optimización de la distribución de cultivos en un campo agrícola.

import random

'''Diccionario que contiene información sobre diversos tipos de vegetales. 
   Cada vegetal está representado por una clave (nombre del vegetal) y un diccionario de atributos:
     - 'nombre': nombre común del vegetal.
     - 'agua_necesaria': cantidad de agua necesaria para su óptimo crecimiento.
     - 'cantidad_de_luz': cantidad de luz solar necesaria.
     - 'temporada': temporada principal de crecimiento del vegetal.
     - 'cuidado': mano de obra necesaria para el crecimiento del vegetal. 
     - 'precio_por_kilo': precio promedio por kilogramo del vegetal en el mercado.
     - 'peso_m2': producción promedio del vegetal por metro cuadrado.''' #CHECAR ESTE Y CUIDADO

vegetales = { 
    "jitomate": {
        "nombre": "Jitomate",
        "agua_necesaria": "Moderada",
        "cantidad_de_luz": "Pleno sol",
        "temporada": "Primavera/Verano",
        "cuidado": "Moderado",
        "precio_por_kilo": 30,
        "peso_m2": 8
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
    """
    Representa un vegetal con sus características de cultivo.
    
    Atributos:
        nombre (str): Nombre del vegetal.
        cantidad_de_luz (str): Requisitos de luz solar (ej. "Pleno sol").
        agua_necesaria (str): Necesidad de agua (ej. "Moderada").
        temporada (str): Temporada de cultivo principal (ej. "Primavera/Verano").
        cuidado (str): Nivel de cuidado necesario (ej. "Moderado").
        precio_por_kilo (float): Precio en el mercado por kilogramo.
        peso_m2 (float): Producción en kilogramos por metro cuadrado.
    """
    def __init__(self, nombre, cantidad_de_luz, agua_necesaria, temporada, cuidado, precio_por_kilo, peso_m2):
    #Inicializa un objeto Vegetal con los datos proporcionados.
        self.nombre = nombre
        self.cantidad_de_luz = cantidad_de_luz
        self.agua_necesaria = agua_necesaria
        self.temporada = temporada
        self.cuidado = cuidado
        self.precio_por_kilo = precio_por_kilo
        self.peso_m2 = peso_m2

    def __eq__(self, other):
    #Comprueba si otro objeto Vegetal es igual a este, basado en el nombre.
        if isinstance(other, Vegetal):
            return self.nombre == other.nombre
        return False

    def __hash__(self):
    #Devuelve un valor hash basado en el nombre del vegetal.
        return hash(self.nombre)

    def __repr__(self):
    #Devuelve el nombre del vegetal como su representación en cadena.
        return self.nombre
    
class Genotipo:
    def __init__(self, cultivos={}):
        self.cultivos = cultivos
        self.utilidad = 0

    def __str__(self):
        # Formatea la utilidad como un número con separadores de miles y un signo de pesos.
        utilidad_formateada = '${:,.0f}'.format(self.utilidad)
        cadena = 'Utilidad: ' + utilidad_formateada + '\n'
        for cultivo in self.cultivos:
            cadena += str(cultivo) + ': ' + str(round(self.cultivos[cultivo], 3) * 100) + '%\n'
        return cadena

    def __repr__(self):
        return self.__str__()
    
#CAMBIAR ESTO A ESPAÑOL
def generate_random_numbers(n, min_gap=0.05):
    n = n + 1
    if n < 1:
        return []  # No random numbers can be generated if n is less than 1
    if n == 1:
        return [1.0]  # Only one number to generate, it has to be 1

    cuts = [0]  # Start with 0 as the first cut
    while len(cuts) < n:
        next_cut = cuts[-1] + min_gap + random.random() * (1 - cuts[-1] - (n - len(cuts)) * min_gap)
        if next_cut <= 1.0:
            cuts.append(next_cut)

    cuts[-1] = 1.0  # Ensure the last cut goes to 1.0 to sum exactly 1.0

    random_numbers = [cuts[i] - cuts[i - 1] for i in range(1, len(cuts))]

    return random_numbers

lista_cultivos = vegetales


def crear_combinacion_aleatoria(n, lista_cultivos):
    genotipo = {}
    random_numbers = generate_random_numbers(n)
    cultivos = list(lista_cultivos.copy())
    
    for i in range(n):
        #Tomar un cultivo aleatorio de la lista de cultivos y asocia un porcentaje aleatorio, 
        #retirar el cultivo de la lista y el porcentaje de la lista de porcentajes
        cultivo = random.choice(cultivos)
        cultivos.remove(cultivo)
        porcentaje = random.choice(random_numbers)
        random_numbers.remove(porcentaje)
        cultivo = lista_cultivos[cultivo]
        vegetal = Vegetal(cultivo["nombre"],cultivo["cantidad_de_luz"],cultivo["agua_necesaria"],
                          cultivo["temporada"],cultivo["cuidado"],
                          cultivo["precio_por_kilo"],cultivo["peso_m2"])
        genotipo[vegetal] = porcentaje 
    return genotipo


def inicializar_poblacion(min_cultivos,tam_poblacion, lista_cultivos):
    poblacion = []
    for _ in range(tam_poblacion):
        n = random.randint(min_cultivos, len(lista_cultivos))
        genotipo = crear_combinacion_aleatoria(n,lista_cultivos)
        genotipo = Genotipo(genotipo)
        poblacion.append(genotipo)
    return poblacion


def evaluar(genotipo:Genotipo = {}, m2 = int, sol = str, agua = str, temp = str):
  
  if genotipo.utilidad != 0: #si ya se ha evaluado, regresa el valor
      return genotipo.utilidad
  '''
  #checamos que la suma de porcentajes sea =1
  sum = 0 #definimos la suma de porcentajes
  for cultivo in genotipo.cultivos :
    sum += cultivo.porcentaje
  if sum != 1 :
    return 0  
 '''
  utilidad_total =0
  for cultivo in genotipo.cultivos:
     # calculamos el ingreso generado por el cultivo
     ingreso = cultivo.peso_m2 * m2 * genotipo.cultivos[cultivo] * cultivo.precio_por_kilo

     costo = 0
     # El precio aproximado de cuidar un m2 por mes de varios cultivos es presentado en https://www.scielo.sa.cr/pdf/ac/v44n2/0377-9424-ac-44-02-81.pdf
     #Suponemos que la mano de
     base_mano_obra = 4 # Moderado /m2
     if cultivo.cuidado == 'Bajo': #/m2 
        base_mano_obra = base_mano_obra * 0.5
     if cultivo.cuidado == 'Alto': #/m2
        base_mano_obra = base_mano_obra * 1.5

     costo_mano_obra= base_mano_obra * m2

     costo += costo_mano_obra

     probabilidad = probabilidad_crecimiento(cultivo,sol,agua,temp) #usamos una función externa
     #encontrar una forma de calcular la probabilidad de que crezca el cultivo dado el status quo plantagi

     utilidad = ingreso - costo
     utilidad_esperada = utilidad * probabilidad
     utilidad_total += utilidad_esperada

  genotipo.utilidad = utilidad_total  
  return utilidad_total

def probabilidad_crecimiento(cultivo = object, sol = str, agua = str, temp = str):
   prob=1

#como el agua afecta la probabilidad
   if (agua != cultivo.agua_necesaria):
      
      if (cultivo.agua_necesaria == 'Alta'):
         if (agua == 'Baja'):
            prob = prob * .3 #ajustar de acuerdo a observaciones
         if (agua == 'Moderada'):
            prob = prob * .7 #ajustar de acuerdo a observaciones

      if (cultivo.agua_necesaria == 'Baja'):
         if (agua == 'Alta'):
            prob = prob * .3 #ajustar de acuerdo a observaciones
         if (agua == 'Moderada'):
            prob = prob * .7 #ajustar de acuerdo a observaciones
      
      if (cultivo.agua_necesaria == 'Moderada'):
            prob = prob * .7 #ajustar de acuerdo a observaciones

#como la temporada afecta la probabilidad
   if (temp != cultivo.temporada):
       prob=prob*.6     

   return prob 


def seleccionar(poblacion,m2,sol,agua,temp,porcentaje=0.5):
    # Ordenar la población con base en la evaluación de cada individuo
    utilidades = {individuo: evaluar(individuo,m2,sol,agua,temp) for individuo in poblacion}
    poblacion_ordenada = list(utilidades.items())
    poblacion_ordenada.sort(key=lambda x: x[1], reverse=True)
    
    #Mantener la lista solo con los genotipos:
        
    #Ordenar la población de acuerdo a la utilidad:
    # Calcular el número de individuos a seleccionar
    num_seleccionados = int(len(poblacion) * porcentaje)  # Seleccionar el 50% de los mejores cultivos para ser padres.
    # Seleccionar los mejores individuos
    seleccionados = poblacion_ordenada[:num_seleccionados]
    seleccionados = [individuo[0] for individuo in seleccionados]
    
    no_seleccionados = poblacion_ordenada[num_seleccionados:]
    no_seleccionados = [individuo[0] for individuo in no_seleccionados]
    
    return seleccionados,no_seleccionados


def normalizar(genotipo):
    suma_total = sum(genotipo.cultivos.values())
    genotipo.cultivos = {cultivo: prop / suma_total for cultivo, prop in genotipo.cultivos.items()}


def cruza_genotipos(min_cult, genotipo1, genotipo2, variacion=0.12):
    # Unificar todos los cultivos en ambos genotipos
    todos_los_cultivos = set(genotipo1.cultivos.keys()).union(set(genotipo2.cultivos.keys()))
    
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
    
    return descendiente1, descendiente2


def mutar_genotipo(genotipo, var = 0.15):
    genotipo.utilidad= 0
    for cultivo in genotipo.cultivos:
            genotipo.cultivos[cultivo] += random.uniform(-var, var)
            if genotipo.cultivos[cultivo] < 0.05:
                genotipo.cultivos[cultivo] = 0.05 + random.uniform(0, 0.1)
    normalizar(genotipo)


def algoritmo_evolutivo(min_cult, pob_inicial, num_generaciones, umbral1, 
                        m2, sol, agua, temp):
    poblacion = inicializar_poblacion(min_cult, pob_inicial, lista_cultivos)
    
    for _ in range(num_generaciones):
        seleccionados, no_seleccionados = seleccionar(poblacion, m2, sol, agua, temp, umbral1)
        
        no_seleccionados = inicializar_poblacion(min_cult, int(pob_inicial*.5), lista_cultivos)
        nueva_generacion = seleccionados + no_seleccionados
        while len(nueva_generacion) < pob_inicial:
            genotipo1 = random.choice(seleccionados)
            genotipo2 = random.choice(seleccionados)
            descendiente1, descendiente2 = cruza_genotipos(min_cult,genotipo1, genotipo2)
            nueva_generacion.append(descendiente1)
            nueva_generacion.append(descendiente2)
        poblacion = nueva_generacion
            
    return seleccionados[0]

#for i in range(10):
#   top = algoritmo_evolutivo(3,100,10000,0.20,0.05, m2 = 1000, sol = 'Pleno sol', agua = 'Moderada', temp = 'Primavera/Verano')
#   print(top,sum(top.cultivos.values()))

class ParametrosAlgoritmo:
    def __init__(self, pob_inicial, num_generaciones, umbral1):
        self.pob_inicial = pob_inicial
        self.num_generaciones = num_generaciones
        self.umbral1 = umbral1

    def __str__(self):
        return f"pob_inicial: {self.pob_inicial}, num_generaciones: {self.num_generaciones}, umbral1: {self.umbral1}"

def evaluar_parametros(parametros, min_cult, m2, sol, agua, temp):
    resultado = algoritmo_evolutivo(min_cult,
                                    parametros.pob_inicial,
                                    parametros.num_generaciones,
                                    parametros.umbral1,
                                    m2, sol, agua, temp)
    return resultado.utilidad

def cruzar_parametros(padre1, padre2):
    nuevo_pob_inicial = (padre1.pob_inicial + padre2.pob_inicial) // 2
    nuevo_num_generaciones = (padre1.num_generaciones + padre2.num_generaciones) // 2
    nuevo_umbral1 = (padre1.umbral1 + padre2.umbral1) / 2
    return ParametrosAlgoritmo(nuevo_pob_inicial, nuevo_num_generaciones, nuevo_umbral1)

def mutar_parametros(parametros):
    parametros.pob_inicial = max(10, int(parametros.pob_inicial * random.uniform(0.8, 1.2)))
    parametros.num_generaciones = max(1, int(parametros.num_generaciones * random.uniform(0.8, 1.2)))
    parametros.umbral1 = max(0.1, min(parametros.umbral1 + random.uniform(-0.1, 0.1), 0.9))

def meta_algoritmo_evolutivo(min_cult, num_generaciones, m2, sol, agua, temp):
    poblacion = [ParametrosAlgoritmo(random.randint(10, 50), random.randint(1, 10), random.uniform(0.1, 0.9))
                 for _ in range(10)]

    for _ in range(num_generaciones):
        evaluaciones = [(individuo, evaluar_parametros(individuo, min_cult, m2, sol, agua, temp))
                        for individuo in poblacion]
        poblacion = [x[0] for x in sorted(evaluaciones, key=lambda x: x[1], reverse=True)[:5]]

        nueva_poblacion = []
        while len(nueva_poblacion) < 10:
            padre1, padre2 = random.sample(poblacion, 2)
            hijo = cruzar_parametros(padre1, padre2)
            mutar_parametros(hijo)
            nueva_poblacion.append(hijo)
        poblacion = nueva_poblacion

    mejor_individuo = max(poblacion, key=lambda ind: evaluar_parametros(ind, min_cult, m2, sol, agua, temp))
    return mejor_individuo



##############################################################################################################################
'''PRUEBAS

    parametros = meta_algoritmo_evolutivo(10, 1000, 'Pleno sol', 'Moderada', 'Primavera/Verano')
print (parametros)
pob_inicial = parametros.pob_inicial
num_generaciones = parametros.num_generaciones
umbral1 = parametros.umbral1



#print(meta_algoritmo_evolutivo(10, 1000, 'Pleno sol', 'Moderada', 'Primavera/Verano'))

#for i in range(10):
    #print(algoritmo_evolutivo(3,pob_inicial,num_generaciones,umbral1, m2 = 1000, sol = 'Pleno sol', agua = 'Moderada', temp = 'Primavera/Verano'))
  '''
##############################################################################################################################

def ejecutar_meta_algoritmo_interactivo():
    print("\nBienvenido al sistema de optimización de algoritmo evolutivo para cultivos.")
    print("Por favor, introduce los siguientes parámetros ambientales para comenzar la optimización:")

    # Solicitar parámetros al usuario
    m2 = float(input("\nIntroduce el área en metros cuadrados (m2) disponible para los cultivos: "))
    sol = input("Introduce la cantidad de luz solar que recibe el campo (Pleno sol o Media): ")
    agua = input("Introduce la cantidad de agua que recibe el campo (Baja o Moderada o Alta): ")
    temp = input("Introduce la temporada en la que te gustaría plantar los vegetales (Primavera/Verano u Otoño/Invierno): ")

    # Validar los valores de entrada (esto es opcional y puede ser más sofisticado según los requisitos)
    if sol not in ['Pleno sol','Media'] or agua not in ['Baja', 'Moderada', 'Alta'] or temp not in ['Primavera/Verano', 'Otoño/Invierno']:
        print("Algunos de los valores introducidos son inválidos. Asegúrate de que la cantidad de luz solar, la disponibilidad de agua y la temporada estén correctamente especificadas.")
        return

    print ("\nCalculando la mejor distribución ")
    # Ejecutar el meta algoritmo
    mejores_parametros = meta_algoritmo_evolutivo(3,10, m2=m2, sol=sol, agua=agua, temp=temp)
    
    #Mejores parámetros
    pob_inicial = mejores_parametros.pob_inicial
    num_generaciones = mejores_parametros.num_generaciones
    umbral1 = mejores_parametros.umbral1
    


    #Ejecutar el algoritmo evolutivo con los mejores parámetros encontrados

    resultado = algoritmo_evolutivo(3,pob_inicial=pob_inicial,num_generaciones=num_generaciones,umbral1=umbral1, m2 = m2, sol = sol, agua = agua, temp = temp)

    # Mostrar los resultados
    print("\nLa mejor distribución de vegetales para el campo encontrada es:")
    print(resultado)
    print (mejores_parametros) #DESPUES BORRAR ESTO
# Ejecutar la función para iniciar la interacción
ejecutar_meta_algoritmo_interactivo()
