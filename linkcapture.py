from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import csv
import re


def ListofList(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)
      
    return(res)


# web scrapping the web sites for blog links 
headers = {'User-Agent': 'My User Agent 1.0',
        #''Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
    }
url = "https://blog.myntra.com/"

r  = requests.get(url, headers=headers)
data = r.text
soup = BeautifulSoup(data, "html.parser")
# print(soup)
# manually identify the tag which contains blog links and edit in find_all method below
links_data=soup.find_all("a", class_="full-link")
# Extract strings that contain link from tags
links = re.findall(r'"(.*?)(?<!\\)"', str(links_data))

#remove unwanted strings which are not links by adding them to "extras" lists also removes dupliates (if any)
final_links = []
extras = ['full-link', '_blank', 'full-link']
for i in links:
    if (i not in extras and i not in final_links):
        final_links.append(i)

#converting list to list of lists
final_links = ListofList(final_links)

# inserting index to the list
count = 1
for link in final_links:
    link.insert(0,count)
    count += 1


file = open('InputSheet.csv', 'a+', newline ='')
 
# writing the data into the CSV file
with file:   
    write = csv.writer(file)
    write.writerows(final_links)

file.close


