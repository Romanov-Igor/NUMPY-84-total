import pandas as pd

# Винительный падеж: "приходится на ..."
WEEKDAYS = ["понедельник", "вторник", "среду", "четверг",
            "пятницу", "субботу", "воскресенье"]

# Окончания
def _plural_orders(n):
    if n % 10 == 1 and n % 100 != 11:
        return f"{n} заказ"
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return f"{n} заказа"
    return f"{n} заказов"

def _revenue(df):
    return df["quantity"] * df["price_per_unit"]


def build_insights(filtered_df, period_df):
    if filtered_df.empty or period_df.empty:
        return ["Нет данных для выводов."]

    insights = []

    # 1. Товар с наибольшей выручкой (по отфильтрованным данным)
    by_item = _revenue(filtered_df).groupby(filtered_df["item_name"]).sum()
    insights.append(
        f"Самую большую выручку принес товар: **{by_item.idxmax()}** "
        f"({by_item.max():,.0f} ₽)."
    )

    # 2. Категория с наибольшей долей (по period_df, как на графике)
    by_cat = _revenue(period_df).groupby(period_df["category"]).sum()
    share = by_cat.max() / by_cat.sum() * 100
    insights.append(
        f"Категория с наибольшей долей выручки (среди всех категорий за период): "
        f"**{by_cat.idxmax()}**, {share:.1f}%."
    )

    # 3. Пик заказов по дням недели (с учётом ничьей)
    orders = filtered_df.drop_duplicates("order_id")
    by_day = (
        orders.groupby(orders["order_date"].dt.dayofweek)["order_id"]
        .count()
        .reindex(range(7), fill_value=0)
    )
    max_count = by_day.max()
    peak_days = by_day[by_day == max_count].index.tolist()

    if len(peak_days) == 7:
        insights.append(
            f"Заказы распределены по дням недели равномерно ({_plural_orders(max_count)} в день)."
        )
    elif len(peak_days) == 1:
        insights.append(
            f"Пик заказов приходится на **{WEEKDAYS[peak_days[0]]}** "
            f"({_plural_orders(max_count)})."
        )
    else:
        names = ", ".join(WEEKDAYS[d] for d in peak_days)
        insights.append(
            f"Пик заказов приходится на **{names}**: по {_plural_orders(max_count)} в каждый из этих дней."
        )
    return insights