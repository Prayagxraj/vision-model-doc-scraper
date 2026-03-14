import requests
from bs4 import BeautifulSoup

BASE_URL = "https://huggingface.co"
GITHUB_MODELS_URL = (
    "https://github.com/huggingface/transformers/tree/main/docs/source/en/model_doc"
)

HEADERS = {"User-Agent": "Mozilla/5.0"}


VISION_KEYWORDS = [
    "vit",
    "swin",
    "detr",
    "beit",
    "convnext",
    "segformer",
    "mask2former",
    "yolos",
]


def get_vision_model_links() -> list:
    """
    Fetch Vision model documentation links from the HuggingFace repo.
    """

    try:
        response = requests.get(GITHUB_MODELS_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching model list: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    model_links = []

    for tag in soup.select("a[href*='model_doc']"):

        href = tag.get("href")

        if href and href.endswith(".md"):

            model_name = href.split("/")[-1].replace(".md", "")

         
            if any(v in model_name.lower() for v in VISION_KEYWORDS):

                doc_url = f"{BASE_URL}/docs/transformers/model_doc/{model_name}"

                model_links.append(doc_url)

    return sorted(set(model_links))