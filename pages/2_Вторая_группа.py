import streamlit as st
import pandas as pd
from datetime import date
import plotly.graph_objects as go

from io import StringIO  # got moved around in python3 if you're using that.

st.set_page_config(
    page_title="Вторая группа",
    page_icon="🏤",
    layout="wide",
    initial_sidebar_state="expanded",

)

if 'sign in' not in st.session_state:
    st.session_state['sign in'] = False

text_input_container_4 = st.sidebar.empty()
button_logout = None

if st.session_state["sign in"] == False:
    st.sidebar.error("Для работы этой вкладки выполните вход в систему на вкладке 'Июнь'")
else:
    button_logout = text_input_container_4.button("Выйти")
    if button_logout:
        st.session_state["sign in"] = False
    st.sidebar.info(f'Вход выполнен пользователем - {st.session_state["user"]}')

    df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRS6za6KxttllG9KP4BCjmD8dMYpltD2v3K5h2pisvD6nBAwf60PdADHwG8BAMIxg/pub?output=csv')
    df = df.set_index('ФИО МКМ')
    #print(date.today().strftime('%d.%m.%Y'))
    data_today = str(date.today().strftime('%d.%m.%Y'))
    st.title(f"Данные 2 группы на {data_today}")
    #st.dataframe(df)

    df_0 = df.copy()
    df_0 = df_0.drop("ИТОГ", axis='index')
    st.dataframe(df_0)

    st.subheader('Балльный СМОТ')
    #Data Set
    labels=df_0.index
    
    values = df_0['СМОТ']

    #The plot
    fig = go.Figure(
        go.Pie(
        labels = labels,
        values = values,
        hoverinfo = "label+percent",
        textinfo = "value"
    ))

    #st.header("Pie chart")
    st.plotly_chart(fig)

    st.subheader('Кросс КН')
    st.bar_chart(df_0['Кросс КН'])
    st.subheader('КН')
    st.bar_chart(df_0['КН'])
    st.subheader('Кросс КК')
    st.bar_chart(df_0['Кросс КК'])
    st.subheader('КК/стикер (POS)')
    st.bar_chart(df_0['КК/стикер'])
    st.subheader('ДК/стикер (POS)')
    st.bar_chart(df_0['ДК/стикер'])
    st.subheader('КСП')
    st.bar_chart(df_0['КСП'])
    st.subheader('Вклад')
    st.bar_chart(df_0['Вклад'])
    st.subheader('Самозанятость')
    st.bar_chart(df_0['Самозанятость'])
    st.subheader('Страх ДК')
    st.bar_chart(df_0['Страх ДК'])
    st.subheader('НС 1к+')
    st.bar_chart(df_0['НС 1к+'])
    st.session_state["sign in"] = False
