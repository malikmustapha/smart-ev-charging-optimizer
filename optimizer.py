import pandas as pd
import math

def optimize_charging_schedule(df, needed_kwh, charger_rate, deadline_hour):
    """
    df: dataframe with datetime + price
    needed_kwh: total energy to charge
    charger_rate: kW
    deadline_hour: hour in day (0-23) by when charging must finish
    """
    # Number of hours needed
    hours_needed = math.ceil(needed_kwh / charger_rate)

    # Use earliest datetime in data as "now" for demo
    now = df['datetime'].min()
    
    # Deadline datetime (on same day as now)
    deadline = now.normalize() + pd.Timedelta(hours=deadline_hour)

    # Filter df between now and deadline
    mask = (df['datetime'] >= now) & (df['datetime'] < deadline)
    future_df = df.loc[mask].copy()

    # Sort by price ascending
    future_df.sort_values(by='price', inplace=True)

    # Pick cheapest hours_needed rows
    selected_hours = future_df.head(hours_needed).sort_values(by='datetime')

    # Calculate estimated cost
    avg_price = selected_hours['price'].mean() if not selected_hours.empty else 0
    total_cost = (needed_kwh) * avg_price

    return selected_hours, total_cost
