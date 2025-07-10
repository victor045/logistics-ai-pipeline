
def calculate_kpis():
    import os
    import json

    route_file = os.path.join('data', 'optimized_route.txt')
    distance_file = os.path.join('data', 'route_distance.txt')
    kpis_file = os.path.join('data', 'kpis.json')

    if os.path.exists(route_file) and os.path.exists(distance_file):
        with open(route_file, 'r') as f:
            route = f.read()
        with open(distance_file, 'r') as f:
            distance = int(f.read())

        num_stops = route.count('->') + 1
        avg_distance_per_stop = distance / num_stops if num_stops else 0

        kpis = {
            "total_stops": num_stops,
            "total_distance_m": distance,
            "avg_distance_per_stop_m": round(avg_distance_per_stop, 2)
        }
        with open(kpis_file, 'w') as f:
            json.dump(kpis, f)
        print("KPIs guardados en kpis.json")
    else:
        print("No se encontraron datos de ruta para calcular KPIs")

