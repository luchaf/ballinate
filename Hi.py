import streamlit as st
import datetime
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Input game results",
        page_icon="100",
    )

    title = st.text_input('copy paste game results from whatsapp chat here:')
    #st.write('Game results', title)

    d = st.date_input("Day to document the results:", datetime.datetime.now())
    #st.write('You chose this date:', d)


    #st.write("# :balloon: Welcome to Streamlit! 👋")

    #st.sidebar.success("Select a demo above.")




if __name__ == "__main__":
    run()
