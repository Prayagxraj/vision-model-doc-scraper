import streamlit as st
import os

from scraper.model_scraper import get_vision_model_links
from scraper.page_parser import scrape_model_page

OUTPUT_FOLDER = "output/Vision_Models"


def save_model_data(model_name, text):

    model_folder = os.path.join(OUTPUT_FOLDER, model_name)

    os.makedirs(model_folder, exist_ok=True)

    file_path = os.path.join(model_folder, f"{model_name}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)


st.title("Vision Model Documentation Scraper")

st.write("Scrape HuggingFace Vision Model documentation.")

if st.button("Start Scraping"):

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    model_links = get_vision_model_links()

    st.write(f"Found {len(model_links)} vision models")

    progress = st.progress(0)

    for i, link in enumerate(model_links):

        model_name = link.split("/")[-1]

        text = scrape_model_page(link)

        if text:
            save_model_data(model_name, text)

        progress.progress((i + 1) / len(model_links))

    st.success("Scraping completed!")

# show scraped models
if os.path.exists(OUTPUT_FOLDER):

    st.subheader("Scraped Models")

    models = os.listdir(OUTPUT_FOLDER)

    selected = st.selectbox("Select model", models)

    if selected:

        file_path = os.path.join(
            OUTPUT_FOLDER, selected, f"{selected}.txt"
        )

        if os.path.exists(file_path):

            with open(file_path, "r") as f:
                content = f.read()

            st.text_area("Documentation", content[:2000], height=400)