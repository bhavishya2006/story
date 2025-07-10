import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

all_titles = soup.find_all(name="h3", class_="title")
movie_titles = [title.get_text() for title in all_titles]

movie_titles.reverse()

cleaned_titles = []
for title in movie_titles:
    if ") " in title:
        parts = title.split(") ", 1)
        if len(parts) > 1:
            title = parts[1]
    cleaned_titles.append(title)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for i, movie in enumerate(cleaned_titles, start=1):
        file.write(f"{i}) {movie}\n")
