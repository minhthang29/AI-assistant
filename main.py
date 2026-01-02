from scraper.fetch_articles import fetch_articles
from scraper.convert_markdown import html_to_markdown, save_markdown
from uploader.upload_vector_store import create_vector_store, upload_file
import hashlib
import os

def slugify(url):
    return url.rstrip("/").split("/")[-1]


def hash_content(content):
    return hashlib.sha256(content.encode()).hexdigest()


def main():
    articles = fetch_articles()
    vector_store = create_vector_store()

    added = 0

    for article in articles[:30]: 
        slug = slugify(article["html_url"])
        markdown = html_to_markdown(article["body"])
        save_markdown(slug, markdown)

        file_path = f"data/markdown/{slug}.md"
        upload_file(vector_store.id, file_path)
        added += 1

    print(f"Uploaded {added} articles")


if __name__ == "__main__":
    main()
