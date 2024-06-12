from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
html_text = requests.get('').text # URL to webscrape (.text -> HTML)
#print(html_text) -> Response(200) means the request is done, or HTML
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='"class_name')
for job in jobs:
    company_name = job.find('h3',class_='class_name').text.replace(' ', ' ') # Removes
    published_date = job.find('span', class_='class_name').span.text
    skills = job.find('span', class_='class_name').text.replace(' ',' ')
    more_info = job.header.h2.a['href']
    if unfamiliar_skill not in skills:
        print(f'''
        Company Name: {company_name.strip()} # removes leading/trailing whitespaces
        Required Skills: {skills}
        ''')

# with open(f'posts/{index}.txt', 'w') as f:
#     f.write...

# Required Skills: 
# pythonscripting,xml,pl/sql,python,openerp

if __name__ == '__main__':
    while True: 
        time_wait = 10
        time.sleep(time_wait * 60) # runs every 10 minutes

