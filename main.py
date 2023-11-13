import streamlit as st
import openai
#import config
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
#from dotenv import load_dotenv, find_dotenv

st.title('Book Recommender')
st.divider()
st.write('Explore new books tailored just for you! Input your favorite genres or books, and our Book Recommendation System will suggest your next great read. Enjoy')
## summary of webapp/ tiny description
#load_dotenv(find_dotenv())
#openai_api_key = os.getenv("OPENAI_API_KEY")
with st.form('form1'):

    st.subheader('Book type')
    st.write('Select your preferred book type')
    book_type = st.radio(
            "Book type",
            ["Non-fiction", "Fiction"]) 

# display different option box for non-fiction
# if user selects non-fiction option --> display non-fiction options , (same for 
## fiction genres
    if book_type == "Fiction":

        st.subheader('Fiction Book Genre')
        options = st.multiselect(
                'Select up to five book genres that you prefer',
                ['Sci-Fi', 'Fantasy', 'Dystopian', 'Mystery', 'Horror', 'Thriller', 'Romance'])

    if book_type == "Non-fiction":
          st.subheader('Non-fiction Books genre')
          options = st.multiselect(
                   'Select up to five book genres that you prefer',
                   ['Autobiograhy', 'Biography', 'Academic', 'Cookbook', 'Science', 'History', 'Travel', 'True crime', 'Art & photography'])
   
    st.subheader("Number of pages")
    # + 200 pages
    # - 200 pages
    # 150 ~ 200 pages
    pages = st.selectbox(
            'How many pages do you want in your recommended book(s)?',
            ('More than 200 pages', 'Less than 200 pages', 'Between 150 pages and 200 pages'))
   

    #submitted = st.form_submit_button('Generate') 
