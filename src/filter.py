import streamlit as st
import pandas as pd

def filter_data(df):
    """
    Фильтрация по дате и категории

    """
    st.sidebar.title("Фильтры")
    min_date = df['order_date'].min().date()
    max_date = df['order_date'].max().date()
    all_label = "Все"
    date_filter = st.sidebar.date_input("Выберите даты", value=(min_date, max_date), min_value=min_date, max_value=max_date)
    options = [all_label] + sorted(df['category'].unique())
    selected = st.sidebar.selectbox("Выберите категорию", options)
    if len(date_filter) == 2:
        start, end = date_filter
        mask = (df['order_date'] >= pd.Timestamp(start)) & (df['order_date'] < pd.Timestamp(end) + pd.Timedelta(days=1))
        if selected == all_label:
            filtered_df = df.loc[mask]
        else:
            filtered_df = df.loc[mask & (df["category"] == selected)]
    else:
        filtered_df = df
    return filtered_df