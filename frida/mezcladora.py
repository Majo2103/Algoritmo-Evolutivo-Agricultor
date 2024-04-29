from clase_genotipo import *
from funcion_evaluadora import *
import random

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
        
        num_mutados = int(len(no_seleccionados) * 1)  # Seleccionar el 70% de los individuos no seleccionados para mutar
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

def ejecutable():
    print("\nBienvenido al Algoritmo Evolutivo para la Optimización Agrícola")
    print("Por favor, introduce los parámetros necesarios para ejecutar el algoritmo.")

    # Parámetros específicos del algoritmo evolutivo
    min_cult = int(input("Introduce el número mínimo de cultivos diferentes en cada genotipo (ej. 3): "))
    pob_inicial = int(input("Introduce el tamaño inicial de la población (ej. 100): "))
    num_generaciones = int(input("Introduce el número de generaciones (ej. 50): "))
    umbral1 = float(input("Introduce el umbral para la mutación (ej. 0.1): "))
    umbral2 = float(input("Introduce el umbral para el cruce (ej. 0.1): "))
    
    # Parámetros de condiciones de cultivo
    m2 = int(input("Introduce el tamaño del campo en metros cuadrados (ej. 1000): "))
    sol = input("Introduce la cantidad de luz solar (Pleno sol, Media sombra): ")
    agua = input("Introduce el nivel de agua requerido (Alta, Moderada, Baja): ")
    temp = input("Introduce la temporada (Primavera/Verano, Otoño/Invierno): ")
    
    # Ejecutar el algoritmo evolutivo
    resultado = algoritmo_evolutivo(min_cult, pob_inicial, num_generaciones, umbral1, umbral2, m2, sol, agua, temp)
    
    # Mostrar el resultado
    print("\n Resultado de la optimización:")
    print(resultado)

# Llamar a la función ejecutable cuando se desee iniciar el proceso
print(ejecutable())


