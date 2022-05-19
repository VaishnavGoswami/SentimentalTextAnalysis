# SentimentalTextAnalysis
This is a program written in Python which performs sentimental analysis on a list of given blogs by performing web Scrapping and later processing that data to calculate Statistics and returns the information in the form of of a CSV File. 
It uses Loughran-McDonald MasterDictionary 1993-2021 as the parameter

## Extracting Derived variables
**Positive Score:** This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.

**Negative Score:** This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.

**Polarity Score:** This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula: 
Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
Range is from -1 to +1

**Subjectivity Score:** This is the score that determines if a given text is objective or subjective. It is calculated by using the formula: 
Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
Range is from 0 to +1

### Analysis of Readability
**Analysis of Readability is calculated using the Gunning Fox index formula described below.**
**Average Sentence Length** = the number of words / the number of sentences
**Percentage of Complex words** = the number of complex words / the number of words 
**Fog Index** = 0.4 * (Average Sentence Length + Percentage of Complex words)

### Average Number of Words Per Sentence
**The formula for calculating is:**
Average Number of Words Per Sentence = the total number of words / the total number of sentences

### Complex Word Count
Complex words are words in the text that contain more than two syllables.

### Word Count
We count the total cleaned words present in the text by 
1.	removing the stop words (using stopwords class of nltk package).
2.	removing any punctuations like ? ! , . from the word before counting.

### Syllable Count Per Word
We count the number of Syllables in each word of the text by counting the vowels present in each word. We also handle some exceptions like words ending with "es","ed" by not counting them as a syllable.

### Personal Pronouns
To calculate Personal Pronouns mentioned in the text, we use regex to find the counts of the words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken so that the country name US is not included in the list.

### Average Word Length
Average Word Length is calculated by the formula:
Sum of the total number of characters in each word/Total number of words
