import matplotlib.pyplot as plt
from src import config

def build_top10_plot(df):
    """
    Построение графика топ-10 товаров
    
    """
    revenue = df['quantity'] * df['price_per_unit']
    top10 = revenue.groupby(df['item_name']).sum().nlargest(10).sort_values()
    
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.barh(top10.index, top10.values, color="steelblue")
    ax.bar_label(bars, fmt="%.0f", padding=3)
    ax.margins(x=0.15)
    ax.set_xlabel("Выручка")
    ax.set_title("Топ-10 товаров по выручке")
    fig.tight_layout()
    
    return fig

def build_category_bar(df, selected=None):
    """
    Построение графика выручки по категориям

    """
    revenue = df["quantity"] * df["price_per_unit"]
    by_cat = revenue.groupby(df["category"]).sum().sort_values()
    share = by_cat / by_cat.sum() * 100

    colors = ["#E4572E" if cat == selected else "steelblue" for cat in by_cat.index]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(by_cat.index, share.values, color=colors)
    ax.bar_label(bars, labels=[f"{v:.1f}%" for v in share.values], padding=3)
    ax.set_ylabel("Доля в общей выручке, %")
    ax.set_title("Выручка по категориям")
    ax.margins(y=0.15)
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()

    return fig

def build_weekday_plot(df):
    """
    Построение графика заказов по дням недели
    
    """
    dates = df["order_date"]

    # одна строка на заказ, чтобы не считать позиции внутри заказа несколько раз
    orders = df.assign(weekday=dates.dt.dayofweek).drop_duplicates("order_id")

    counts = (
        orders.groupby("weekday")["order_id"]
        .count()
        .reindex(range(7), fill_value=0)   # все 7 дней, даже если заказов не было
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(config.DAYS, counts.values, color="steelblue")
    ax.bar_label(bars, padding=3)
    ax.set_ylabel("Количество заказов")
    ax.set_title("Заказы по дням недели")
    ax.margins(y=0.15)
    fig.tight_layout()

    return fig