import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x*x)

st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender", ["Male", "Female"])

container = st.container()
container.write("This is written inside the container")
st.write("This is written outside the container")
