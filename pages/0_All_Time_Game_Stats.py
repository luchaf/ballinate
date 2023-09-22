from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code


def all_time_game_stats() -> None:

    st.write("display all time game stats here")


st.set_page_config(page_title="All time game stats", page_icon="📹")
st.markdown("# All time game stats")
st.sidebar.header("All time game stats")

all_time_game_stats()

#show_code(animation_demo)
