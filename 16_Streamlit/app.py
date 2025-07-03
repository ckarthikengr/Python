import streamlit as st
import pandas as pd
import numpy as np

## Title of an application
st.title("Hello streamlit")

## Display simple text
st.write("This is simple text")

df = pd.DataFrame(
    {
        'first_column':[1,2,3,4],
        'second_column':[10,20,30,40]
    }
)

## Display the Dataframe

st.write("Here is the dataframe")

st.write(df)


## Create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)