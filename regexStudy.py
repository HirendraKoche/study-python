import re
from collections import Counter


# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
pattern = r'\b\w+\b'
words = re.findall(pattern, paragraph)
wordsCounter = Counter(words)
mostCommonWords = wordsCounter.most_common()
#print(mostCommonWords)

def isValidVariable(str_s):
    pattern = r'^[a-z]+[-|_]?[a-z0-9]+'
    if re.fullmatch(pattern, str_s) is None:
        return False
    else:
        return True

# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


pattern = r'[%$@&;.!?,#]'

clean_text = re.sub(pattern, '', sentence)

def mostFrequentWords(str_s):
    pat = r'\b\w+\b'
    words = re.findall(pat, str_s.lower())

    wordCounter = Counter(words)
    return wordCounter.most_common()

print(mostFrequentWords(clean_text))