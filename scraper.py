import requests 
import time 
from bs4 import BeautifulSoup
import random
import cloudscraper

url = 'https://www.soccer.com/srch?query=tiempos'
headers = [
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1'
]

def get_random_header():
    return {'random_header':random.choice(headers)}

try:
    headers = get_random_header()
    
    scraper = cloudscraper.create_scraper()
    html_text = scraper.get("https://www.soccer.com/srch?query=tiempos").text
    soup = BeautifulSoup(html_text, 'lxml')
    # Your scraping code here
    print(html_text)
except Exception as e:
    print(f"An error occurred: {str(e)}")

time.sleep(10)

