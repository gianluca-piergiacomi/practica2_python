rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9}, 
            'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7}, 
            'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8}, 
            'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6}, 
            'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
        }
    },
    {
        'theme': 'Plato principal', 
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8}, 
            'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9}, 
            'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7}, 
            'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8}, 
            'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
        }
    },
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7}, 
            'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8}, 
            'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9}, 
            'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6}, 
            'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9}, 
            'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7}, 
            'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8}, 
            'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7}, 
            'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9}, 
            'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8}, 
            'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7}, 
            'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9}, 
            'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
        },
    }
]

def procesar_competencia(rounds):
    #se arma el diccionario de estadísticas
    estadisticas = {}
    
    #inicializa el contador para cada cocinero
    for nombre in rounds[0]['scores']:
        estadisticas[nombre] = {
            'puntaje_total': 0,
            'rondas_ganadas': 0,
            'mejor_ronda': 0
        }
    
    numero_ronda = 1
    
    #recorrido de rondas
    for ronda in rounds:
        print("Ronda", numero_ronda, "-", ronda['theme'])
        
        puntaje_maximo_ronda = -1
        ganador_ronda = ""
        
        for cocinero, notas in ronda['scores'].items():
            #suma las 3 notas
            suma_notas = notas['judge_1'] + notas['judge_2'] + notas['judge_3']
            
            #acumula las notas en el puntaje total
            estadisticas[cocinero]['puntaje_total'] = estadisticas[cocinero]['puntaje_total'] + suma_notas
            
            #verifica si es la mejor ronda para el cocinero
            if suma_notas > estadisticas[cocinero]['mejor_ronda']:
                estadisticas[cocinero]['mejor_ronda'] = suma_notas
                
            #busca el máximo para actualizarlo y saber quién va ganando la ronda
            if suma_notas > puntaje_maximo_ronda:
                puntaje_maximo_ronda = suma_notas 
                ganador_ronda = cocinero          
        
        #al ganador se le suma 1 victoria al acumulador de rondas ganadas
        estadisticas[ganador_ronda]['rondas_ganadas'] = estadisticas[ganador_ronda]['rondas_ganadas'] + 1
        
        print("Ganador de la ronda:", ganador_ronda, "con", puntaje_maximo_ronda, "puntos")
        print("-" * 30)
        
        print("---Tabla parcial---")
        for cocinero, datos in estadisticas.items():
            print(cocinero, "- Puntos:", datos['puntaje_total'], "puntos.")
        print("\n")
        
        #queda pasar a la siguiente ronda
        numero_ronda = numero_ronda + 1

    
    #pasa los datos del diccionario a una lista comun para que sea más fácil ordenarlos. 
    lista_para_ordenar = []
    for cocinero, datos in estadisticas.items():
        fila = [cocinero, datos['puntaje_total'], datos['rondas_ganadas'], datos['mejor_ronda']]
        lista_para_ordenar.append(fila)
            
    #ordenamos la lista por puntaje total de forma descendente.
    lista_para_ordenar.sort(key=lambda fila: fila[1], reverse=True)

    print("Tabla de posiciones final:")
    cantidad_rondas = len(rounds)
    
    for fila in lista_para_ordenar:
        nombre = fila[0]
        total = fila[1]
        ganadas = fila[2]
        mejor = fila[3]
        promedio = total / cantidad_rondas
        
        print(nombre, "- Puntos:", total, "- Rondas Ganadas:", ganadas, "- Mejor Ronda:", mejor, "- Promedio:", promedio)

procesar_competencia(rounds)