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

def inicializar_poblacion(tam_poblacion, lista_cultivos):
    poblacion = []
    for _ in range(tam_poblacion):
        genotipo = crear_combinacion_aleatoria(lista_cultivos)
        genotipo = Genotipo(genotipo)
        poblacion.append(genotipo)
    return poblacion

def crear_combinacion_aleatoria(lista_cultivos):
    genotipo = []
    random_numbers = generate_random_numbers(len(lista_cultivos))
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

def seleccionar(poblacion,m2,sol,agua,temp):
    # Ordenar la población con base en la evaluación de cada individuo
    utilidades = {individuo: evaluar(individuo,m2,sol,agua,temp) for individuo in poblacion}
    
    #Ordenar la población de acuerdo a la utilidad:
    poblacion_ordenada = [k for k, v in sorted(utilidades.items(), key=lambda item: item[1], reverse=True)]
    # Calcular el número de individuos a seleccionar
    num_seleccionados = int(len(poblacion) * 0.3)  # Seleccionar el 30% de los mejores cultivos para ser padres.
    # Seleccionar los mejores individuos
    seleccionados = poblacion_ordenada[:num_seleccionados]
    no_seleccionados = poblacion_ordenada[num_seleccionados:]
    
    return seleccionados,no_seleccionados
    
    
def ajustar_porcentajes(originales, umbral):
    perturbados = [(p[0],max(random.uniform(0, umbral), p[1] + random.uniform(-umbral, umbral))) for p in originales]
    suma_perturbados = sum(p[1] for p in perturbados)
    normalizados = [(p[0],p[1] / suma_perturbados) for p in perturbados]
    return normalizados


def cruzar(num_hijos, padre1, padre2, umbral):
    hijos = []
    punto_corte = len(padre1.cultivos) // 2

    hijo1 = Genotipo(padre1.cultivos[:punto_corte] + padre2.cultivos[punto_corte:])
    hijo2 = Genotipo(padre2.cultivos[:punto_corte] + padre1.cultivos[punto_corte:])

    # Generar hijos con nuevos porcentajes basados en los originales con cierto umbral de variación
    for _ in range(num_hijos):
        hijo = random.choice([hijo1, hijo2])
        nuevos_porcentajes = ajustar_porcentajes([(c.nombre,c.porcentaje) for c in hijo.cultivos], umbral) 
        #Ajustar los porcentajes de los hijos
        for cultivo in hijo.cultivos:
            cultivo.porcentaje = [p[1] for p in nuevos_porcentajes if p[0] == cultivo.nombre][0]
        hijos.append(hijo)
    return hijos
    
def mutar(no_seleccionados, umbral):
    for individuo in no_seleccionados:
        nuevos_porcentajes = ajustar_porcentajes([(c.nombre,c.porcentaje) for c in individuo.cultivos], umbral)
        for cultivo in individuo.cultivos:
            cultivo.porcentaje = [p[1] for p in nuevos_porcentajes if p[0] == cultivo.nombre][0]
    return no_seleccionados

def algoritmo_evolutivo(pob_inicial, num_generaciones, umbral1, umbral2, m2, sol, agua, temp):
    poblacion = inicializar_poblacion(pob_inicial, lista_cultivos)
    for _ in range(num_generaciones):
        seleccionados, no_seleccionados = seleccionar(poblacion,m2,sol,agua,temp)
        nueva_generacion = seleccionados+mutar(no_seleccionados, umbral1)
        while len(nueva_generacion) < len(poblacion):
            if seleccionados:
                padre1, padre2 = random.choice(seleccionados), random.choice(seleccionados)
                n = random.randint(2, 6)
                hijos = cruzar(n, padre1, padre2, umbral2)
                nueva_generacion.extend(hijos)
        poblacion = nueva_generacion
    
    # Regresar el mejor individuo de la última generación:
    utilidades = {individuo: evaluar(individuo,m2,sol,agua,temp) for individuo in poblacion}
    mejor_individuo = max(utilidades, key=utilidades.get)
    return mejor_individuo
    
for i in range(10):
    print(algoritmo_evolutivo(300, 4000,0.1,0.05, m2 = 1000, sol = 'Pleno sol', agua = 'Moderada', temp = 'Primavera/Verano'))