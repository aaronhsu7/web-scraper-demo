import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

with open('home.html', 'r') as html_file: 
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find('h5') 
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags: 
        print(course.text)

# Grabbing price example 
# class_ to relate to the HTML attribute rather than Python 
course_cards = soup.find_all('div', class_='card')

for course in course_cards: 
    course_name = course.h5.text # stores the text in each iteration
    course_price = course.a.text.split()[-1] # a tag stores the prices 

    print(f'{course_name} costs {course_price}')
