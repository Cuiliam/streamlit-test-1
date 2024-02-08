
import time

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code


def test_page():
    st.write("Below is a graph hypothetically")

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    #last_rows = np.random.randn(1, 1)
    last_rows = np.array([[1]])
    #print(last_rows)
    st.write(last_rows)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        #new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        new_rows = last_rows + i
        #print(new_rows)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        #time.sleep(0.05)


st.set_page_config(page_title="Test Page")
st.markdown("# Test Page")
st.sidebar.header("Test Page")
st.write(
    """This page is just a test to see if I can make a new page"""
)

test_page()

show_code(test_page)
