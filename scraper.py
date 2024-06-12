import requests 
import time 
from bs4 import BeautifulSoup

url = 'https://www.soccer.com/srch?query=tiempos'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_text = requests.get('https://www.soccer.com/srch?query=tiempos').text 
        soup = BeautifulSoup(html_text, 'lxml')
        # Your scraping code here
        print(response.text)
    else:
        print(f"Received status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Delay of 3 seconds
time.sleep(3)