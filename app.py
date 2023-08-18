import streamlit as st
import pickle

movies_list=pickle.load(open('movies.pkl','rb'))

st.title('Movie Recommender System')
import streamlit as st

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
