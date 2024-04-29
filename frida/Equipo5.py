import random


vegetales = { #diccionario de vegetales que contine todos los posibles vegetales y su información
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
    }

    
}


class Vegetal:
    def __init__(self, nombre, sol, agua, temporada, mano_obra, precio_kilo, porcentaje,peso_m2):
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
        
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return self.nombre
    
    def __eq__(self, other):
        return self.nombre == other.nombre

class Genotipo:
    def __init__(self, cultivos = []): #recibe un arreglo de vegetales
        self.cultivos = cultivos
        self.utilidad = 0
        
    def __str__(self):
        #Utilidad y, cultivos con su porcentaje:
        cadena = 'Utilidad: '+str(self.utilidad)+'\n'
        for cultivo in self.cultivos:
            cadena += cultivo.nombre+' '+str(cultivo.porcentaje)+'\n'
            
        return cadena

def evaluar(genotipo:Genotipo = [], m2 = int, sol = str, agua = str, temp = str):
  
  if genotipo.utilidad != 0:
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
     ingreso = cultivo.peso_m2 * m2 * cultivo.porcentaje * cultivo.precio_kilo

     # calculamos los costos
     costo = 0
     # El precio aproximado de cuidar un m2 por mes de varios cultivos es presentado en https://www.scielo.sa.cr/pdf/ac/v44n2/0377-9424-ac-44-02-81.pdf
     #Suponemos que la mano de
     base_mano_obra = 4 # Moderado /m2
     if cultivo.mano_obra == 'Bajo': #/m2 
        base_mano_obra = base_mano_obra * 0.5
     if cultivo.mano_obra == 'Alto': #/m2
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
   if (agua != cultivo.agua):
      
      if (cultivo.agua == 'Alta'):
         if (agua == 'Baja'):
            prob = prob * .3 #ajustar de acuerdo a observaciones
         if (agua == 'Moderada'):
            prob = prob * .7 #ajustar de acuerdo a observaciones

      if (cultivo.agua == 'Baja'):
         if (agua == 'Alta'):
            prob = prob * .3 #ajustar de acuerdo a observaciones
         if (agua == 'Moderada'):
            prob = prob * .7 #ajustar de acuerdo a observaciones
      
      if (cultivo.agua == 'Moderada'):
            prob = prob * .7 #ajustar de acuerdo a observaciones

#como la temporada afecta la probabilidad
   if (temp != cultivo.temporada):
       prob=prob*.6     

   return prob 


lista_cultivos = vegetales

#Esta función permite generar números aleatorios que sumen 1
def generate_random_numbers(n):
    cuts = sorted(random.random() for _ in range(n - 1))
    random_numbers = []
    if cuts:
        random_numbers.append(cuts[0])
    else:
        return [1.0]
    for i in range(1, len(cuts)):
        random_numbers.append(cuts[i] - cuts[i - 1])
    random_numbers.append(1 - cuts[-1])
    return random_numbers

def inicializar_poblacion(min_cult,tam_poblacion, lista_cultivos):
    poblacion = []
    for _ in range(tam_poblacion):
        n = random.randint(min_cult, len(lista_cultivos))
        genotipo = crear_combinacion_aleatoria(n,lista_cultivos)
        genotipo = Genotipo(genotipo)
        poblacion.append(genotipo)
    return poblacion

def crear_combinacion_aleatoriaGERRY(n, lista_cultivos):
    genotipo = []
    random_numbers = generate_random_numbers(n)
    cultivos = list(lista_cultivos.copy())
    
    for i in range(len(random_numbers)):
        #Tomar un cultivo aleatorio de la lista de cultivos y asocia un porcentaje aleatorio, 
        #retirar el cultivo de la lista y el porcentaje de la lista de porcentajes
        cultivo = random.choice(cultivos)
        cultivos.remove(cultivo)
        porcentaje = random.choice(random_numbers)
        random_numbers.remove(porcentaje)
        cultivo = lista_cultivos[cultivo]
        vegetal = Vegetal(cultivo["nombre"],cultivo["cantidad_de_luz"],cultivo["agua_necesaria"],
                          cultivo["temporada"],cultivo["cuidado"],
                          cultivo["precio_por_kilo"],porcentaje,cultivo["peso_m2"])
        genotipo.append(vegetal)   
    return genotipo
def crear_combinacion_aleatoria(n, lista_cultivos):
    genotipo = []
    random_numbers = generate_random_numbers(n)
    cultivos = list(lista_cultivos.keys())
    
    for i in range(n):
        cultivo = random.choice(cultivos)
        cultivos.remove(cultivo)
        porcentaje = random_numbers[i]
        info_cultivo = lista_cultivos[cultivo]
        vegetal = Vegetal(info_cultivo["nombre"], info_cultivo["cantidad_de_luz"], info_cultivo["agua_necesaria"],
                          info_cultivo["temporada"], info_cultivo["cuidado"], info_cultivo["precio_por_kilo"],
                          porcentaje, info_cultivo["peso_m2"])
        genotipo.append(vegetal)
    return genotipo

def seleccionar(poblacion,m2,sol,agua,temp):
    # Ordenar la población con base en la evaluación de cada individuo
    utilidades = {individuo: evaluar(individuo,m2,sol,agua,temp) for individuo in poblacion}
    
    ##TO DO: Ordenar bien los individuos segun su utilidad:
    poblacion_ordenada = list(utilidades.items())
    poblacion_ordenada.sort(key=lambda x: x[1], reverse=True)
        
    #Ordenar la población de acuerdo a la utilidad:
    # Calcular el número de individuos a seleccionar
    num_seleccionados = int(len(poblacion) * 0.4)  # Seleccionar el 40% de los mejores cultivos para ser padres.
    # Seleccionar los mejores individuos
    seleccionados = poblacion_ordenada[:num_seleccionados]
    no_seleccionados = poblacion_ordenada[num_seleccionados:]
    
    return seleccionados,no_seleccionados
    
    
def ajustar_porcentajes(originales, umbral):
    perturbados = []
    
    for p in originales:
        perturbados.append((p[0],max(random.uniform(0, umbral), p[1] + random.uniform(-umbral, umbral))))
    suma_perturbados = sum(p[1] for p in perturbados)
    normalizados = [(p[0],p[1] / suma_perturbados) for p in perturbados]
    return normalizados


def cruzarGERRY(num_hijos, padre1, padre2, umbral):
    hijos = []
    punto_corte = min(len(padre1.cultivos),len(padre2.cultivos)) // 2

    pre1 = padre1.cultivos[:punto_corte] + padre2.cultivos[punto_corte:]
    pre2 = padre2.cultivos[:punto_corte] + padre1.cultivos[punto_corte:]

    cult1 = []
    cult2 = []
#De cada uno de los nuevos genotipos, si en la lista hay nombres de cultivos repetidos, se suman los porcentajes de dichos cultivos:
  
    for i in range(len(pre1)):
        for j in range(i+1,len(pre1)):
            if pre1[i].nombre == pre1[j].nombre:
                pre1[i].porcentaje += pre1[j].porcentaje
                break
        if pre1[i] not in cult1:
            cult1.append(pre1[i])
    hijo1 = Genotipo(cult1)
    
    for i in range(len(pre2)):
        for j in range(i+1,len(pre2)):
            if pre2[i].nombre == pre2[j].nombre:
                pre2[i].porcentaje += pre2[j].porcentaje
        if pre2[i] not in cult2:
            cult2.append(pre2[i])
    hijo2 = Genotipo(cult2)

    # Generar hijos con nuevos porcentajes basados en los originales con cierto umbral de variación
    for _ in range(num_hijos):
        hijo = random.choice([hijo1, hijo2])
        nuevos_porcentajes = ajustar_porcentajes([(c.nombre,c.porcentaje) for c in hijo.cultivos], umbral) 
        #Ajustar los porcentajes de los hijos
        for cultivo in hijo.cultivos:
            cultivo.porcentaje = [p[1] for p in nuevos_porcentajes if p[0] == cultivo.nombre][0]
        hijos.append(hijo)
    return hijos
def cruzar(num_hijos, padre1, padre2, umbral):
    hijos = []
    punto_corte = min(len(padre1.cultivos), len(padre2.cultivos)) // 2

    for _ in range(num_hijos):
        pre1 = padre1.cultivos[:punto_corte] + padre2.cultivos[punto_corte:]
        pre2 = padre2.cultivos[:punto_corte] + padre1.cultivos[punto_corte:]
        
        # Normalizar los porcentajes
        suma_pre1 = sum(c.porcentaje for c in pre1)
        suma_pre2 = sum(c.porcentaje for c in pre2)
        
        for c in pre1:
            c.porcentaje /= suma_pre1
        for c in pre2:
            c.porcentaje /= suma_pre2
        
        hijo1 = Genotipo(pre1)
        hijo2 = Genotipo(pre2)
        hijos.extend([hijo1, hijo2])
        
    return hijos
  
def mutar(no_seleccionados, umbral):
    for individuo in no_seleccionados:
        nuevos_porcentajes = ajustar_porcentajes([(c.nombre,c.porcentaje) for c in individuo.cultivos], umbral)
        for cultivo in individuo.cultivos:
            cultivo.porcentaje = [p[1] for p in nuevos_porcentajes if p[0] == cultivo.nombre][0]
    return no_seleccionados


def algoritmo_evolutivo(min_cult,pob_inicial, num_generaciones, umbral1, umbral2, m2, sol, agua, temp):
    poblacion = inicializar_poblacion(min_cult,pob_inicial, lista_cultivos)
    for _ in range(num_generaciones):
        seleccionados, no_seleccionados = seleccionar(poblacion,m2,sol,agua,temp)
        
        seleccionados = [individuo[0] for individuo in seleccionados]
        no_seleccionados = [individuo[0] for individuo in no_seleccionados]
        
        num_mutados = int(len(no_seleccionados) * .7)  # Seleccionar el 70% de los individuos no seleccionados para mutar
        random_no_seleccionados = random.sample(no_seleccionados, num_mutados)
        
        for no_selected in random_no_seleccionados:
            no_selected.utilidad = 0
        no_seleccionados = mutar(random_no_seleccionados, umbral1)
        nueva_generacion = seleccionados + no_seleccionados
        #El resto de la población se genera cruzando a los seleccionados
        
        #EL CRUZAMIENTO NO FUNCIONA BIEN DEL TODO
        while len(nueva_generacion) < pob_inicial:
            if seleccionados:
                padre1 = random.choice(seleccionados)
                random.shuffle(seleccionados)
                padre2 = random.choice(seleccionados)
                
                hijos = cruzar(2, padre1, padre2, umbral2)
                nueva_generacion.extend(hijos)
        poblacion = nueva_generacion
    
    utilidades={}
    for individuo in poblacion:
        utilidades[individuo] = evaluar(individuo,m2,sol,agua,temp)
    poblacion_ordenada = list(utilidades.items())
    poblacion_ordenada.sort(key=lambda x: x[1], reverse=True)

    return poblacion_ordenada[0][0]
    
#for i in range(10):
    #print(algoritmo_evolutivo(3,30000,10,0.20,0.05, m2 = 1000, sol = 'Pleno sol', agua = 'Moderada', temp = 'Primavera/Verano'))

'''def ejecutable():
    print("\nBienvenido al Algoritmo Evolutivo para la Optimización Agrícola")
    print("Por favor, introduce los parámetros necesarios para ejecutar el algoritmo.")

    # Parámetros específicos del algoritmo evolutivo 
    #ESTO NO LO VA A INGRESAR EL USUARIO, SE VA A OPTIMIZAR CON OTRO CODIGO
    min_cult = int(input("Introduce el número mínimo de cultivos diferentes en cada genotipo (ej. 3): "))
    pob_inicial = int(input("Introduce el tamaño inicial de la población (ej. 100): "))
    num_generaciones = int(input("Introduce el número de generaciones (ej. 50): "))
    umbral1 = float(input("Introduce el umbral para la mutación (ej. 0.1): "))
    umbral2 = float(input("Introduce el umbral para el cruce (ej. 0.1): "))
    
    # Parámetros de condiciones de cultivo
    m2 = int(input("Introduce el tamaño del campo en metros cuadrados (ej. 1000): "))
    sol = input("Introduce la cantidad de luz solar que recibe el campo (Pleno sol, Media sombra): ")
    agua = input("Introduce el nivel de agua que recibe el campo (Alta, Moderada, Baja): ")
    temp = input("Introduce la temporada (Primavera/Verano, Otoño/Invierno): ")
    
    # Ejecutar el algoritmo evolutivo
    resultado = algoritmo_evolutivo(min_cult, pob_inicial, num_generaciones, umbral1, umbral2, m2, sol, agua, temp)
    
    # Mostrar el resultado
    print("\n Resultado de la optimización:")
    print(resultado)

# Llamar a la función ejecutable cuando se desee iniciar el proceso
print(ejecutable())'''

class Parametros:
    def __init__(self, min_cult, pob_inicial, num_generaciones, umbral1, umbral2):
        self.min_cult = min_cult
        self.pob_inicial = pob_inicial
        self.num_generaciones = num_generaciones
        self.umbral1 = umbral1
        self.umbral2 = umbral2

def evaluar_parametros(params, m2, sol, agua, temp):
    resultado = algoritmo_evolutivo(params.min_cult, params.pob_inicial, params.num_generaciones,
                                    params.umbral1, params.umbral2, m2, sol, agua, temp)
    return resultado.utilidad  # Asumiendo que algoritmo_evolutivo devuelve algo con un atributo 'utilidad'

def meta_algoritmo(m2, sol, agua, temp):
    # Parámetros iniciales
    poblacion = [Parametros(random.randint(3, 10), random.randint(100, 300), random.randint(10, 50),
                             random.uniform(0.01, 0.2), random.uniform(0.01, 0.2)) for _ in range(10)]
    
    for generacion in range(20):  # Ejecutamos por 20 generaciones
        evaluaciones = [(p, evaluar_parametros(p, m2, sol, agua, temp)) for p in poblacion]
        evaluaciones.sort(key=lambda x: x[1], reverse=True)  # Ordenamos por utilidad, descendente
        mejores = evaluaciones[:5]  # Seleccionamos los 5 mejores

        # Reproducción y mutación para crear una nueva población
        nuevos = []
        while len(nuevos) < 10:
            padre1, padre2 = random.sample([p[0] for p in mejores], 2)
            hijo = Parametros(
                min_cult=random.choice([padre1.min_cult, padre2.min_cult]),
                pob_inicial=random.choice([padre1.pob_inicial, padre2.pob_inicial]),
                num_generaciones=random.choice([padre1.num_generaciones, padre2.num_generaciones]),
                umbral1=random.uniform(min(padre1.umbral1, padre2.umbral1), max(padre1.umbral1, padre2.umbral1)),
                umbral2=random.uniform(min(padre1.umbral2, padre2.umbral2), max(padre1.umbral2, padre2.umbral2))
            )
            nuevos.append(hijo)
        poblacion = nuevos
    
    mejor = max(poblacion, key=lambda p: evaluar_parametros(p, m2, sol, agua, temp))
    return mejor

# Uso del meta algoritmo:
#mejor_conjunto_parametros = meta_algoritmo(1000, 'Pleno sol', 'Moderada', 'Primavera/Verano')
#print(mejor_conjunto_parametros)


def ejecutable():
    print("\nBienvenido al Algoritmo Evolutivo para la Optimización Agrícola")
    print("Por favor, introduce las condiciones del cultivo necesarias para ejecutar el algoritmo.")

    # Parámetros de condiciones de cultivo ingresados por el usuario
    m2 = int(input("Introduce el tamaño del campo en metros cuadrados (ej. 1000): "))
    sol = input("Introduce la cantidad de luz solar que recibe el campo (Pleno sol, Media sombra): ")
    agua = input("Introduce el nivel de agua que recibe el campo (Alta, Moderada, Baja): ")
    temp = input("Introduce la temporada (Primavera/Verano, Otoño/Invierno): ")
    
    # Obtener los mejores parámetros del algoritmo evolutivo utilizando el meta algoritmo
    # Asumimos que la función meta_algoritmo ya está implementada y devuelve una instancia de Parametros
    parametros_optimos = meta_algoritmo(m2, sol, agua, temp)
    
    # Ejecutar el algoritmo evolutivo con los parámetros optimizados
    resultado = algoritmo_evolutivo(
        parametros_optimos.min_cult,
        parametros_optimos.pob_inicial,
        parametros_optimos.num_generaciones,
        parametros_optimos.umbral1,
        parametros_optimos.umbral2,
        m2, sol, agua, temp
    )
    
    # Mostrar el resultado
    print("\nResultado de la optimización:")
    print(resultado)

# Llamar a la función ejecutable cuando se desee iniciar el proceso
ejecutable()
