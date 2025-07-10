import pandas as pd

df = pd.read_csv('data/predicted_demand.csv')
latest_day = df['ds'].max()
df_today = df[df['ds'] == latest_day].copy()

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

df_today['coordinates'] = df_today['postal_code'].map(postal_coords)
print(df_today[['postal_code', 'coordinates']])

