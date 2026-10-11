import streamlit as st
from src import loader, merger, cleaner, filter, metrics, plotter

@st.cache_data
def load_data():
    df_items, df_orders, df_users = loader.load_data()
    merged_df = merger.merge_data(df_items, df_orders, df_users)
    cleaned_df = cleaner.clean_data(merged_df)
    return cleaned_df

def main():
    cleaned_df = load_data()    # Сырой датафрейм
    filtered_df = filter.filter_data(cleaned_df)   # Отфильтрованный датафрейм
    total_orders, total_revenue, total_unique_users, average_bill = metrics.calculate_metrics(filtered_df) # Метрики
    
    # Отображаем сырые данные в Streamlit
    st.title("Сырые данные")
    with st.expander("Показать данные"):
        st.dataframe(cleaned_df)

    # Отображаем отфильтрованные данные в Streamlit
    st.title("Отфильтрованные данные")
    if filtered_df.empty:
        st.warning("Нет данных за выбранный период и категорию.")
    else:
        st.caption(f'Строк: {len(filtered_df)} из {len(cleaned_df)}')
        st.dataframe(filtered_df)

    # Отображаем метрики
    row1 = st.columns(2)
    row2 = st.columns(2)
    row1[0].metric("Общее количество заказов", value=total_orders)
    row1[1].metric("Общая выручка", value=f"{total_revenue:,.2f} ₽")
    row2[0].metric("Количесвто уникальных пользователей", value=total_unique_users)
    row2[1].metric("Средний чек", value=f"{average_bill:,.2f} ₽")

    # Отображаем графики
    tab1, tab2, tab3 = st.tabs(["Топ-10 товаров", "Выручка по категориям", "Заказы по дням недели"])
    with tab1:
        st.pyplot(plotter.build_top10_plot(cleaned_df))
    with tab2:
        st.pyplot(plotter.build_category_bar(cleaned_df))
    with tab3:
        st.pyplot(plotter.build_weekday_plot(cleaned_df))

    # Аналитические выводы
    st.markdown(
        """
        # Выводы
        1. Самую большую выручку принес товар: Ноутбук ASUS VivoBook.  
        2. Категория с наибольшей долей выручки: Электроника. 54.6%, что значительно больше других категорий.  
        3. Пик продаж приходится на пятницу. В четверг и субботу также продажи больше чем в другие дни.
        """
    )

if __name__ == "__main__":
    main()
    


