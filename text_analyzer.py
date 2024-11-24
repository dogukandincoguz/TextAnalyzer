from sys import argv
import re
import locale
import os


locale.setlocale(locale.LC_ALL, "en_US")

os.linesep = "\n"

txt = open(argv[1], "r")
text = txt.read().lower()


#2.1
def count_total_words():
    allWords = re.findall(r"[\w'-]+", text)  #finds all words including " ' " and " - " by not splitting them.
    allWords = [word[:-1] if word.endswith("'") else word for word in allWords]
    return len(allWords)


def word_occurence(word):
    allWords = re.findall(r"[\w'-]+", text)
    allWords = [w[:-1] if w.endswith("'") else w for w in allWords]
    word_count = {}                               #  Using dictionary for word occurence per word.
    for i in allWords:
        if i in word_count:             # If loop for adding and counting words.
            word_count[i] += 1
        else:
            word_count[i] = 1
    return word_count[word]




#2.2
def count_sentences():
    sentences = re.split(r"\.\.\.|[.!?]", text) #finds all sentences by splitting from "...","!","?" or "."
    total_sentences = len(sentences)-1
    return total_sentences



#2.3
def word_per_sentence():
    if count_sentences() != 0 :
        wordPerSentence = count_total_words()/count_sentences()
        wordPerSentence = round(wordPerSentence , 2)
        return wordPerSentence
    return -1

#2.4
def total_characters():
    totalCharacters = len(text)
    return totalCharacters

#2.5
def total_characters2():
    allWords = re.findall(r"[\w'-]+", text)
    allWords = [word[:-1] if word.endswith("'") else word for word in allWords]
    cleanText = "".join(allWords)
    exceptionalTotalCharacters = len(cleanText)
    return exceptionalTotalCharacters

#2.7
def frequency_calculator(word):
    frequency = word_occurence(word)/count_total_words()
    frequency = round(frequency, 4)
    return frequency


def frequency_table():
    allWords = re.findall(r"[\w'-]+", text)
    allWords = [w[:-1] if w.endswith("'") else w for w in allWords]
    wordsbyFrequency = {}
    for j in allWords:
        wordsbyFrequency[j]= frequency_calculator(j)
    wordsbyFrequency = dict(sorted(wordsbyFrequency.items(), key = lambda x: (-x[1], x[0]))) # This line compares frequency and sorting them by descending order. If  frequencies are equal, it looks their alphabetical order.
    return wordsbyFrequency

#2.6
def longest_word():
    allWords = re.findall(r"[\w'-]+", text)
    allWords = [w[:-1] if w.endswith("'") else w for w in allWords]
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
    longestWords = dict(sorted(longestWords.items(), key = lambda x: (-x[1], x[0]))) # Same as wordsbyfrequency dict.
    return longestWords

def shortest_word():                                      # Doing same thing at longest_word() func.
    allWords = re.findall(r"[\w'-]+", text)
    allWords = [w[:-1] if w.endswith("'") else w for w in allWords]
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
    return shortestWords

if __name__ == "__main__":
    txt = open(argv[1], "r")
    text = txt.read().lower()
    txt.close()
    output_txt = open(argv[2], "w")
    #Statistics
    output_txt.write("Statistics about {:7s}:\n".format(argv[1]))
    output_txt.write("{:24s}: {}\n".format("#Words",count_total_words()))
    output_txt.write("{:24s}: {}\n".format("#Sentences",count_sentences()))
    output_txt.write("{:24s}: {:.2f}\n".format("#Words/#Sentences",word_per_sentence()))
    output_txt.write("{:24s}: {}\n".format("#Characters",total_characters()))
    output_txt.write("#Characters (Just Words): {}\n".format(total_characters2()))
    #Shortest Word
    if len(shortest_word()) == 1:
       for (word,freq) in shortest_word().items():
            output_txt.write("{:24s}: {:25}({:.4f})\n".format("The Shortest Word",word,freq))
    else:
        output_txt.write("{:24s}:\n".format("The Shortest Words"))
        for (word, freq) in shortest_word().items():
            output_txt.write("{:24s} ({:.4f})\n".format(word, freq))

    #Longest Word
    if len(longest_word()) == 1 :
        for (word,freq) in longest_word().items():
            output_txt.write("{:24s}: {:25}({:.4f})\n".format("The Longest Word", word, freq))
    else:
        output_txt.write("{:24s}:\n".format("The Longest Words"))
        for (word, freq) in longest_word().items():
            output_txt.write("{:24s} ({:.4f})\n".format(word, freq))

    #All Words and freq
    output_txt.write("{:24s}:\n".format("Words and Frequencies"))
    freqList = list(frequency_table().items())
    for i,(l,n) in enumerate(freqList):
        if i ==len(freqList) - 1 :                                       # My code was adding space at last of output, so i did this to prevent it.
            output_txt.write("{:24s}: {:.4f}".format(l,n))
        else:
            output_txt.write("{:24s}: {:.4f}\n".format(l,n))
    output_txt.close()
