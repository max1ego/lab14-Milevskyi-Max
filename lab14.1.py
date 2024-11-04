import requests
import json
import string
from collections import Counter
from bs4 import BeautifulSoup

url = input("Введіть URL веб-сторінки: ")

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    letters_only = [char.lower() for char in text if char.lower() in string.ascii_lowercase]

    letter_counts = Counter(letters_only)

    with open("letter_frequency.json", "w") as file:
        json.dump(letter_counts, file, indent=4)

    print("Частота літер збережена у файлі 'letter_frequency.json'.")

except requests.exceptions.RequestException as e:
    print("Помилка при завантаженні веб-сторінки:", e)

