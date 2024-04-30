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
     # El precio aproximado de cuidar un m2 por mes de varios cultivos es presentado en https://www.scielo.sa.cr/pdf/ac/v44n2/0377-9424-ac-44-02-81.pdf
     #Suponemos que la mano de
     base_mano_obra = 400 # Moderado /m2
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
     utilidad_total += utilidad
  
  
  return utilidad






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
       prob = prob *.6 

   if (sol != cultivo.sol):
      prob = prob *.8

   return prob 



"""pruebas

jitomate =Vegetal('Jitomate', 'Pleno sol','Moderada','Primavera/Verano','Moderado',15,.50,8)
cebolla=Vegetal(nombre= "Cebolla",agua= "Moderada",sol="Pleno sol", temporada= "Otoño/Invierno",
        mano_obra= "Bajo",precio_kilo= 7.5,peso_m2= 4,porcentaje=.50)

cebolla2=Vegetal(nombre= "Cebolla",agua= "Moderada",sol="Pleno sol", temporada= "Otoño/Invierno",
        mano_obra= "Bajo",precio_kilo= 7.5,peso_m2= 4,porcentaje=.40)

vegetales = [jitomate, cebolla]
vegetales2 = [jitomate, cebolla2]
g = Genotipo(vegetales)
g2 = Genotipo(vegetales2)

print(evaluar(g,m2 = 1000, sol = 'Pleno sol', agua = 'Moderada', temp = 'Primavera/Verano'))

print(evaluar(g2,m2 = 1000, sol = 'Pleno sol', agua = 'Moderada', temp = 'Primavera/Verano'))
"""
