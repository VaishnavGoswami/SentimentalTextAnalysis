import copyreg
from bs4 import BeautifulSoup
from numpy import size # this module helps in web scrapping.
import requests  # this module helps us to download a web page
from csv import writer
import csv
import re


def ListofList(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)
      
    return(res)

headers = {'User-Agent': 'My User Agent 1.0',
        #''Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
    }
url = "https://blog.myntra.com/"

r  = requests.get(url, headers=headers)
data = r.text
soup = BeautifulSoup(data, "html.parser")
# print(soup)
links_data=soup.find_all("a", class_="full-link")
# print (type(links_data))
links = re.findall(r'"(.*?)(?<!\\)"', str(links_data))
# print(type(links))
final_links = []
extras = ['full-link', '_blank', 'full-link']
for i in links:
    if (i not in extras):
        final_links.append(i)

#converting list to list of lists
final_links = ListofList(final_links)

# inserting index to the list
count = 1
for link in final_links:
    link.insert(0,count)
    count += 1

# file = open("InputSheet.csv", "w", newline= "")
# header = ['URL_ID', 'URL']
# writer = csv.writer(file, fieldnames = header)

# for w in range(len(final_links)) :
#   writer.writerow([w+1, final_links[w]])

# file.close()

file = open('InputSheet.csv', 'a+', newline ='')
 
# writing the data into the file
with file:   
    write = csv.writer(file)
    write.writerows(final_links)

file.close


# https://blog.myntra.com/rubans-a-story-of-sheer-grit-and-perseverance/