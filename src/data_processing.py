def load_data():
    import pandas as pd
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'data', 'deliveries.csv')
    file_path = os.path.abspath(file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError("Archivo deliveries.csv no encontrado")

    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df['date'] = pd.to_datetime(df['date'])

    print("Datos cargados correctamente:")
    print(df.head())

