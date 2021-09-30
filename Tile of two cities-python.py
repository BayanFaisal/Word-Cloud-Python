# We use the text of the famous novel by Charles Dickens, A Tale of Two Cities. Credit to Project Gutenberg. 
# We want to read and clean the input, then count the frequencies of each word.

from collections import Counter

file=open('98-0.txt', encoding="utf8")


# We want to use stopwords file <--- common words to exclude. Credit to Andreas Mueller

stopwords = set(line.strip() for line in open('stopwords'))


# We create our data structure here.

wordcount = {}

# We instantiate a dictionary, replace punctuation , and add every word in the file to the dictionary.

for word in file.read().lower().split():
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace("\"", "")
    word = word.replace("“", "")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1 


# We want to count of each words present in wordcount, and sort it.


d = collections.Counter(wordcount)

# We want to extract the top ten most frequently occurring words from our data structure, and print them.

for word, count in d.most_common(10):
    print(word, ":", count)