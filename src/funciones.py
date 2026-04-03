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
        
def ordenar_tabla(tabla):
    return sorted(tabla.items(), key = lambda x: x[1]['Total'], reverse = True)

def calcular_promedio(datos):
    return round(datos['Total'] / len(datos['Rondas']),1)
