from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os

def html_to_markdown(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["nav", "footer", "script", "style", "aside"]):
        tag.decompose()

    markdown = md(str(soup), heading_style="ATX")
    return markdown


def save_markdown(slug, content):
    import logging
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        target_dir = os.path.abspath(os.path.join(base_dir, "..", "data", "markdown"))
        os.makedirs(target_dir, exist_ok=True)

        path = os.path.join(target_dir, f"{slug}.md")

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return path
    except Exception as e:
        print(f"Failed to save markdown for {slug}: {e}")
        raise
