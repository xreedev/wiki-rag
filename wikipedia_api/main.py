import requests

def get_wikipedia_text(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,
        "titles": title
    }
    response = requests.get(url, params=params)
    pages = response.json()["query"]["pages"]
    page = next(iter(pages.values()))
    return page.get("extract", "")