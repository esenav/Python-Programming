from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request, nltk, string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

"""
 Implemented for Python 3.5 by 1402039 and 1403713
 Beautiful Soup will be used for pulling data out of Websites files
 NLTK is also imported in order to tokenise output and process POS Tagging
 In addition, NLTK is used for implementing the stopwords which is imported from the nltk.corpus
 In order to create the steming analysis, PorterStemmer is imported from nltk.stem
"""

def main():
    with open("Websites.txt") as file:
        for line in file:
            start(line)
        file.close()
        
def htmlTags(element):
    # Elements in the HTML tags to filter in the 'noHTMLtags' function
    if element.parent.name in ['html','style', 'body', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

# The HTML tags will be parsed so the text could be analysed
def noHTMLtags(body):
    soup = BeautifulSoup(body, 'html.parser')
    content = soup.findAll(text=True)
    # Filters HTML tags from the Content
    visibleContent = filter(htmlTags, content)
    # The output will be displayed with no HTML tags
    return " ".join(i.strip() for i in visibleContent)

def start(line):
    # The following opens the URL link and reads the content
    htmlOutput = urllib.request.urlopen(line).read().decode('utf-8')
    # The function 'noHTMLtags' enable 'htmlOutput' to be displayed with clear text
    outputToTokenize = noHTMLtags(htmlOutput)
    print("Starting to process website: "+line)
    # Function .maketrans, makes a transitional table, that .translate uses to remove punctuation with white spaces
    remove= str.maketrans(string.punctuation, ' '*len(string.punctuation))
    # Removes punctuation in website address to be used as a file name
    name = line.translate(remove).replace(' ', '_').rstrip()
    filename = name+"_Results.txt"
    # Naming variables global is used that other def() can use variable in their run
    global result
    # Opening file with website as a name, "w+" tells python to create that file if it does not exists
    result = open(filename, "w+")
    pre_processing(outputToTokenize)

def pre_processing(outputToTokenize):
    # The stopwords is set to English
    stopWords = set(stopwords.words('english'))
    # Removal of punctuations in the website text
    remove= str.maketrans(string.punctuation, ' '*len(string.punctuation))
    final_output = outputToTokenize.translate(remove)
    tokens = word_tokenize(final_output)
    # Ensures that the, non-alpha are deleted from the tokens
    newnew = list(filter(lambda a:a.isalpha(), tokens))
    # map lets us lower case entire list without iteration
    newmap = map(str.lower, newnew)
    global newnew2
    # Ensures that the, non-stop words are deleted from the tokens
    newnew2 = list(filter(lambda b:b not in stopWords, newmap))
    result.write("Pre-Processing Stage\n"+"Number of items in a list: "+str(len(newnew2))+"\n")
    result.write(str(newnew2)+"\n\n")
    print("Stage 1 completed")
    speech_Tag(tokens)

def speech_Tag(tokens):
    # Using NLTK we Tag, on non processed tokens
    tags = nltk.pos_tag(tokens)
    # Frequency of tags
    tags_fd = nltk.FreqDist(tag for(word,tag)in tags)
    tag_fd = nltk.FreqDist(tags)
    # Sorts the most common words
    comm_tags = tags_fd.most_common()
    most_comm = tag_fd.most_common()
    result.write("Speech Tags\n")
    result.write(str(tags)+"\n\n")
    print("Stage 2 completed")
    keyWords(most_comm, comm_tags)
    
def keyWords(most_comm, comm_tags):
    # Sorts out the most common words based on the tags
    sort_most = [wt[0] for(wt, _) in most_comm if wt[1]==comm_tags[0][0]]
    sort_most2 = [wt[0] for(wt, _)in most_comm if wt[1]==comm_tags[1][0]]
    mostCommWords = map(str.lower ,sort_most[:4])
    #Common word removal ### NOTE: This sometimes does not work if you have print statement before the 2 for loops
    for words in mostCommWords:
        for a in newnew2:
            if words==a:
               newnew2.remove(a)
    result.write("Selecting Keywords\n"+"Number of items in a list: "+str(len(newnew2))+"\n")
    result.write(str(newnew2)+"\n\n")
    print("Stage 3 completed")
    stemming()

def stemming():
    # Using PorterStemmer
    stems = PorterStemmer()
    stem_list = []
    # set is used on the list to eliminate duplicate values == no duplicate stems
    for keys in set(newnew2):
         a = stems.stem(keys)
         stem_list.append(a)
    result.write("Stemming Process\n")
    result.write(str(stem_list)+"\n")
    result.close()
    print("Stage 4 completed",'\n')
        
main()
