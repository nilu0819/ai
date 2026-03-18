import streamlit as st

st.title("my first streamlit app by nilesh ram")

st.write("")

st,header("select a number")
number=st.slider("select a number",1,546,5)

st,subheader('result')
squred_number=number * number

st.subheader('result')
squred_number(f'the squre of **{number} ** is ** {squred_number}**.')
