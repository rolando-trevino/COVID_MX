"""Main module for the streamlit app"""

import streamlit as st

import src.pages.covid_19_mx

PAGES = {
    "COVID MX": src.pages.covid_19_mx,
}


def main():
    st.sidebar.write("# COVID MX")

    page = PAGES["COVID MX"]

    page.write()

    st.sidebar.write("---")
    st.sidebar.info(
        "Author: Rolando Treviño Lozano\n\nRepository: [COVID MX](https://github.com/rolando-trevino/COVID_MX)"
    )


if __name__ == "__main__":

    st.set_page_config(
        page_title="COVID MX",
        page_icon=(":computer:"),
        layout="centered",
        initial_sidebar_state="auto",
    )

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    main()
