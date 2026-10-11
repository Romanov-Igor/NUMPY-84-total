import pandas as pd

def calculate_metrics(df):
    """
    Расчет метрик

    """
    total_orders = df['order_id'].count()     # Общее количество заказов
    total_revenue = (df['price_per_unit'] * df['quantity']).sum()     # Общая выручка
    total_unique_users = df['user_id'].nunique()    # Количество уникальных пользователей
    average_bill = total_revenue / total_orders if total_orders != 0 else 0     # Средний чек

    return total_orders, total_revenue, total_unique_users, average_bill