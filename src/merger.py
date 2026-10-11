import pandas as pd

def merge_data(df_items, df_orders, df_users):
    """
    Объединение данных

    """
    #Объединяем в один DataFrame
    merged_df = pd.merge(df_orders, df_users, on="user_id", how="left").merge(df_items, on="item_id", how="left")
    return merged_df