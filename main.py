import streamlit as st
import google.generativeai as genai
import os
#import config

st.title('Book Recommender')
st.divider()
st.write('Explore new books tailored just for you! Input your favorite genres or books, and our Book Recommendation System will suggest your next great read. Enjoy')
## summary of webapp/ tiny description


gemini_key = st.secrets["gemini_api_key"]
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel("gemini-2.0-flash")

tab1, tab2 = st.tabs(['Fiction Books Genre', ' Non-fiction Books Genre'])

with tab1:

    st.header('Fiction Books')
    #st.write('Select your preferred book type')
    
    fiction_books =  ['sci-fi', 'fantasy', 'dystopian', 'mystery', 'horror', 'thriller', 'romance']
    # allow the user to select multiple genres at once (most classics discuss various themes)

    st.subheader('Book Genre')
    fiction_genres= st.multiselect(
                'Select your preferred book genre',
               # ['sci-fi', 'fantasy', 'dystopian', 'mystery', 'horror', 'thriller', 'romance'] 
                fiction_books)
    # give user the option to select the number of books to be recommended
    st.subheader('Number of books to be recommended')
    r_books = st.number_input("Number of books to recommend", min_value=1 , step=1)

    st.subheader("Number of pages")
    # + 200 pages
    # - 200 pages
    # 150 ~ 200 pages
    nf_pages = st.selectbox('How many pages should the book be?',
                         ('More than 200 pages', 'Less than 200 pages' , 'Between 150 pages and 200 pages'))
    fiction_prompt = f"Recommend a list of {r_books} fiction books with each boook containing the folowing genres: {fiction_genres} and being {nf_pages}"
    

    #prompt = PromptTemplate(input_variables=["booktype","n_pages", "genre"] ,
    #                       template="Generate a list of ten {booktype} {genre} books with each book being {n_pages} ")
    submitted = st.button('Generate Recommendations')
    if submitted:
        response = model.generate_content(fiction_prompt)
        st.success(response.text)

with tab2:
    st.header('Non-fiction Books')

    nonfiction_books = ['Autobiography', 'Biography', 'Academic', 'Cookbook', 'Science', 'History', 'Travel', 'True crime', 'Art & photography']

    st.subheader('Book Genre')
    nonfiction_genres = st.multiselect('Select your preferred book genre', nonfiction_books)

    st.subheader('Number of books to be recommended')
    rnf_books = st.number_input("Number of books", min_value=1 , step=1)

    st.subheader("Number of pages")
    f_pages = st.selectbox(
            'How many pages do you want in your recommended book(s)?',
            ('More than 200 pages', 'Less than 200 pages', 'Between 150 pages and 200 pages'))

    non_fiction_prompt = f"Recommend a list of {rnf_books} non-fiction books with each book containing the following genres:  {nonfiction_genres} being {f_pages}"
    nf_submitted = st.button('Generate')

    if nf_submitted:
        response = model.generate_content(non_fiction_prompt)
        st.success(response.text)


# Book summarizer
# (User enters the selected book in a text field and clicks a button. Once clicked, the sys will generate text that contains the summary of the selected book)
with st.form('form2'):
    st.subheader('Book Summarizer')
    book_title = st.text_input('Enter your selected book title', '')
    summary_prompt = f"Summarize the book {book_title} in three paragraph"
    #summary_prompt = PromptTemplate(input_variables=["booktitle"] ,
    #                       template= "_Summarize the book {booktitle} in one paragraph")
    summarize_btn = st.form_submit_button("Summarize")
    if summarize_btn:
        response = model.generate_content(summary_prompt)
        st.success(response.text)

# Need another feature (about the author?) , Discussion bot!

with st.sidebar:
    # Add a page for discussion bot
    #st.subheader("This is a sidebar")
    #st.page_link("main.py", label="Home")
    st.page_link("pages/discussion_bot.py", label="Discussion Chatbot")
