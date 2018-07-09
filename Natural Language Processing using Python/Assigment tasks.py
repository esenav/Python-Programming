import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk import pos_tag, ngrams
from urllib import request
from bs4 import BeautifulSoup
import re


def Task_1():
    text = """A Message From The Headmaster
    Kow tow!
    That’s the Chinese for “hello”, as I’ve learnt this week, because those were the first words said to me by
    the Head of our Chinese sister academy, the Tiananmen Not At All Free School.
    As you’ve probably gathered, we were rolling out the school “red”(!) carpet this week for Mr Xi Sho-pping,
    who was on a visit to try and buy as much of the school as we could sell him.
    ...
    Mr Sho-pping then visited the old boiler room and we signed an agreement for him to build not only a new
    nuclear boiler to replace it, but to build another two boilers, just in case the other one blows up, which
    it won’t of course. Even better, all the boilers will be run entirely by himself and members of the Beijing
    Nuclear Intelligence Services Department, who are delighted to be the given the chance of experimenting
    with untried nuclear technology in someone else’s school. How exciting is that! I can’t have been the only
    one to feel a warm glow at the thought of so much radioactivity at the very heart of the school. Who
    knows, by this time next year I could be the Two-head-master! (Finkelstein, D., you’re on fire – as is the
    boiler room!)
    D.C"""

    text_tokenized = word_tokenize(text)
    print(text_tokenized)
    post_tag = pos_tag(text_tokenized)
    print(post_tag)
    

#Task_1()

def Task_2():
    url = "http://www.bbc.co.uk/news/business-41779341"
    html = request.urlopen(url).read().decode('utf8')
    raw_text = BeautifulSoup(html, "html5lib").get_text()
    tokens = word_tokenize(raw_text)
    #tokens = tokens[11707:12431] # Correct text tokens with some noise for different URLs needs to identify different tokens.
    tokens1 = tokens[11707:11806]
    tokens2 = tokens[11841:12431]
    complete_text = tokens1+tokens2
    text = nltk.Text(complete_text)
    #print(text.concordance('$'))
    test_list = ["50bn", "euro", "£50,000", "£117.3m", "30p", "500m","euro ", "338bn", "euros", "$15bn", "$92.88"]
    final_REP = [w for w in test_list if re.search('^(£|\$|euro)|([0-9])+(\.|[0-9,9])+(p|bn|m)$', w)] # Regular exp FINAL finds everything what is asked
    find_bn_ending = [w for w in complete_text if re.search('^([0-9])+(\.|[0-9,9])+(p|bn|m|euro.)$', w)] # Finding amount tokens NOT USED IN PROGRAM
    print("Showing test for Regular expression")
    print(test_list)
    find_number = [w for w in complete_text if re.findall('^[0-9]+(\.|[0-9,9])+(p|bn|m|euro)$', w)] # Finding amount tokens that are used in program
    find_full_token = [w for w in complete_text if re.search('^(£|\$)+([0-9])+(\.|[0-9,9])+(p|bn|m|euro.)$', w)]  # Finding full possible tokens                
    find_currency = [w for w in text if re.findall('\$$', w)]  # finding all $ sign in tokens
    #print(html[92003:97000])# Full text with noise
    #print(html[92003:92570]) # First part
    #print(html[93150:94750])  # Second part
    #print(html[95200:97005])   # Third part
    print("")
    tr = []
    try:
        if len(find_currency) == len(find_number):
            print("Lists compared and bined\n")
            tr = [x+y for x, y in zip(find_currency, find_number)] # Joins tokens in a loop from two different lists
        else:
            print("Comparing both tokens of currency and amount,\nthere is not equal amounts of them and we cannot merge lists for completed tokens\noutput might not be complete")
    except:
        print("Comparing both tokens of currency and amount,\nthere is not equal amounts of them and we cannot merge lists for completed tokens\noutput might not be complete")
           
    final_list = tr + find_full_token
    
    if tr == 0 :
        final_list = find_full_token
    else:
        for s in final_list:
            if(s[:1]=="$"):
                currency = "Dollars"
            elif(s[:1]=="£"):
                currency = "Pounds"
            else:
                currency = s[:1]
                
            print("Found a match!")
            print("Currency: ",currency)
            print("Amount: ", str(s[1:]))
            print(" ")
  




def Task_3():
    print("Hello. Please ask me about flights in Europe.")

    while True:
        user = input().lower()
        response = re.sub('^goodbye$', 'Goodbye!', user)
        if response != user:
            print(response)
            return
        response = re.sub('^yes$', 'Okey', response)
        response = re.sub('^no$','What is wrong?', response)
#tested 'i want to 'user input' ? '       
        response = re.sub('^i want to ([a-z\' ]+)$', r'What date do you want \1?',response)
#tested 'tell me about 'whatever user inputs' '
        response = re.sub('^tell me about ([a-z\' ]+)$',r'Sorry \1 have no information, about that', response)
#tested 'next available flights to 'destination' '
        response = re.sub('^([a-z]+) available flights to ([a-z]+)$', r'There is no information about flights to \2, sorry try different destination.', response)
#tested 'what about flights to paris on april 2?' MUST END WITH ? MARK  
        response = re.sub('^(how|what) about to ([a-z]+) on ([a-z]+) ([0-31]+(st|nd|th))\?$', r'Sorry, all flights to \2 on \3 \4 were canceled, try different AirLine.', response)
#tested 'can we book it for april to berlin?' MUST END WITH ? MARK  
        response = re.sub('^can we book it for ([a-z]+) to ([a-z]+)\?$', r'Apology, but this system does not support booking, please refer to out website', response)
        response = re.sub('^what good are you for', r'I am a simple robot, now please go away', response)
#tested 'what would be the first available flight to Paris next year?' MUST END WITH ? MARK 
        response = re.sub('^what would be the first ([a-z\' ]+)\?$',r'There are no \1. Please accept our apologies', response)
        
        if response == user:
            response = re.sub('.*','Sorry invalid statement.', response)
            
        print(response)
    

exlist = [None, Task_1, Task_2, Task_3]
running = True
while running:
    line = input("Select exercise (0 to quit): ")
    if line == "0":
        running = False
    elif len(line) == 1 and "1" <= line <= "8":
        exlist[int(line)]()
    else:
        print("Invalid input - try again")

    
