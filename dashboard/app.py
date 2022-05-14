import streamlit as st
import pandas as pd 
import plotly.figure_factory as ff
import plotly.express as px
from PIL import Image

# IMPORTING Data set

Dataset = pd.read_csv('../Data/Week1_challenge_data_source.csv')
CleanDataset = pd.read_csv('../Data/clean_data.csv')
Handset_Type_image= Image.open('../image/HandsetType.JPG')
Handset_Manufacture= Image.open('../image/ManufactureHandset.JPG')

SIDEBAR_OPTION_PROJECT_WIKI = "Project Wiki"
SIDEBAR_OPTION_ANALYSIS = "Data Exploration"
SIDEBAR_OPTION_FORECAST = "Predict"
SIDEBAR_OPTION_ABOUT= "About Me"


SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_WIKI, SIDEBAR_OPTION_ANALYSIS, SIDEBAR_OPTION_FORECAST, SIDEBAR_OPTION_ABOUT]



def wiki_section():

    
    st.subheader("User Analytics in the Telecommunication Industry")
    
    with st.expander("Short introduction about Telecommunication Industry challenge"):
         st.subheader(" Task 1 - User Overview analysis ")
         st.write("""
         The lifeblood of any business is its customers. Businesses are always finding ways 
         to better understand their customers so that they can provide more efficient and 
         tailored solutions to them. Exploratory Data Analysis is a fundamental step in the data science process.
        It involves all the processes used to familiarise oneself with the data and
        explore initial insights that will inform further steps in the data science process.
         """)
         st.subheader("Task 2 - User Engagement analysis")
         st.write("""
         As telecom brands are the data providers of all online activities, 
         meeting user requirements, and creating an engaging user experience is a prerequisite for them.
        uilding & improving the QoS (Quality of Service) to leverage the mobile platforms 
        and to get more users for the business is good but the success of the business would be determined
        by the user engagement and activity of the customers on available apps.

         """)

         st.subheader("Task 3 - Experience Analytics")
         st.write("""
        The Telecommunication industry has experienced a great revolution since the last decade.
        Mobile devices have become the new fashion trend and play a vital role in everyone's life. 
        The success of the mobile industry is largely dependent on its consumers. 
        Therefore, it is necessary for the vendors to focus on their target audience 
        i.e. what are the needs and requirements of their consumers and how they feel and perceive their products. 
        Tracking & evaluation of customers’ experience can help the organizations to optimize their products and services
        so that it meets the evolving user expectations, needs, and acceptance.
        """)
         st.subheader("Task 4 - Satisfaction Analysis")
         st.write("""
        Assuming that the satisfaction of a user is dependent on user engagement and experience, 
        you’re expected in this section to analyze customer satisfaction in depth. 

        """)

         

def visual_analysis_section():
     st.title(" Data Analysis ")
    #displaying data 
     col1, col2 = st.columns(2)

     with col1:
         st.text('Telecomunication Data set')
         st.dataframe(Dataset)

     with col2:
          st.text('Cleaned Telecommunication Dataset')
          st.dataframe(CleanDataset)

     st.title("Visualization ")
     col1, col2 =st.columns(2)
     
     #the top 10 handsets used by the customers.
     with col1:

           
        st.image(Handset_Type_image, caption='Top 10 handset used by customer')

    #top 3 handset manufacturers      
     with col2:
    
        st.image(Handset_Manufacture, caption='Top 3 handset manufacturers  ')
    
def Prediction_section():
    st.write(" Data Analysis And Visualization ")

    #PredModel()
   
def About_section():
    st.write(" Data Analysis And Visualization ")

     
     #MeetTeam()


def main():
    st.sidebar.success("Choose an Option")
    SIDEBAR_STATUS = st.sidebar.selectbox('Menu Option',SIDEBAR_OPTIONS)

    if SIDEBAR_STATUS == SIDEBAR_OPTION_PROJECT_WIKI:
        wiki_section()
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_ANALYSIS:
        visual_analysis_section()
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_FORECAST:
        Prediction_section()
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_ABOUT:
        About_section()
    else:
        pass
main()  