import streamlit as st
import pandas as pd
from datetime import date
import plotly.graph_objects as go

from io import StringIO  # got moved around in python3 if you're using that.

data_today = str(date.today().strftime('%d.%m.%Y'))
st.title(f"Рейтинг групп на {data_today}")
st.write(f'{date.now()}')

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
df_3 = df_1.set_axis(new_index, axis='index')

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










