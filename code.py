from bs4 import BeautifulSoup # this module helps in web scrapping.
from csv import writer
import requests  # this module helps us to download a web page
import pandas as pd
import re
import csv

def Analyse(url):
    

    headers = {
        'User-Agent': 'My User Agent 1.0',
        #''Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
    }
    #url = "https://insights.blackcoffer.com/how-does-ai-help-to-monitor-retail-shelf-watches/"

    r  = requests.get(url, headers=headers)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    paragraph=soup.find_all('p')
    heading=soup.find_all('h1')
    para = heading +paragraph
    para= remove_html_tags(para)

    Totalsentences= SentenceCount(para) #count total sentences
    #print(Totalsentences)

    para = para.replace(".","")
    para = para.replace("?","")
    para = para.replace(",","")
    para = para.replace("-","")
    para = para.replace(":","")
    para = para.replace("(","")
    para = para.replace(")","")
    para = para.replace("[","")
    para = para.replace("]","")

    # Split on spaces
    para = para.split(' ')


    words=remove_stopwords(para, stopwords)

    word_count= len(words)
    complex_count, syllables= complex_Words_count(words)
    syllables_per_word = round(syllables/word_count)
    Personal_Pronouns_count = Personal_Pronouns(words)
    avg_word_len = round(word_len(words)/ word_count)

    #converting all words to upper case
    words_in_uppercase = Upper_case(words)

    Positive_score = P_score(words_in_uppercase)
    Negative_score = N_score(words_in_uppercase)
    Subjectivity = (Positive_score + Negative_score)/ (word_count + 0.000001)
    Polarity = (Positive_score - Negative_score)/ ((Positive_score + Negative_score) + 0.000001)



    Avg_len_sentences = word_count/Totalsentences
    percentage_of_complex_no = 100*(complex_count/word_count)
    Fog_index = (0.4*( Avg_len_sentences + percentage_of_complex_no))

    new_row = []
    new_row.extend((Url_id,url, Positive_score, Negative_score, Polarity, Subjectivity,
     Avg_len_sentences, percentage_of_complex_no, Fog_index,Avg_len_sentences,complex_count,word_count,
     syllables_per_word, Personal_Pronouns_count, avg_word_len))
    return new_row

def Flattened_list(two_D_list):
    one_D_list= []  
    for element in two_D_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                one_D_list.append(item)
        else:
            one_D_list.append(element)
    return one_D_list

def SentenceCount(text):
    count=0
    for i in text:
        if i == "." or i=="?":
            count +=1
    return count

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', str(text))

def remove_stopwords(a, b):
    for i in a[:]:
        if i in b:
            a.remove(i)
    return a

def remove_empty(text): #removing empty values from the list
    while("" in text) :
        text.remove("")
    return text

def complex_Words_count(text):
    complex_count=0
    syllables = 0
    counter=0
    for words in text:
        #syllables += counter
        counter=0
        i="^" # "i" is initialized as some random symbol
        for j in words:

            if not(i=='e' and (j=='s' or j=='d')):
                if j in vowels:
                    counter +=1
            if i=='e' and (j=='s' or j=='d'):
                counter -= 1
            #print(counter)
            i=j
        syllables += counter

        if counter > 2:
            complex_count+=1    
    return complex_count, syllables;  

def N_score(text):
    Score_counter=0
    for words in text:
        if words in Negative_words:
            Score_counter += 1
    return Score_counter
    

def P_score(text):

    Score_counter= 0
    for words in text:
        if words in Positive_words:
            Score_counter += 1
    return Score_counter

def word_len(text):
    counter = 0
    for word in text:
        for characters in word:
            counter += 1
    return counter


def Upper_case(text):
    new_text = [x.upper() for x in text]
    return new_text

def Personal_Pronouns(text):
    counter = 0
    for words in text:
        if words in Personal_Pronouns_list:
            counter += 1
    return counter


#useful lists
Personal_Pronouns_list = ['I','We','My','Ours','Us','i','we','my','ours','us']
vowels= ['a','e','i','o','u']

with open('StopWords.csv', newline='') as f:
    reader = csv.reader(f)
    stopwords2d = list(reader)

stopwords = Flattened_list(stopwords2d)

#importing list of positive words
with open('Positive_words1.csv', newline='') as f:
    reader = csv.reader(f)
    Positive_words2d = list(reader)

Positive_words = Flattened_list(Positive_words2d)
Positive_words = remove_empty(Positive_words)

#importing list of negative words
with open('Negative_words.csv', newline='') as f:
    reader = csv.reader(f)
    Negative_words2d = list(reader)

Negative_words = Flattened_list(Negative_words2d)

#importing input url file
path = "InputSheet.csv"
df=pd.read_csv(path)


Url_id = 0
for url in df.URL:
    Url_id += 1
    new_row = Analyse(url)
    with open('Output Data Structure.xlsx - Sheet1.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(new_row)  
        f_object.close()