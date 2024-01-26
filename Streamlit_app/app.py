import streamlit as st
from art import text2art

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Ascii_Art_Generetor",
    page_icon="🤖",
)


st.title("Ascii Art Generator (by Nadia Godje)🎨🎨🎨")

text=st.text_input('Entrez un texte')

art_style = st.selectbox("Choisissez le style d'art ASCII :", ["block", "block2", "caligraphy"])

ascii_art = text2art(text, font=art_style)


if st.button("Valider"):
    st.markdown(f'```{ascii_art}```', unsafe_allow_html=True)
