# Import necessary libraries: 'requests' to fetch web content and 'BeautifulSoup' to parse it.
import requests
from bs4 import BeautifulSoup

# The URL of the archived Empire's "100 Best Movies" page to be scraped.
# Using the Wayback Machine ensures the website structure remains consistent.
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

try:
    # --- 1. Fetching the Website Content ---
    response = requests.get(URL)
    response.raise_for_status()
    website_html = response.text

    # --- 2. Parsing the HTML ---
    soup = BeautifulSoup(website_html, "html.parser")

    # --- 3. Extracting and Cleaning Movie Titles ---
    # Find all h3 tags with the class "title", which contain the movie titles.
    all_movies = soup.find_all(name="h3", class_="title")

    # Extract the full text which includes the rank, e.g., "100) Stand By Me".
    movie_titles_with_rank = [movie.getText() for movie in all_movies]

    # Clean the titles by stripping the rank (e.g., "100) ") from the beginning.
    # We split each string at the first space and take the rest of it.
    movie_titles_clean = []
    for title in movie_titles_with_rank:
        # This handles different formats like "100) Title" or "12: Title".
        clean_title = title.split(" ", 1)[1]
        movie_titles_clean.append(clean_title)

    # The website lists movies from 100 down to 1. Reverse the list to get them in ascending order.
    movies = movie_titles_clean[::-1]

    # --- 4. Writing to a Text File ---
    # Open "movies.txt" in write mode with UTF-8 encoding for special characters.
    with open("movies.txt", mode="w", encoding="utf-8") as file:
        # Loop through the clean list, using enumerate to add the correct rank (1, 2, 3...).
        for index, movie in enumerate(movies, start=1):
            file.write(f"{index}) {movie}\n")

    print("Successfully generated movies.txt! 🎬")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
