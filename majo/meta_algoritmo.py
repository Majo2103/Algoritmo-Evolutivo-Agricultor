#determina los parametros optimos de minimo de cultivos, población inicial, numero de generaciones , umbrales de variación. 1 y 2

#imports
from mezcladora import *
from funcion_evaluadora import *
import time


#evalua que tan bueno es un algoritmo
def evaluar_algoritmo(min_cult,pob_inicial, num_generaciones, umbral1, umbral2, m2, sol, agua, temp):# el algoritmo recibe lo mismo que el algoritmo evolutivo
    tiempo_inicial = time.time()
    res = algoritmo_evolutivo(min_cult,pob_inicial, num_generaciones, umbral1, umbral2, m2, sol, agua, temp)
    tiempo_final = time.time()

    tiempo_ejecucion =tiempo_final - tiempo_inicial #mientras menor mejor

    res.utilidad()

    evaluacion = 




