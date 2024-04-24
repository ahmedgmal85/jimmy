import re
from collections import Counter 

with open('random_paragraphs','r') as file:

 words = re.findall(r'\b\w+\b ', file.read()) 
stop_words = set(["the","and","or","but","to","of","a","an","in","on","for","with","as","by","at"])

words = [word for word in words if word.lower() not in stop_words] 

word_freq = Counter(words)
for word ,freq in word_freq.items():
   print(word + ":" + str(freq))