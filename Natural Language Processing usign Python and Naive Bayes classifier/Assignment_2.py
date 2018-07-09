from collections import Counter
import pandas
import operator
import functools

#Evaldas Senavaitis 1402039

# IGNORE MOST OF THE PRINT COMMENTS

#print("Input vocabulary file: ")
#user1 = input()
vocab_file = open("SampleTrain.vocab.txt","r")
#vocab_data = vocab_file.read()
list_vocab = []
for line in vocab_file.readlines():
    list_vocab.append(line.rstrip())   
#list_vocab.append(vocab_data.split('\n'))
#print(list_vocab)
#print("Input training document file: ")
#user2 = input()
training_file = open("SampleTrain.txt", "r")
data = training_file.read()
#print(data)
count = len(data.split('\n'))-1 # knowing how many documents are in corpus
#print(count) 
correct = data.replace('\t', ' ').strip() # can be used to know how many documents are in corpus
#print(correct)
count_training = len(correct.split('\n'))
list1 = []
list2 = []
train_class = []
list1.append(correct.split('\n'))
for word in list1:
    countfinal = 0
    for element in word:
        count1 = len(element[5:].split()) # **
        somelist = element[5:].split()
        #print(count1) # knowing how many words are per each document
        countfinal = countfinal + count1 # counting total words in training corpus
        list2 = list2+somelist # all words in training corpus
        c = element[3:5].split()
        train_class = train_class + c
        count_training_c = list(Counter(train_class).values())

#print(countfinal)
#print(count_training_c)
bool_list = []
for vocab_word in list_vocab: # checking vocab words with training corpus
    #print(vocab_word)
    for list1_word in list2:
        booleans = Counter(vocab_word) == Counter(list1_word)
        bool_list.append(booleans)
x=sum(bool_list)
#print(x)
#print(bool_list)
#print(countfinal == x) # checking if word count is the same as number of True statements when comparing vocabulary with training or testing data

#print("Input Test document file: ")
#user3 = input()
test_file = open("sampleTest.txt", "r")
test_data = test_file.read()
test_correct = test_data.replace('\t', ' ').strip()
#print(test_correct)
count2 = len(test_correct.split('\n')) # number used for prior probability Ndoc
test_list = []
test_class = []
test_doc = []
test_list.append(test_correct.split('\n'))
#print(test_list)
for c in test_list:
    count_zero = 0
    for c_element in c:
        cl=c_element[3:5].split()
        test_class = test_class + cl
        count_classes = list(Counter(test_class).values()) # counts unique elements in a list, values shown are times, unique element occured in a list.
                                                    # Ex: [3, 3] means that element one occured 3 times in a list, and element 2 occured 3 times in a list as well
        c0=c_element[:3]
        test_doc.append(c0)
#print(test_doc)
#print("Number of how many times class occurs in a document corpus - ",count_classes)
class_numbers = test_class[0:len(count_classes)]
#print("Class numbers in test document: " ,class_numbers) # class_number[0-1] to access class numbers
#print("Prints the class amounts in a test document: ",Counter(test_class))
if len(count_classes) > 2:
    print("ADD ADDITIONAL LISTS TO THE CODE, AS MORE THAN 2 CLASSES WERE DETECTED IN A TEST FILE !!!")

# Counting prior probability for the test classes # Can be used for Training corpus as well with few changes
#print("Prior probabilities in test document:")
prob_c = count_classes[0]/count2 
#print("Prior probability of class 0 - ", prob_c)
prob_c1 = count_classes[1]/count2
#print("Prior probability of class 1 - ", prob_c1)
print("Prior probabilities:")
train_dict = Counter(train_class)
prior_dict = {}
for x, z in train_dict.items():
    prior = z/count_training
    prior_dict.update({x:prior})
    print("class ", x, " = ",prior)

# Counting likelyhood with smoothing
c_n = int(class_numbers[0]) # for class at first position
list_class_0 = []
list_class_1 = []
list_c = []
for text in test_list:
    count_w = 0
    count_v = 0
    for element in text:
        
        com = int(element[3:5])
        list_c.append(com)
        #print(com)
        #print(element[5:])
        if com == c_n: # if statement makes for loop initiate as many times as if statement is true
            count_0 = len(element[5:].split())
            count_w = count_w+count_0       #counting words that are in class 0
            #print(element[5:])# words belonging to class 0
            somelist2 = element[5:].split()
            list_class_0 = list_class_0+somelist2
#            for vocab_word in test_list: # checking vocab words with training corpus # loops 3 times
 #               #print(vocab_word)
  #              for compare in vocab_word: # loops 3 times
   #                 print("")
                    #somelist2 = element[5:].split()
                    #list_class_0 = list_class_0+somelist2
        if com != c_n:
            count_1 = len(element[5:].split())
            count_v = count_v+count_1       # counting words that are in class 1
            #print(element[5:]) # words belonging to class 1
            somelist2 = element[5:].split()
            list_class_1 = list_class_1+somelist2
            
#print("List of words belonging to class 0", list_class_0)
#print("List of words belonging to class 1", list_class_1)
dict_counter = Counter(list_class_0) # counts how many times word occured in a list
dict_counter2 = Counter(list_class_1)
pos_laplace = []
class_0 = ["class = 0"]
class_1 = ["class = 1"]
print("      ")
print("Feature likelihoods")
pos_dict = {}
neg_dict = {}
for q, w in dict_counter.items():  
    #print(y/len(list_class_1))
    laplace = w+1
    pos_laplace.append(laplace) 
    prob_wi_c = laplace / (len(list_class_0)+abs(len(list_vocab))) # Counting class 0 likelihood with smoothing
    #print(q + ('\n'), prob_wi_c, end=" ")
    pos_dict.update({q:prob_wi_c})
    
pr = pandas.DataFrame(pos_dict,class_0, pos_dict.keys() )
print(pr)
#print(pos_laplace)
final_pos = functools.reduce(operator.mul, pos_laplace, 1)
#print(final_pos)

#print(dict_counter2)
neg_laplace = []
for i, y in dict_counter2.items():  # printing how many times words occured in a test corpus (for loop)
    #print(y/len(list_class_1))
    laplace = y+1
    neg_laplace.append(laplace)
    prob_wi_c = (y+1)/(len(list_class_1)+abs(len(list_vocab)))
    #print(i, prob_wi_c)
    neg_dict.update({i:prob_wi_c})
final_neg = functools.reduce(operator.mul, neg_laplace, 1)
pd = pandas.DataFrame(neg_dict,class_1, neg_dict.keys() )
print(pd)
print('\n')
print("Predictions on test data")
#print(count_w) # 5 word count
#print(count_v) # 7 word count

lst = []
lst2 = []
for texts in list1:
    count_p = 0
    count_n = 0
    for element in texts:
        com = int(element[3:5])
        if com == c_n:
            words = element[5:].split()
            lst = lst + words
        if com != c_n:
            words = element[5:].split()
            lst2 = lst2 + words
#print(Counter(lst))
#print(Counter(lst2))
list5 = []
for a in test_list:
    count_zero = 0
    for c_element in a:
        cl=c_element[3:5].split()
        somelist = c_element[5:].split()
        #print(somelist)
        templist=[]
        for x in somelist:
            tm= Counter(lst)[x]
            templist.append(tm+1)
        list5.append(templist)
#print(list5)
list6 = []
for s in test_list:
    count_zero = 0
    for c_element in s:
        cl=c_element[3:5].split()
        somelist2 = c_element[5:].split()
        #print(somelist2)
        templist=[]
        for x in somelist2:
            tm= Counter(lst2)[x]
            templist.append(tm+1)
        list6.append(templist)
#print(list6)
dict_0 = []
def pos():
    #print("positive")
    for x in list5:
        multi = len(x)
        num1=list(prior_dict.values())[0]
        num2=functools.reduce(operator.mul, x, 1)
        pos_nb_prob = (num1*num2)/(len(list_class_1)+abs(len(list_vocab)))**len(x)
        #print(pos_nb_prob)
        dict_0.append(pos_nb_prob)
dict_1 = []
def neg():
    #print("negative")
    for x in list6:
        multi = len(x)
        num1=list(prior_dict.values())[0]
        num2=functools.reduce(operator.mul, x, 1)
        pos_nb_prob = (num1*num2)/(len(list_class_1)+abs(len(list_vocab)))**len(x)
        #print(pos_nb_prob)
        dict_1.append(pos_nb_prob)
sort = sorted(list(prior_dict.keys()))
if sort[0] == '0':
    pos()
if sort[1] == '1':
    neg()
o=0
p=0
m=0
while (o<len(list5)):
    if dict_0[o]>dict_1[o]:
        print(test_doc[o]," = ", "class 0")
        o=o+1
        p=p+1
    else:
        print(test_doc[o]," = ", "class 1")
        o=o+1
        m=m+1
v = list(Counter(list_c).values())[0]
v2 = list(Counter(list_c).values())[1]
#print(p,m)
proc =abs( (v2 - m) / v2 * 100)
proc2 =abs( (p - v) / v * 100)
if proc == proc2:
    
    print("Accuracy on test data = ",round(100 - proc), "%" )

