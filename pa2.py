from sys import argv
import re
import locale


locale.setlocale(locale.LC_ALL, "en_US")

txt = open(argv[1], "r")
text = txt.read().lower()


#2.1
def count_total_words():
    allWords = re.findall(r"[\w'-]+", text)  #finds all words including " ' " and " - " by not splitting them.
    return len(allWords)


def word_occuring(word):
    allWords = re.findall(r"[\w'-]+", text)
    word_count = {}                               #  Using dictionary for word occurence per word.
    for i in allWords:
        if i in word_count:                       # If loop for adding and counting words.
            word_count[i] += 1
        else:
            word_count[i] = 1
    return word_count[word]




#2.2
def count_sentences():
    sentences = re.split(r"\.\.\.|[.!?]", text) #finds all sentences by splitting from "...","!","?" or "."
    total_sentences = len(sentences)
    return total_sentences



#2.3
def word_per_sentence():
    wordPerSentence = count_total_words()/count_sentences()

    wordPerSentence = "%.2f" % wordPerSentence
    return wordPerSentence

#2.4
def total_characters():
    totalCharacters = len(text)
    return totalCharacters

#2.5
def total_characters2():
    cleanText = re.sub(r"[^\w'-]+", "",text) #Cleaning text from whitespaces and punctuations without touching in-word punctuations
    exceptionalTotalCharacters = len(cleanText)
    return exceptionalTotalCharacters

#2.7
def frequency_calculator(word):
    frequency = word_occuring(word)/count_total_words()
    frequency = "%.4f" % frequency
    return frequency

#2.6
def longest_word():
    allWords = re.findall(r"[\w'-]+", text)
    maxLength = len(max(allWords, key = len))           # Finding longest word's letter length
    longestWords = {}                                 # Using dict. to do print more basic
    for i in sorted(allWords, key = len):
        if len(i) == maxLength:
           if i in longestWords:                      # In this if loop, i blocked words being duplicated in dict.
              pass
           else:
              longestWords[i] = frequency_calculator(i)
        else:
            continue
    longestWords = dict(sorted(longestWords.items(), key = lambda x: (-x[1], x[0]))) # This line compares frequency and sorting them by descending order. If  frequencies are equal, it looks their alphabetical order.

def shortest_word():                                      # Doing same thing at longest_word() func.
    allWords = re.findall(r"[\w'-]+", text)
    minLength = len(min(allWords, key = len))
    shortestWords = {}
    for k in sorted(allWords, key = len):
        if len(k) == minLength:
            if k in shortestWords:
                pass
            else:
                shortestWords[k] = frequency_calculator(k)
        else:
            continue
    shortestWords = dict(sorted(shortestWords.items(), key = lambda x: (-x[1],x[0])))
