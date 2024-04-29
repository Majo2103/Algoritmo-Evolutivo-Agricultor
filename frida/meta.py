from Equipo5 import  *
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
mejor_conjunto_parametros = meta_algoritmo(1000, 'Pleno sol', 'Moderada', 'Primavera/Verano')
print(mejor_conjunto_parametros)
