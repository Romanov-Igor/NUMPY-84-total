import streamlit as st
import pandas as pd


def filter_data(df):
    """
    Фильтрация по дате и категории.
    Возвращает: period_df (только период), filtered_df (период + категория),
    selected (выбранная категория или None, если выбрано "Все").
    """
    st.sidebar.title("Фильтры")
    min_date = df['order_date'].min().date()
    max_date = df['order_date'].max().date()
    all_label = "Все"

    date_filter = st.sidebar.date_input(
        "Выберите даты",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )
    options = [all_label] + sorted(df['category'].unique())
    selected = st.sidebar.selectbox("Выберите категорию", options)

    # 1. Фильтр по периоду
    if len(date_filter) == 2:
        start, end = date_filter
        mask = (df['order_date'] >= pd.Timestamp(start)) & (df['order_date'] < pd.Timestamp(end) + pd.Timedelta(days=1))
        period_df = df.loc[mask]
    else:  # пользователь выбрал только начало периода
        period_df = df

    # 2. Фильтр по категории поверх периода
    if selected == all_label:
        filtered_df = period_df
        selected = None
    else:
        filtered_df = period_df[period_df["category"] == selected]

    return period_df, filtered_df, selected