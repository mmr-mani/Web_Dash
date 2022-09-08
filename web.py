import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.offline as po
import plotly.graph_objs as pg

st.set_page_config(page_title="Gaming Job Trending Tech",
                   page_icon=":video_game:", layout="wide")

st.title(":bar_chart: Analysis Dashboard")
# st.markdown('#')

data = pd.read_csv("E:\\Final_Project\\Web_Dash\\Aswift_Jobs_data.csv")
Country_code = pd.read_csv("E:\\Final_Project\\Web_Dash\\Country_code.csv")
data = data.iloc[:, 1:]
# print(data.head())

Countries = data.Country.value_counts()
Countries = pd.DataFrame(
    {'Country': Countries.index, 'Num_jobs': Countries.values})

Country_job = pd.merge(Countries, Country_code, on='Country', how='inner')

st.sidebar.header(('Filter'))
Country = st.sidebar.multiselect(
    'Select the Country:', options=data['Country'].unique(), default=['United Kingdom'])
#Country = st.sidebar.multiselect('Select the Country:', options=data['Country'].unique(), default=data['Country'].unique())
Job_Mode = st.sidebar.multiselect(
    'Select the Job Mode:', options=data['Job_Mode'].unique(), default=data['Job_Mode'].unique())

data_selection = data.query("Country ==@Country & Job_Mode==@Job_Mode")

st.header(f'Total Jobs: {len(data_selection)}')

# World_map

Country_points = dict(
    type='choropleth', locations=Country_job['Code'], z=Country_job['Num_jobs'], text=Country_job['Country'])

# layout = dict(title='Global Jobs', geo=dict(
#     projection={'type': 'hammer'}, showlakes=True, lakecolor='rgb(0,191,255)'))

layout = dict(title='Global Jobs', geo = dict(projection = {'type':'robinson'}))

x = pg.Figure(data=[Country_points], layout=layout)
st.plotly_chart(x)


# Programming Languages
Program_language = (data_selection.iloc[:, 9:14]).sum(axis=0)
Program_language = pd.DataFrame(
    {'Programming_Language': Program_language.index, 'Values': Program_language.values})
Program_language.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending Programming Languages")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(Program_language, x="Programming_Language", y="Values",
                      text="Values", color="Programming_Language"), use_container_width=True)
    tab2.plotly_chart(px.pie(Program_language, values='Values',
                      names='Programming_Language'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(Program_language)


# Company Required position
Company_Position = (data_selection.iloc[:, 14:21]).sum(axis=0)
Company_Position = pd.DataFrame(
    {'Company_Positions': Company_Position.index, 'Values': Company_Position.values})
Company_Position.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending Job Positions")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(Company_Position, x="Company_Positions", y="Values",
                      text="Values", color="Company_Positions"), use_container_width=True)
    tab2.plotly_chart(px.pie(Company_Position, values='Values',
                      names='Company_Positions'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(Company_Position)

# Software_list
Software_list = (data_selection.iloc[:, 21:29]).sum(axis=0)
Software_list = pd.DataFrame(
    {'Software_lists': Software_list.index, 'Values': Software_list.values})
Software_list.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending Softwares")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(Software_list, x="Software_lists", y="Values",
                      text="Values", color="Software_lists"), use_container_width=True)
    tab2.plotly_chart(px.pie(Software_list, values='Values',
                      names='Software_lists'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(Software_list)

# Database_list
Database_list = (data_selection.iloc[:, 29:34]).sum(axis=0)
Database_list = pd.DataFrame(
    {'Database_lists': Database_list.index, 'Values': Database_list.values})
Database_list.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending Databases")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(Database_list, x="Database_lists", y="Values",
                      text="Values", color="Database_lists"), use_container_width=True)
    tab2.plotly_chart(px.pie(Database_list, values='Values',
                      names='Database_lists'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(Database_list)

# VFX_software
VFX_software = (data_selection.iloc[:, 34:40]).sum(axis=0)
VFX_software = pd.DataFrame(
    {'VFX_softwares': VFX_software.index, 'Values': VFX_software.values})
VFX_software.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending VFX Softwares")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(VFX_software, x="VFX_softwares", y="Values",
                      text="Values", color="VFX_softwares"), use_container_width=True)
    tab2.plotly_chart(px.pie(VFX_software, values='Values',
                      names='VFX_softwares'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(VFX_software)

# Gaming_engines
Gaming_engine = (data_selection.iloc[:, 40:44]).sum(axis=0)
Gaming_engine = pd.DataFrame(
    {'Gaming_engines': Gaming_engine.index, 'Values': Gaming_engine.values})
Gaming_engine.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending Gaming Engines")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(Gaming_engine, x="Gaming_engines", y="Values",
                      text="Values", color="Gaming_engines"), use_container_width=True)
    tab2.plotly_chart(px.pie(Gaming_engine, values='Values',
                      names='Gaming_engines'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(Gaming_engine)

# Console_list
Console_list = (data_selection.iloc[:, 44:48]).sum(axis=0)
Console_list = pd.DataFrame(
    {'Console_lists': Console_list.index, 'Values': Console_list.values})
Console_list.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending Console lists")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(Console_list, x="Console_lists", y="Values",
                      text="Values", color="Console_lists"), use_container_width=True)
    tab2.plotly_chart(px.pie(Console_list, values='Values',
                      names='Console_lists'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(Console_list)

# OS_knowledge
OS_knowledge = (data_selection.iloc[:, 48:51]).sum(axis=0)
OS_knowledge = pd.DataFrame(
    {'OS_knowledges': OS_knowledge.index, 'Values': OS_knowledge.values})
OS_knowledge.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending OS")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(OS_knowledge, x="OS_knowledges", y="Values",
                      text="Values", color="OS_knowledges"), use_container_width=True)
    tab2.plotly_chart(px.pie(OS_knowledge, values='Values',
                      names='OS_knowledges'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(OS_knowledge)

# Gaming_knowledge
Gaming_knowledge = (data_selection.iloc[:, 51:64]).sum(axis=0)
Gaming_knowledge = pd.DataFrame(
    {'Gaming_knowledges': Gaming_knowledge.index, 'Values': Gaming_knowledge.values})
Gaming_knowledge.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending Gaming knowledge")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(Gaming_knowledge, x="Gaming_knowledges", y="Values",
                      text="Values", color="Gaming_knowledges"), use_container_width=True)
    tab2.plotly_chart(px.pie(Gaming_knowledge, values='Values',
                      names='Gaming_knowledges'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(Gaming_knowledge)

# Technology_list
Technology_list = (data_selection.iloc[:, 64:71]).sum(axis=0)
Technology_list = pd.DataFrame(
    {'Technology_lists': Technology_list.index, 'Values': Technology_list.values})
Technology_list.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending Technology lists")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(Technology_list, x="Technology_lists", y="Values",
                      text="Values", color="Technology_lists"), use_container_width=True)
    tab2.plotly_chart(px.pie(Technology_list, values='Values',
                      names='Technology_lists'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(Company_Position)

# Documentation_list
Documentation_list = (data_selection.iloc[:, 71:77]).sum(axis=0)
Documentation_list = pd.DataFrame(
    {'Documentation_lists': Documentation_list.index, 'Values': Documentation_list.values})
Documentation_list.sort_values(by=['Values'], inplace=True, ascending=False)

st.subheader("Trending Documentation Softwares")

col1, col2 = st.columns(2, gap="large")
with col1:
    #st.plotly_chart(Program_language_fig1, use_container_width=True)
    tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
    tab1.plotly_chart(px.bar(Documentation_list, x="Documentation_lists", y="Values",
                      text="Values", color="Documentation_lists"), use_container_width=True)
    tab2.plotly_chart(px.pie(Documentation_list, values='Values',
                      names='Documentation_lists'), use_container_width=True)

with col2:
    st.markdown('##')
    st.subheader("☛ Data")
    st.dataframe(Documentation_list)


st.markdown("---")

st.header("Job Detail Data")
st.dataframe(data_selection)
st.markdown("---")


# # ---- HIDE STREAMLIT STYLE ----
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)


# def my_widget(key):
#     st.subheader('Hello there!')
#     return st.button("Click me " + key)

# # This works in the main area
# clicked = my_widget("first")

# # And within an expander
# my_expander = st.expander("Expand", expanded=True)
# with my_expander:
#     clicked = my_widget("second")

# # AND in st.sidebar!
# with st.sidebar:
#     clicked = my_widget("third")
