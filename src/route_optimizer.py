
def optimize_routes():
    import pandas as pd
    import os
    from ortools.constraint_solver import routing_enums_pb2
    from ortools.constraint_solver import pywrapcp

    file_path = os.path.join('data', 'predicted_demand.csv')
    df = pd.read_csv(file_path)
    df['postal_code'] = df['postal_code'].astype(str).str.zfill(5)
    print("Códigos postales únicos:", df['postal_code'].unique())

    # Simular coordenadas (en una versión real, se geolocaliza el código postal)
    postal_coords = {
        '01000': (19.36, -99.18),
        '02000': (19.38, -99.20),
        '03000': (19.40, -99.22),
        '04000': (19.42, -99.24),
        '05000': (19.44, -99.26),
        '06000': (19.46, -99.28),
        '07000': (19.48, -99.30),
        '08000': (19.50, -99.32),
    }

    # Filtrar solo el día más reciente
    latest_day = df['ds'].max()
    df_today = df[df['ds'] == latest_day].copy()

    # 🔧 Asegurar que los códigos postales sean strings de 5 dígitos
    df_today['postal_code'] = df_today['postal_code'].astype(str).str.zfill(5)

    # Mapear coordenadas
    df_today['coordinates'] = df_today['postal_code'].map(postal_coords)
    df_today = df_today[df_today['coordinates'].notnull()].copy()
    if df_today.empty:
        print("⚠️ No hay coordenadas válidas para la fecha:", latest_day)
        return



    # Crear matriz de distancias euclidianas
    def euclidean_distance(a, b):
        return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5

    coords = df_today['coordinates'].tolist()
    num_locations = len(coords)

    distance_matrix = [
        [int(euclidean_distance(coords[i], coords[j]) * 1000) for j in range(num_locations)]
        for i in range(num_locations)
    ]

    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        route = []
        total_distance = 0
        index = routing.Start(0)
        while not routing.IsEnd(index):
            node = manager.IndexToNode(index)
            route.append(df_today.iloc[node]['postal_code'])
            next_index = solution.Value(routing.NextVar(index))
            total_distance += routing.GetArcCostForVehicle(index, next_index, 0)
            index = next_index
        with open('data/optimized_route.txt', 'w') as f:
            f.write("->".join(route))
        with open('data/route_distance.txt', 'w') as f:
            f.write(str(total_distance))
        print(f"Ruta óptima: {route}, Distancia total: {total_distance} m")
    else:
        print("No se encontró solución de ruteo")
