#https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
#print(results.prettify())


job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    #print(title_element.text)
    #print(company_element.text)
    #print(location_element.text)
    #print("\n"*2)
    #print(job_element, end="\n"*2)

python_jobs = results.find_all("h2", string=lambda  text: "python" in text.lower())

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]


split_urls = []
useful_urls = []

for python_element in python_job_elements:
    title_python = python_element.find("h2", class_="title")
    company_python = python_element.find("h3", class_="company")
    location_python = python_element.find("p", class_="location")
    #print(title_python.text)
    #print(company_python.text)
    #print(location_python.text)
    #print("\n"*2)


    links = python_element.find_all("a")
    for link in links:
        link_url = link["href"]     

        split_urls.append(link_url)
  
useful_urls = split_urls[1::2]
for url in useful_urls:
    print(url + "\n")