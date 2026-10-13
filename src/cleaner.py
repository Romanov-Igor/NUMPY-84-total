import numpy as np
import pandas as pd
from src import config

def clean_data(merged_df):
    """
    Очистка данных: скрытые пропуски, типы, обработка пропусков

    """
    cleaned_df = merged_df.copy()

    # 1. Скрытые пропуски -> NaN
    cleaned_df = cleaned_df.replace(config.MISSING_MARKERS, np.nan)

    # 2. Приводим типы данных
    cleaned_df['order_date'] = pd.to_datetime(cleaned_df['order_date'], errors='coerce')
    cleaned_df['registration_date'] = pd.to_datetime(cleaned_df['registration_date'], errors='coerce')

    # 3. Критичные поля: без них строка бесполезна -> удаляем
    critical_cols = [c for c in ['order_id', 'user_id', 'order_date', 'item_id'] if c in cleaned_df.columns]
    cleaned_df = cleaned_df.dropna(subset=critical_cols)

    # 4. Числовые поля -> медиана
    num_cols = cleaned_df.select_dtypes(include='number').columns
    cleaned_df[num_cols] = cleaned_df[num_cols].fillna(cleaned_df[num_cols].median())

    # 5. Текстовые/категориальные поля -> 'unknown'
    cat_cols = cleaned_df.select_dtypes(include=['str', 'object', 'category']).columns
    cleaned_df[cat_cols] = cleaned_df[cat_cols].fillna('unknown')

    return cleaned_df