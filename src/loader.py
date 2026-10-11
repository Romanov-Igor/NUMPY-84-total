from src import config
import pandas as pd

def load_data():
    #Загружаем данные из CSV файлов в DataFrame
    df_items = pd.read_csv(config.DATA_DIR / "items.csv")
    df_orders = pd.read_csv(config.DATA_DIR / "orders.csv")
    df_users = pd.read_csv(config.DATA_DIR / "users.csv")

    return df_items, df_orders, df_users