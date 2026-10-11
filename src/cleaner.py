import pandas as pd

def clean_data(merged_df):
    """
    Очистка данных
    
    """
    cleaned_df = merged_df.copy()

    # Приводим типы данных к нужным форматам
    cleaned_df['order_date'] = pd.to_datetime(cleaned_df['order_date'], errors='coerce')
    cleaned_df['registration_date'] = pd.to_datetime(cleaned_df['registration_date'], errors='coerce')

    return cleaned_df