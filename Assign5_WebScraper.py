import requests
from bs4 import BeautifulSoup

#URL to search through
URL = 'https://www.jobindex.dk/jobsoegning/it'

#Variables for searching through pages other than the first 
# Only Applicable for Jobindex
pageIndexNumber = 2
pageIndex = '?page='

#Make a list to hold all the elements that 
listOfRelevantElements = []

#Getting the page
page = requests.get(URL)
 
#Soup-ify the page for further searching
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='results')
#print(results.prettify())

job_elements = results.find_all('div', class_='PaidJob')
for job_elemnent in job_elements:
    inner_element = job_elemnent.find('div', class_='PaidJob-inner')

    inner_element_text = str(inner_element.text.strip())
    #print(type(inner_element_text))

    if 'python'.lower() in inner_element_text.lower():
        print('contains "python"')


    #print(inner_element.text.strip())
    #print('\n')


#Find the max number of pages for the given seach URL in jobindex:
paging = soup.find(class_='jix_pagination')
page_elements = paging.find_all('a', class_='page-link')

#THIS variable specifically is that variable
maxPageNumber = int( page_elements[-1].text.strip())

while(pageIndexNumber <= maxPageNumber):
    print('page number: ' + str(pageIndexNumber))
    newPage = requests.get(URL + pageIndex + str(pageIndexNumber))
       
    

    #Soup-ify the page for further searching
    soup = BeautifulSoup(newPage.content, 'html.parser')

    results = soup.find(class_='results')
    #print(results.prettify())

    job_elements = results.find_all('div', class_='PaidJob')

    for job_elemnent in job_elements:
        inner_element = job_elemnent.find('div', class_='PaidJob-inner')


        inner_element_text = str(inner_element.text.strip())
        #print(type(inner_element_text))

        if 'python'.lower() in inner_element_text.lower():
            print('contains "python"')


    
    pageIndexNumber = pageIndexNumber + 1















