import streamlit as st
import fastf1 as ff1

from PIL import Image

from src.Data_Viz.data_analysis import data_analysis
from src.Data_Viz.sectors import sectors
from src.Data_Viz.speed import speed
from src.Data_Viz.tyre_strategy import tyre_strategy
from src.Data_Viz.tyre_performance import tyre_performance
from src.Data_Viz.track_speed_gear import track_speed_gear

# Título página inicial
st.set_page_config(
    page_title="FTS F1",
    page_icon="🏁",
    layout="wide",
    initial_sidebar_state="expanded"
)

image = Image.open('./images/f1_capa.jpg')

st.image(image, use_column_width=True)
st.write("<div align='center'><h2><i>Explore F1 Data with Artificial Intelligence</i></h2></div>",
         unsafe_allow_html=True)
st.write("")

# Enable the cache
ff1.Cache.enable_cache('cache_data')
       
seasons = [2021, 2022, 2023, 2024]
session_names = ['Session1', 'Session2', 'Session3', 'Session4', 'Session5']

# Criar a interface de seleção de 'season' e 'stage'
selected_season = st.selectbox('Select Season:', seasons, key='season_data', index=seasons.index(2024))

events_data = ff1.get_event_schedule(selected_season)
#st.write(events_data)
events = events_data['EventName']

# Criar a interface de seleção de 'season' e 'stage'
selected_event = st.selectbox('Select Event:', events, key='event_data', index=0)
#st.write(selected_event)

sessions_data = ff1.get_event(selected_season, selected_event)
sessions = sessions_data[session_names]
#st.write(sessions_data)
#st.write(sessions)

session_mapping = {
    'Practice 1': 1,
    'Practice 2': 2,
    'Practice 3': 3
}

# Criar a interface de seleção de 'season' e 'stage'
selected_session = st.selectbox('Select Session:', sessions, key='session_data')

try:
    data = ff1.get_session(selected_season, selected_event, selected_session)
    data.load()
except:
    session_testing = session_mapping.get(selected_session, 1)
    data = ff1.get_testing_session(selected_season, 1, session_testing)
    data.load()

#st.write(data)

tabs = st.tabs(["Best Lap Data Analysis", "Sectors", "Speed", "Tyre Strategy", "Tyre Performance", "Track Speed and Gear"])

with tabs[0]:

    data_analysis(data, selected_season, selected_event, selected_session)

with tabs[1]:  

    sectors(data, selected_season, selected_event, selected_session)

with tabs[2]: 

    speed(data, selected_season, selected_event, selected_session)

with tabs[3]:

    tyre_strategy(data, selected_season, selected_event, selected_session)
    
with tabs[4]:
        
    tyre_performance(data, selected_season, selected_event, selected_session)

with tabs[5]:
    
    track_speed_gear(data, selected_season, selected_event, selected_session)

st.markdown("<h2 style='text-align: center; color: grey; font-size: 14px;'>Version 1.0.0 - Full Time Sports </h2>", unsafe_allow_html=True)

