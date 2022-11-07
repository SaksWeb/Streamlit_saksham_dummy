import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import altair as alt
from streamlit_lottie import st_lottie
import requests
import json
from streamlit_option_menu import option_menu

with st.sidebar:
    selected=option_menu(menu_title=None, options=["Home","Projects","Contact"],icons=["house","book","envelope"],orientation="horizontal",)


def load_lottieurl(url:str):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

col5,col7=st.columns(2)


lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_1pxqjqps.json")
lottie_hello2 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_o6spyjnc.json")
lottie_hello3 = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_wo5lnbyz.json")
lottie_hello4 = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_8zaahewg.json")
lottie_hello5 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_qp1q7mct.json")

with col7:
    st_lottie(lottie_hello,key="hello")

a= [1,2,3,4,5,6,7,8]
n=np.array(a)
nd = n.reshape((2,4))
dis = {
    "name":"saksham",
    "age":20,
    
}
data = pd.read_csv("advertising.csv")
with col5:

    st.title("Welcome to my demo page")
    st.markdown("""
    I Saksham Shrivastava welcomes you

    """)
    welcome_but = st.button("click here before you start ")
    if welcome_but :
        st.header("Here's you are watching an advertising data")

        st.dataframe(data)
        st.write("and it's only for demo")
        st.json(dis)


#@st.cache
#def ret_time(a):
#    time.sleep(5)
#    return time.time()
#if st.checkbox("1"):
#    st.write(ret_time(1))
#
#if st.checkbox("2"):
#    st.write(ret_time(2))


data2 = pd.DataFrame(
    np.random.randn(100,5),
    columns=['a','b','c','d','e']
)
col8,col9=st.columns(2)
with col8:
    st_lottie(lottie_hello2,key="sa")

with col9:

    st.subheader("see the data below")
    st.write(data2)
    data2_but = st.button("click here to see graphs for above data")
    if data2_but:
        st.write("line chart")
        st.line_chart(data2)
        st.write("Area chart")
        st.area_chart(data2)
        st.write("Bar chart")
        st.bar_chart(data2)
        st.write("Scatter plot")
        plt.scatter(data2['a'],data2['b'])
        #st.pyplot()
        chart=alt.Chart(data2).mark_circle().encode(
            x='a',y='b'
        )
        st.altair_chart(chart)
col3,col4=st.columns(2)
with col4:
    st_lottie(lottie_hello3,key="ks")
with col3:

    dec_but= st.button("click here for decision tree")
    if dec_but:
    
        st.graphviz_chart("""
        digraph{
            saksham -> shrivastava
            shivansh -> mishra
            cs -> ds
            ds -> cs
            ds -> ml
            ml -> AI
            cs -> ml
            cs -> AI
            ds -> saksham
            ds -> shivansh
            saksham -> ml
            saksham -> AI
            shivansh  -> ml
            shivansh -> AI
    
        }
        """)
#st.map()
entry_but=st.button("Entry form")
if entry_but :

    st.title("Entry form start's from here")
    col1,col2=st.columns(2)
    col10,col11=st.columns(2)
    with col1:

        name= st.text_input("Name")
        st.write(name)
        address=st.text_area("Adress")
        st.number_input("enter number")
        st.radio("colours",["red","green","blue"])

    with col2:

        st.selectbox("colours",["red","green","blue"])
        st.multiselect("colours",["red","green","blue"])

        st.date_input("date?")
        st.time_input("time?")
        st.checkbox("Accept T&C")
        if st.button("Submit"):
            st.write("Submitted")
    with col10:
        st_lottie(lottie_hello4,key="ha")

    with col11:
        st_lottie(lottie_hello5,key="m")




    st.slider("age",1,99)
    st.warning("Note :- Don't upload any file for now")
    file=st.file_uploader("upload a file")




but1=st.button("click here for progress bar and wait for balloons")
if but1:
    progress=st.progress(0)

    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
    st.balloons()

if st.button("Some more functions"):
    st.write("Below lines are only for time pass")
    st.error("error")
    st.success("success")
    st.info("information")
    st.exception(RuntimeError("Error"))