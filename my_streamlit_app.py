import streamlit as st
import pandas as pd
import seaborn as sns


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

df_cars = pd.read_csv(link)


# Here we use "magic commands":

df_cars


viz_correlation = sns.heatmap(df_cars.corr(), 

								center=0,

								cmap = sns.color_palette("vlag", as_cmap=True)

								)


st.pyplot(viz_correlation.figure)


genre = st.radio(
    "Select Country of origin",
    ('Japan', 'USA', 'Europe'))
if genre == 'USA':
	df4 = df_cars.loc[df_cars["continent"] ==" US."]
	df4
if genre == 'Europe':
	df5 = df_cars.loc[df_cars["continent"] ==" Europe."]
	df5
else:
	df6 = df_cars.loc[df_cars["continent"] ==" Japan."]	
	df6

"""genre = st.radio(
    "Select Country of origin",
    ('Japan', 'USA', 'Europe'))

if genre == 'USA':
	df_cars.loc[df_cars[continent] =" US."]
elif genre == 'Japan':
	dfJap = df_cars["continent"].str.contains(" Japan.",regex=True)
	st.write(dfJap)
else:
    dfEu=df_cars["continent"].str.contains(" Europe.",regex=True)
st.write(dfEu)"""""


