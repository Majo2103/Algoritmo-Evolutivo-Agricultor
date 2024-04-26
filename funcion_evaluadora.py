from clase_genotipo import *

def evaluar(genotipo:Genotipo = [], m2 = int, sol = str, agua = str, temp = str):
  
  #checamos que la suma de porcentajes sea =1
  sum = 0 #definimos la suma de porcentajes
  for cultivo in genotipo.cultivos :
    sum += cultivo.porcentaje
  if sum != 1 :
    return 0
  

  utilidad_total =0
  for cultivo in genotipo.cultivos:
     # calculamos el ingreso generado por el cultivo
     ingreso = cultivo.peso_m2 * m2 * cultivo.porcentaje * cultivo.precio_kilo

     # calculamos los costos
     costo = 0
     #encontrar una forma de calcular los costos de la mano de obra para cada planta

     probabilidad = 1
     #encontrar una forma de calcular la probabilidad de que crezca el cultivo dado el status quo planta


     utilidad = ingreso - costo
     utilidad_esperada = utilidad * probabilidad
     utilidad_total += utilidad
  
  

  return utilidad