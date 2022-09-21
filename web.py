import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as pg

# Function to plot bar and pie chart and return best tech
def plots_column (Title,X,Y,Data):
    #Bar chart
    Bar = px.bar(Data, x=X, y=Y,text=Y, color=X)
    Bar.update_layout(title_text=Title, title_x=0.5)
    #Pie Chart
    Pie = px.pie(Data, values=Y,names=X)
    Pie.update_layout(title_text=Title, title_x=0.5)
    # Set the column to show plot and data side by side
    col1, col2 = st.columns(2, gap="large")
    with col1:
        # Tabs to point Pie Chart and Bar Chart
        tab1, tab2 = st.tabs(["📶 Chart", "📉 Pie"])
        tab1.plotly_chart(Bar, use_container_width=True)
        tab2.plotly_chart(Pie, use_container_width=True)

    with col2:
        st.markdown('##')
        st.subheader("☛ Data")
        st.dataframe(Data)
    st.markdown("---")
    # Identify the best Tech
    Best = ''.join(Data[X].head(1).values)
    return Best

st.set_page_config(page_title="Analysis Dashboard",page_icon=":video_game:", layout="wide")

st.title(":bar_chart: Trends at Gaming Industry")
# st.markdown('#')
 
@st.cache
def collect_data(filename):
    data = pd.read_csv(filename)
    return data


data = collect_data("data//Aswift_Jobs_data.csv")
Country_code = collect_data("data//Country_code.csv")
# data = data.iloc[:, 1:]

Countries = data.Country.value_counts()
Countries = pd.DataFrame({'Country': Countries.index, 'Num_jobs': Countries.values})

Country_job = pd.merge(Countries, Country_code, on='Country', how='inner')

# Add Filters
st.sidebar.header(('Filters'))
Country = st.sidebar.multiselect('Select the Country', options=data['Country'].unique(), default=['United Kingdom'])
if st.sidebar.checkbox('Select all'):
    Country = list(data['Country'].unique())

Job_Mode = st.sidebar.multiselect(
    'Select the Job Mode', options=data['Job_Mode'].unique(), default=data['Job_Mode'].unique())

data_selection = data.query("Country ==@Country & Job_Mode==@Job_Mode")

# World_map
st.header(f'Global Jobs Posted - {len(data)}')
Country_points = dict(type='choropleth', locations=Country_job['Code'], z=Country_job['Num_jobs'], text=Country_job['Country'])
layout = dict(geo = dict(projection = {'type':'robinson'}))
W_Map = pg.Figure(data=[Country_points], layout=layout)
W_Map.update_layout(title_text='Jobs posted all over the world based on the Job listing Website', title_x=0.5)
Countries.sort_values(by=['Num_jobs'], inplace=True, ascending=False)
st.plotly_chart(W_Map)

C_best = plots_column('Jobs posted all over the world based on the Job listing Website','Country','Num_jobs',Countries)
st.success(f'From the above chart, we can say that **{C_best}** has more jobs in the Gaming Industry based on the Job listing Website')

Clist = ', '.join(Country)
st.header(f'Selected Country: {Clist}')
st.subheader(f'Jobs based on selection: {len(data_selection)}')



# job Positions
st.subheader("Trending Job Positions in Gaming Industry")
Role = data_selection.Job_Role.value_counts()
Role = pd.DataFrame({'Roles': Role.index, 'Values': Role.values})
R_best = plots_column('Most required job postions in Gaming Industry','Roles','Values',Role)
st.success(f'From the above chart, we can say that most of the companies are looking for **{R_best}** in the Gaming Industry based on the selection')

# Software_list
st.subheader("Trending Softwares required to know in the Gaming Industry")
Software_list = (data_selection.iloc[:, 10:17]).sum(axis=0)
Software_list = pd.DataFrame({'Software_lists': Software_list.index, 'Values': Software_list.values})
Software_list.sort_values(by=['Values'], inplace=True, ascending=False)
S_best = plots_column('Most required softwares to learn in Gaming Industry','Software_lists','Values',Software_list)
st.success(f'From the above chart, we can say that most of the companies are looking for candidates how knows **{S_best}** software in the Gaming Industry based on the selection')

# Programming Languages
st.subheader("Trending Programming Languages required to know in Gaming Industry")
Program_language = (data_selection.iloc[:, 17:22]).sum(axis=0)
Program_language = pd.DataFrame({'Program_languages': Program_language.index, 'Values': Program_language.values})
Program_language.sort_values(by=['Values'], inplace=True, ascending=False)
P_best = plots_column('Trend Programming Languages to learn in Gaming Industry','Program_languages','Values',Program_language)
st.success(f'From the above chart, we can say that most of the companies are looking for candidates how knows **{P_best}** as Programming Language in the Gaming Industry based on the selection')

# Game Engines
st.subheader("Trending Game Engines required to know in Gaming Industry")
Gaming_engine = (data_selection.iloc[:, 22:26]).sum(axis=0)
Gaming_engine = pd.DataFrame({'Gaming_engines': Gaming_engine.index, 'Values': Gaming_engine.values})
Gaming_engine.sort_values(by=['Values'], inplace=True, ascending=False)
G_best = plots_column('Trend Game Engines to learn in Gaming Industry','Gaming_engines','Values',Gaming_engine)
st.success(f'From the above chart, we can say that most of the companies are looking for candidates how knows **{G_best}** Game Engine in the Gaming Industry based on the selection')

#Data bases
st.subheader("Trending Databases required to know in Gaming Industry")
Database_list = (data_selection.iloc[:, 26:31]).sum(axis=0)
Database_list = pd.DataFrame({'Database_lists': Database_list.index, 'Values': Database_list.values})
Database_list.sort_values(by=['Values'], inplace=True, ascending=False)
D_best = plots_column('Trend DataBases to learn in Gaming Industry','Database_lists','Values',Database_list)
st.success(f'From the above chart, we can say that most of the companies are looking for candidates how knows **{D_best}** Database in the Gaming Industry based on the selection')

#Console List
st.subheader("Consoles required to know in Gaming Industry")
Console_list = (data_selection.iloc[:, 49:53]).sum(axis=0)
Console_list = pd.DataFrame({'Console_lists': Console_list.index, 'Values': Console_list.values})
Console_list.sort_values(by=['Values'], inplace=True, ascending=False)
Cl_best = plots_column('Consoles to learn in Gaming Industry','Console_lists','Values',Console_list)
st.success(f'From the above chart, we can say that most of the companies are looking for candidates how knows **{Cl_best}** console in the Gaming Industry based on the selection')

# Gaming_knowledge
st.subheader("Gaming knowledge required to know in Gaming Industry")
Gaming_knowledge = (data_selection.iloc[:, 31:42]).sum(axis=0)
Gaming_knowledge = pd.DataFrame({'Gaming_knowledges': Gaming_knowledge.index, 'Values': Gaming_knowledge.values})
Gaming_knowledge.sort_values(by=['Values'], inplace=True, ascending=False)
GK_best = plots_column('Gaming knowledge to learn in Gaming Industry','Gaming_knowledges','Values',Gaming_knowledge)
st.success(f'Most of the companies requires for candidates how knows the above gaming technologies like **{GK_best}** in the Gaming Industry based on the selection')

# Additional Knowledge
st.subheader("Additional Technology required to know in Gaming Industry")
Technology_list = (data_selection.iloc[:, 42:49]).sum(axis=0)
Technology_list = pd.DataFrame({'Technology_lists': Technology_list.index, 'Values': Technology_list.values})
Technology_list.sort_values(by=['Values'], inplace=True, ascending=False)
T_best = plots_column('Additional knowledges to learn in Gaming Industry','Technology_lists','Values',Technology_list)
st.success(f'Most of the companies requires for candidates how knows the above additional technologies like **{T_best}** in the Gaming Industry based on the selection')


st.header("Job Detail Data")
st.dataframe(data_selection)
st.markdown("---")

