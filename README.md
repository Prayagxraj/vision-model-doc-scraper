Vision Model Documentation Scraper

This project is a simple web scraper that collects documentation for Vision Models from the Hugging Face Transformers documentation and stores it locally in a structured folder format.

The script navigates through the Transformers documentation, gathers links to the vision model pages, extracts the main documentation content, and saves the information into .txt files for each model.


Source Website

Hugging Face Transformers Documentation
https://huggingface.co/docs/transformers/index

Navigation path used:
Docs → API → Models → Vision Models


Features

- Scrapes documentation for multiple vision models
- Extracts the main content from each model’s documentation page
- Automatically creates folders for each model
- Saves the scraped content as .txt files
- Optional Streamlit interface to run the scraper through a simple web UI


How It Works

1. The script first collects model documentation links from the Hugging Face Transformers repository.
2. It filters the links to keep only vision-related models.
3. For every model found:
   - A folder is created inside Vision_Models
   - The model documentation page is scraped
   - The extracted content is saved as a .txt file.


Installation

Install the required dependencies before running the project:

pip install -r requirements.txt


Running the Scraper

CLI Version

python main.py

This will:
- scrape vision model documentation
- create folders automatically
- store the scraped content locally.


Streamlit Interface 


streamlit run app.py

This launches a small web interface where you can:
- start the scraping process
- monitor the progress
- preview the scraped documentation.
