import os
from scraper.model_scraper import get_vision_model_links
from scraper.page_parser import scrape_model_page

OUTPUT_FOLDER = "output/Vision_Models"


def save_model_data(model_name: str, text: str) -> None:
    """
    Save scraped documentation to a text file.
    """

    model_folder = os.path.join(OUTPUT_FOLDER, model_name)
    os.makedirs(model_folder, exist_ok=True)

    file_path = os.path.join(model_folder, f"{model_name}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)


def main():

    print("\nStarting Vision Model Scraper...\n")

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    model_links = get_vision_model_links()

    if not model_links:
        print("No Vision models found.")
        return

    print(f"Found {len(model_links)} Vision models\n")

    for link in model_links:

        model_name = link.split("/")[-1]

        print(f"Scraping {model_name}...")

        text = scrape_model_page(link)

        if text:
            save_model_data(model_name, text)
            print(f"Saved {model_name}\n")
        else:
            print(f"Skipped {model_name}\n")

    print("Scraping completed successfully!")


if __name__ == "__main__":
    main()