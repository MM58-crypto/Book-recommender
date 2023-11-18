import streamlit as st
import openai
import os
import config
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv

st.title('Book Recommender')
st.divider()
st.write('Explore new books tailored just for you! Input your favorite genres or books, and our Book Recommendation System will suggest your next great read. Enjoy')
## summary of webapp/ tiny description
load_dotenv(find_dotenv())
openai_api_key = os.getenv("OPENAI_API_KEY")
def generate_response(input_text):
    llm= OpenAI(temperature=0.7, openai_api_key=config.OPENAI_API_KEY)
    st.success(llm(input_text))

with st.form('form1'):

    st.subheader('Book type')
    st.write('Select your preferred book type')
    
    fiction_books =  ['sci-fi', 'fantasy', 'dystopian', 'mystery', 'horror', 'thriller', 'romance']
    nonfiction_books = ['Autobiograhy', 'Biography', 'Academic', 'Cookbook', 'Science', 'History', 'Travel', 'True crime', 'Art & photography']

  #  if 'selected_books' not in st.session_state:
  #     st.session_state.selected_books = []

    book_type = st.radio(
            "Book type",
            ["Non-fiction", "Fiction"]) 

# display different option box for non-fiction
# if user selects non-fiction option --> display non-fiction options , (same for 
## fiction genres)
 
#book_type == "Fiction":
       # fiction_genres = st.session_state.selected_books
    st.caption("(Select only from the dropdown list of your preferred book type)")
    st.subheader('Fiction Book Genre')
    fiction_genres= st.selectbox(
                'Select your preferred book genre',
               # ['sci-fi', 'fantasy', 'dystopian', 'mystery', 'horror', 'thriller', 'romance'] 
                fiction_books)
 
   # ron_fiction_genres = st.session_state.selected_books
    st.subheader('Non-fiction Books genre')
    non_fiction_genres = st.selectbox(
            'Select your preferred book genre',
                #   ['Autobiograhy', 'Biography', 'Academic', 'Cookbook', 'Science', 'History', 'Travel', 'True crime', 'Art & photography']
             nonfiction_books)
    st.subheader("Number of pages")
    # + 200 pages
    # - 200 pages
    # 150 ~ 200 pages
    pages = st.selectbox(
            'How many pages do you want in your recommended book(s)?',
            ('More than 200 pages', 'Less than 200 pages', 'Between 150 pages and 200 pages'))
   
    prompt = PromptTemplate(input_variables=["booktype","n_pages", "genre"] ,
                           template="Generate a list of ten {booktype} {genre} books with each book being {n_pages} ")
    submitted = st.form_submit_button('Generate')
    if submitted:
        if book_type == "Fiction":
            generate_response(prompt.format(booktype=book_type, n_pages=pages, genre=fiction_genres))
        elif book_type == "Non-fiction":
            generate_response(prompt.format(booktype=book_type, n_pages=pages, genre=non_fiction_genres))
# Book summarizer
# (User enters the selected book in a text field and clicks a button. Once clicked, the sys will generate text that contains the summary of the selected book)
with st.form('form2'):
    st.subheader('Book Summarizer')
    book_title = st.text_input('Enter your selected book title', '')
    summary_prompt = PromptTemplate(input_variables=["booktitle"] ,
                           template= "_Summarize the book {booktitle} in one paragraph")
    summarize_btn = st.form_submit_button("Summarize")

    if summarize_btn:
        generate_response(summary_prompt.format(booktitle=book_title))


