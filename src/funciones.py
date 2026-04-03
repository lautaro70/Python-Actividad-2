def calcular_puntaje_por_ronda(scores):
    totales = {}
    
    for cocinero, judges in scores.items():
        totales[cocinero] = sum(judges.values())
        
    return totales

def buscar_ganador(totales_ronda):
    return max(totales_ronda, key = totales_ronda.get)

def actualizar_tabla(tabla, totales_ronda, ganador):
    for cocinero, puntos in totales_ronda.items:
        if cocinero not in tabla:
            tabla[cocinero] = {
                'Total': 0,
                'Ganadas': 0,
                'Mejor': 0,
                'Rondas': []
            }
        
        tabla[cocinero]['Total'] += puntos
        tabla[cocinero]['Rondas'].append(puntos)
        
        if puntos > tabla[cocinero]['Mejor']:
            tabla[cocinero]['Mejor'] = puntos
        
        tabla[ganador]['Ganadas'] +1
        
def imprimir_tabla(tabla):
    
    ranking = sorted(tabla.items(), key = lambda x: x[1]['Total'],reverse=True)
    
    print("Tabla de posiciones final:")
    print("Cocinero     Puntaje total       Rondas ganadas      Mejor ronda     Promedio")
    print("-"*40)
    
    for cocinero, datos in ranking:
        promedio = round(datos['Total'] / len(datos['Rondas']),1)
        print(f"{cocinero:10}{datos['Total']:5}{datos['Ganadas']:5}{datos['Mejor']:6}{promedio}")