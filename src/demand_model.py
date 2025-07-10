
def predict_demand():
    import pandas as pd
    from prophet import Prophet
    import os

    input_path = os.path.join('data', 'deliveries.csv')
    df = pd.read_csv(input_path)
    df['date'] = pd.to_datetime(df['date'])

    predictions = []
    for zone in df['postal_code'].unique():
        zone_df = df[df['postal_code'] == zone][['date', 'deliveries']].rename(columns={'date': 'ds', 'deliveries': 'y'})
        if len(zone_df) < 3:
            print(f"⚠️ No hay suficientes datos para {zone}, se necesitan al menos 3.")
            continue
        try:
            model = Prophet(daily_seasonality=True)
            model.fit(zone_df)
            future = model.make_future_dataframe(periods=7)
            forecast = model.predict(future)
            forecast['postal_code'] = zone
            predictions.append(forecast[['ds', 'yhat', 'postal_code']])
        except Exception as e:
            print(f"❌ Falló la predicción para {zone}: {e}")


    all_predictions = pd.concat(predictions)
    output_path = os.path.join('data', 'predicted_demand.csv')
    all_predictions.to_csv(output_path, index=False)
    print(f"Predicción guardada en {output_path}")

