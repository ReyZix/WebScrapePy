import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

# URL of the website you want to scrape
url = 'http://quotes.toscrape.com/'

try:
    # Use a session object to persist parameters across requests
    with requests.Session() as session:
        response = session.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extracting all quotes from the webpage
            quotes = soup.find_all('div', class_='quote')

            for quote in quotes:
                text = quote.find('span', class_='text').get_text()
                author = quote.find('small', class_='author').get_text()
                tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
                print(f'Quote: {text}\nAuthor: {author}\nTags: {", ".join(tags)}\n')
        else:
            print(f"Failed to retrieve the webpage: {response.status_code}")

except RequestException as e:
    print(f"An error occurred: {e}")
