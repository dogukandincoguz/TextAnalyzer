import re
text = "world earth"
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
           if i in longestWords:                      # In this if loop, i blocked words being duplicate
              pass
           else:
              longestWords[i] = frequency_calculator(i)
        else:
            continue
    sorted(longestWords.items(), key = lambda x: x[1], reverse = True)

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
    sorted(shortestWords.items(), key = lambda x: x[1], reverse = True)