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


-------------------------- STEPS TO RUN THIS PROJECTT------------------------------------------

## How to Run the Project

Follow these steps to run the project on your system.

### 1. Clone the repository

```bash
git clone https://github.com/Prayagxraj/vision-model-doc-scraper.git
```

### 2. Navigate to the project directory

```bash
cd vision-model-doc-scraper
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 5. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the project

```bash
python main.py
```

### 7. Run the Streamlit application

```bash
streamlit run app.py
```

After running the command the Streamlit interface will open in the browser where the scraping process can be triggered and the results can be viewed
streamlit run app.py
 This launches a small web interface that allows users to view the extracted documentation.
