def calcular_puntaje_por_ronda(scores):
    totales = {}
    
    for cocinero, judges in scores.items():
        totales[cocinero] = sum(judges.values())
        
    return totales

def buscar_ganador(totales_ronda):
    return max(totales_ronda, key = totales_ronda.get)

def actualizar_tabla(tabla, totales_ronda, ganador):
    for cocinero, puntos in totales_ronda.items():
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
        
        if cocinero == ganador:
            tabla[cocinero]['Ganadas'] += 1
        
def imprimir_tabla(tabla):
    
    ranking = sorted(tabla.items(), key = lambda x: x[1]['Total'],reverse=True)
    
    print("Tabla de posiciones:")
    print(f"{'Cocinero':<12} {'Total':>6} {'Ganadas':>8} {'Mejor':>8} {'Promedio':>10}")
    print("-"*60)
    
    for cocinero, datos in ranking:
        promedio = round(datos['Total'] / len(datos['Rondas']),1)
        print(f"{cocinero:12} {datos['Total']:6} {datos['Ganadas']:8} {datos['Mejor']:10} {promedio:8}")
    
    print("-"*60)