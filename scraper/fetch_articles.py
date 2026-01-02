import requests

def fetch_articles():
    url = "https://support.optisigns.com/api/v2/help_center/articles.json"
    articles = []

    while url:
        response = requests.get(url)
        data = response.json()

        articles.extend(data["articles"])
        url = data.get("next_page")

    return articles
