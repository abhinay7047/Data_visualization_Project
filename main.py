import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Set page configuration to wide layout
st.set_page_config(layout='wide')

# Read the data from the CSV file
df = pd.read_csv('india.csv')

# Set the title of the Streamlit app
st.title("Welcome to the India")

# Create a list of unique states for the sidebar dropdown
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

# Sidebar for selecting state and parameters
st.sidebar.title('India Ka Data Viz')
selected_state = st.sidebar.selectbox('Select a state', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

# Button to plot the graph
plot = st.sidebar.button('Plot Graph')

# Perform actions when the plot button is clicked
if plot:
    st.text('Size represents primary parameter')
    st.text('Color represents secondary parameter')

    if selected_state == 'Overall India':
        # Plot for India
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District',
                                color_continuous_scale='viridis')

        # Display the plotly chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)
    else:
        # Plot for selected state
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6,
                                size_max=35, mapbox_style="carto-positron", width=1200, height=700,
                                hover_name='District', color_continuous_scale="viridis")

        # Display the plotly chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)
