import requests
import json
from bs4 import BeautifulSoup

with open("url.txt", "r") as file:
    urls = [line.strip() for line in file]

titles = {}

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.find("title")

        titles[url] = title_tag.text if title_tag else "Назва не знайдена"
    
    except requests.RequestException as e:
        titles[url] = f"Не вдалося завантажити сторінку: {e}"

with open("title.json", "w", encoding="utf-8") as file:
    json.dump(titles, file, ensure_ascii=False, indent=4)

print("Назви сторінок збережено у файл title.json.")
