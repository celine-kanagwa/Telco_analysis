import streamlit as st 
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns

from plot_relations import plot_relations

import sys
sys.path.append('..')
from sql.query import fetchall

# imports datasets
clean_data = pd.read_csv('../Data/clean_data.csv')
user_data = pd.read_csv('../Data/all_user_data.csv')
experience_data = pd.read_csv('../Data/experience_data.csv')


# project description
def description_function():
	pass

# data analysis
def analysis_function():
	# task 1
	st.header('Task 1')
	# dataset in whole and columns used in it
	st.subheader('Dataset in whole(Sample of 100 values)')
	st.dataframe(clean_data[:100])

	# aggregating per user using msind
	st.subheader('Agregating per user information(Sample of 100 Users')
	st.dataframe(user_data[:100])

	# mean median describe and brief description
	st.subheader('Statistical description of data')
	st.dataframe(user_data.describe())

	# total dl and ul vs applications
	st.subheader('Total download and upload bytes vs applications')
	
	plot_list = ['Social Media DL (Bytes)', 'Social Media UL (Bytes)','Google DL (Bytes)','Google UL (Bytes)','Email DL (Bytes)','Email UL (Bytes)','Youtube DL (Bytes)','Youtube UL (Bytes)','Netflix DL (Bytes)','Netflix UL (Bytes)','Gaming DL (Bytes)', 'Gaming UL (Bytes)']
	view_plots = st.multiselect('Choose plots to view',
			plot_list
		)
	
	sample_size = st.slider('Sample Size', 1000, int(len(clean_data)))
	for figure in view_plots:
		main = figure
		plot = plot_relations(clean_data[['Dur. (ms).1','Dur. (ms)','Total DL (Bytes)','Total UL (Bytes)',main]][:sample_size], main)
		st.pyplot(plot)
	# mean of deciles


	# task 2
	st.header('Task 2')
	# engagement clusters graph and experience
	st.subheader('Engagement Clusters graph, Duration vs Total DL')
	fig = px.scatter(user_data,x='Dur. (ms)',y='Total DL (Bytes)',color='Cluster Engagement', log_x=True, size_max=60)
	fig.update_layout(width=800)
	st.write(fig)
	# top 3 most used applications

	# task 3
	# experience clusters graph
	st.subheader('Experience Clusters graph, Avg RTT DL (ms) vs DL TP < 50 Kbps (%)')
	fig = px.scatter(user_data,x='Avg RTT DL (ms)',y='DL TP < 50 Kbps (%)',color='Cluster Experience', log_x=True, size_max=60)
	fig.update_layout(width=800)
	st.write(fig)

	# task 4
	st.header('Task 4')
	# top 10 most satisfied customers
	st.subheader('Top 10 most satisfied customers')
	sample_size = st.slider('Sample Size', 10, int(len(experience_data)))
	st.dataframe(experience_data.sort_values('Satisfaction Score',axis=0, ascending=False, inplace=False)[:sample_size])
	# screenshot of db fetch



# model prediction testing
def ai_function():
	pass

# sidebar menu
with st.sidebar:
	selected = option_menu(
			menu_title = 'Menu',
			options = ['Analysis']
		)

if selected == 'Project Description':
	st.title('Project Description')
	description_function()

if selected == 'Analysis':
	st.title('Analysis')
	analysis_function()

if selected == 'AI':
	ai_function()

if selected == 'About Me':
	st.title('About Me')