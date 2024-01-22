import streamlit as st
import pandas as pd
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Ascii_Art_Generetor",
    page_icon="🤖",
)


st.title("Ascii Art Generator (by Nadia Godje)🎨🎨🎨")

text=st.text_input('Entrez un mot')

text_color = st.color_picker("Choisissez la couleur du mot ", "#000000")
styled_text = f"<p style='color:{text_color}; font-size: 24px;'>{text}</p>"

if st.button("Valider"):
    st.write(styled_text, unsafe_allow_html=True)

