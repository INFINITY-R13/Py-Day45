# Top 100 Movies Web Scraper 🎬

This project contains a Python script that scrapes the "100 Best Movies of All Time" from an archived version of an Empire Online article. It uses the `requests` library to fetch the webpage and `BeautifulSoup` to parse the HTML, extracting the movie titles. The final list is then saved into a `movies.txt` file, numbered in ascending order.

-----

## Project Overview

The primary goal of this script is to demonstrate a simple yet practical web scraping task. It shows how to:

  - **Fetch** web content from a specific URL.
  - **Parse** HTML to locate and extract relevant data.
  - **Process** and clean the extracted data.
  - **Write** the final, formatted data to a local text file.

-----

## Prerequisites

Before you can run the script, you need to have **Python** installed on your system. You will also need the following Python libraries:

  - `requests`: For making HTTP requests to get the webpage.
  - `beautifulsoup4`: For parsing the HTML content.

-----

## Installation & Setup

1.  Clone the repository or download the files to your local machine.

2.  Install the required libraries using `pip`. You can do this by running the following command in your terminal:

    ```bash
    pip install requests beautifulsoup4
    ```

-----

## How to Run the Script

Once you have installed the prerequisites, you can run the scraper by executing the `main.py` file:

```bash
python main.py
```

After the script finishes, you will find a new file named `movies.txt` in the same directory, containing the list of the top 100 movies.

-----

## Output Sample

The generated `movies.txt` file will be formatted as follows:

```
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
5) Pulp Fiction
... and so on
```

-----

## ⚠️ A Note on the URL

To ensure the scraper works consistently, it uses a cached version of the website from the Internet Archive's Wayback Machine. This is because the live version of the Empire Online article may have changed its HTML structure since the script was originally written.

**URL Used:** `https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/`