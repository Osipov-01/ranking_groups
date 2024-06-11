import streamlit as st
import pandas as pd
from datetime import date
from datetime import datetime
import plotly.graph_objects as go

from io import StringIO  # got moved around in python3 if you're using that.

st.set_page_config(
    page_title="Общий анализ",
    page_icon="🏤",
    layout="wide",
    initial_sidebar_state="expanded",

)

df_auth = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRk8UfW-agKMGralUkIeF4zIRUI1JP1Mx7j0ReFrO6IDfrKFL_FrlMZXYMpTFWex5RkwZl_7hSdfVwD/pub?output=csv')

text_input_container_0 = st.sidebar.empty()
text_input_container_1 = st.sidebar.empty()
text_input_container_2 = st.sidebar.empty()
text_input_container_3 = st.sidebar.empty()
text_input_container_4 = st.sidebar.empty()


# st.sidebar.success("Select a page above.")

if "login" not in st.session_state:
    st.session_state["login"] = ""

if "password" not in st.session_state:
    st.session_state["password"] = ""

if "user" not in st.session_state:
    st.session_state["user"] = ""

if "sign in" not in st.session_state:
    st.session_state["sign in"] = False

button_sign_in = None
button_logout = None


if st.session_state["sign in"] == False:
    text_input_container_0.title("Авторизация")
    login = text_input_container_1.text_input("Логин", st.session_state["login"], placeholder="login")
    st.session_state["login"] = login
    password = text_input_container_2.text_input("Пароль", st.session_state["password"], placeholder="password", type='password')
    st.session_state["password"] = password

    button_sign_in = text_input_container_3.button("Войти")
else:
    st.sidebar.info(f'Вход выполнен пользователем - {st.session_state["user"]}')
    data_today = str(date.today().strftime('%d.%m.%Y'))
    st.title(f"Рейтинг групп на {data_today}")
    #st.write(f'{datetime.now}')
    #st.dataframe(df_auth)

    button_logout = text_input_container_4.button("Выйти")
    if button_logout:
        st.session_state["sign in"] = False

    names_groops = ['/','Группа 1', 'Группа 2', 'Группа 3']

    #группа 1

    df1 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQTreMVxXtZ16D5JRzh5_WP6TLA32jP0hXfg6F1eQaDKM66BBzmAo8diaVct0KIHg/pub?output=csv')
    df1 = df1.set_index('ФИО МКМ')
    df_1 = df1.copy()
    # Удалить все строки, кроме строки с индексом 1
    df_1 = df_1.query('index == "ИТОГ"') 

    # Переименуйте индекс
    new_index = pd.Index([names_groops[1]])  # Новый индекс
    df_1 = df_1.set_axis(new_index, axis='index')
    #st.dataframe(df_1)

    #группа 2
    df2 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRS6za6KxttllG9KP4BCjmD8dMYpltD2v3K5h2pisvD6nBAwf60PdADHwG8BAMIxg/pub?output=csv')
    df2 = df2.set_index('ФИО МКМ')
    df_2 = df2.copy()
    # Удалить все строки, кроме строки с индексом 1
    df_2 = df_2.query('index == "ИТОГ"') 
    # Переименуйте индекс
    new_index = pd.Index([names_groops[2]])  # Новый индекс
    df_2 = df_2.set_axis(new_index, axis='index')

    #st.dataframe(df_2)

    #группа 3
    df3 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTLw8fmxo0WAZU2HMKNpYWObok6TO9gqlLmGDUYb1Bp2Hc_MFPAwJT_IiO4VAJunQ/pub?output=csv')
    df3 = df3.set_index('ФИО МКМ')
    df_3 = df3.copy()
    # Удалить все строки, кроме строки с индексом 1
    df_3 = df_3.query('index == "ИТОГ"') 

    # Переименуйте индекс
    new_index = pd.Index([names_groops[3]])  # Новый индекс
    df_3 = df_3.set_axis(new_index, axis='index')

    #st.dataframe(df_3)

    df_0 = pd.concat([df_1, df_2, df_3])

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


if button_sign_in:
    true_pass = 0
    for ind in df_auth.index:
        log = df_auth['login'][ind]
        pas = df_auth['password'][ind]        
        if (login == log) & (password == pas):
            text_input_container_0.empty()            
            text_input_container_1.empty()
            text_input_container_2.empty()
            text_input_container_3.empty()
            user = df_auth['Фамилия_Имя'][ind]
            st.session_state["user"] = user
            st.sidebar.info(f'Вход выполнен пользователем - {user}')
            st.session_state["sign in"] = True
            break;
    if st.session_state["sign in"] == False:
        if (login == None) | (password == None):
            st.sidebar.warning('Введите все поля для входа')
        else: 
            st.sidebar.error('Неверный логин/пароль')
        text_input_container_4.empty()
    else:       
        data_today = str(date.today().strftime('%d.%m.%Y'))
        st.title(f"Рейтинг групп на {data_today}")
        #st.write(f'{datetime.now}')
        #st.dataframe(df_auth)

        button_logout = text_input_container_4.button("Выйти")
        if button_logout:
            st.session_state["sign in"] = False

        names_groops = ['/','Группа 1', 'Группа 2', 'Группа 3']

        #группа 1

        df1 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQTreMVxXtZ16D5JRzh5_WP6TLA32jP0hXfg6F1eQaDKM66BBzmAo8diaVct0KIHg/pub?output=csv')
        df1 = df1.set_index('ФИО МКМ')
        df_1 = df1.copy()
        # Удалить все строки, кроме строки с индексом 1
        df_1 = df_1.query('index == "ИТОГ"') 

        # Переименуйте индекс
        new_index = pd.Index([names_groops[1]])  # Новый индекс
        df_1 = df_1.set_axis(new_index, axis='index')
        #st.dataframe(df_1)

        #группа 2
        df2 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRS6za6KxttllG9KP4BCjmD8dMYpltD2v3K5h2pisvD6nBAwf60PdADHwG8BAMIxg/pub?output=csv')
        df2 = df2.set_index('ФИО МКМ')
        df_2 = df2.copy()
        # Удалить все строки, кроме строки с индексом 1
        df_2 = df_2.query('index == "ИТОГ"') 
        # Переименуйте индекс
        new_index = pd.Index([names_groops[2]])  # Новый индекс
        df_2 = df_2.set_axis(new_index, axis='index')

        #st.dataframe(df_2)

        #группа 3
        df3 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTLw8fmxo0WAZU2HMKNpYWObok6TO9gqlLmGDUYb1Bp2Hc_MFPAwJT_IiO4VAJunQ/pub?output=csv')
        df3 = df3.set_index('ФИО МКМ')
        df_3 = df3.copy()
        # Удалить все строки, кроме строки с индексом 1
        df_3 = df_3.query('index == "ИТОГ"') 

        # Переименуйте индекс
        new_index = pd.Index([names_groops[3]])  # Новый индекс
        df_3 = df_3.set_axis(new_index, axis='index')

        #st.dataframe(df_3)

        df_0 = pd.concat([df_1, df_2, df_3])

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








