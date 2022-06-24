from pages import information, model
import streamlit as st
# Page Settings
favicon = "images/favicon.ico"
st.set_page_config(page_title="garbAIge", page_icon=favicon)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load Animation
animation_symbol1 = "♻️"
animation_symbol2 = "🗑️"
st.markdown(
    f"""
    <div class="snowflake">{animation_symbol1}</div>
    <div class="snowflake">{animation_symbol1}</div>
    <div class="snowflake">{animation_symbol1}</div>
    <div class="snowflake">{animation_symbol1}</div>
    <div class="snowflake">{animation_symbol1}</div>
    <div class="snowflake">{animation_symbol2}</div>
    <div class="snowflake">{animation_symbol2}</div>
    <div class="snowflake">{animation_symbol2}</div>
    <div class="snowflake">{animation_symbol2}</div>
    """,
    unsafe_allow_html=True,
)
PAGES = {
    "Model Demo": model,
    "About The Project": information
}

st.sidebar.title('garbAIge')
selection = st.sidebar.radio("Navigate To", list(PAGES.keys()))
page = PAGES[selection]
page.app()