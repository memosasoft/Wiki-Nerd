# Python program to AI learning from reading text data
from datetime import datetime

## Importing Necessary Modules
import requests     # to get image from the web
import shutil       # to save it locally
import datetime     # user for unique file name
import time         # used for sleep relax function
import os           # used to navigate OS path
import urllib.parse # used to format file name that comes from url
import shelve       # used for saving sys memory
#import text_tools as txt_tool

RELAX_TIME = 0.00314

# Learning settings 
# TODO - Should be dynamique depending on the size of document
# NOT YT IMPLEMENTED
QUALITY_THRESHOLD = 0

# MIN_KEYWORDS_IN_NET determine how many keywords 
# needed to incorporate net in memory
MIN_KEYWORDS_IN_NET = 5

# KEYWORD_MATRIX_LIMIT_SIZE and KEYWORD_MATRIX_LIMIT_WEIGHT
# determine how many keywords in net memory
# determine the weight of a keyword in net memory
KEYWORD_MATRIX_LIMIT_SIZE = 20
KEYWORD_MATRIX_LIMIT_WEIGHT = 1

MIN_KEYWORD_LEN = 1
MAX_KEYWORD_LEN = 15 

# Experimental objects and data-structures
# looking for a way to save the data 
# looking for a way to collect de data

base_subject = ""

keywords = {}   
dictionnary = {}  
data_dates = []

stop_words = []
stop_code = []
stop_sentences = []

# memory data-structure
semantic_subject = ""
semantic_net_id = 0

# semantic network dictionnary
semantic_net = {"NOTHING": 0, "INIT": 0, "TESTING": 0}

# memory sub lists for memory management
net_memory = [semantic_net]
subject_memory = []
dates_memory = []

# Start reading folder with wiki text
# the text where downloaded with another 
# python program: 
# wiki_url_spider.py

# preformate downloaded WIKI Documents 
# before starting reading and learning 
# txt_tool.read_files() - text_tools.py

def start_program():
    
    # Program intro
    print("WELCOME TO MY WIKI-NERD-1.1\n") 
    print("------------------------------")         
    print("Python AI - self-learning program")
    print("Using Wikipedia to extract semantic networks\n")
    print("Memosa Services") 
    print("help: gfm.mail.72@gmail.com")
    clean_memory()
    relax(RELAX_TIME)
    read_files()
    
def read_files():
    
    global base_subject
    
    # user interaction to help understand program flow
    #print("STARTING READING WIKI LOCAL FILES")
    #print("Document path :")
    
    # Set the path where the wiki documents are found
    PATH = "/home/dr-g/Projet/Programmation/Python/wiki-nerd-1.1/data"
    
    # Set the path
    files = os.listdir(PATH)
    #print(str(PATH))

    print("\n\nMAIN LOOP - STARTED")
    print("STARTING DOCUMENT READING PROCESS...")
    
    # iterate thru all files in the folder
    for file_name in files:

        print("Getting document in the folder...")
        relax(RELAX_TIME)
        
        # Getting document in the folder
        with open(PATH + "/" + file_name, "r") as file: 
            # reading each line     
            text_content = file.read()
            file.close() 

        print("Transfer text information into local buffer...")
        relax(RELAX_TIME)

        with open("buffer.txt", "w") as file: 
            # reading each line     
            file.write(text_content)
            file.close() 

        # transfer text information into buffer
        subject = clean_title(file_name)   
        base_subject = subject
        
        print("MAIN SUBJECT: " + subject)
        relax(RELAX_TIME)
                
        # start first loop reading process 
        # looking for keyword matrix
        print("STARTING reading process and learning process")
        read_and_learn(subject)
        
        # Pace the system
        relax(RELAX_TIME)
        
        ##print("STARTING FINAL CLEANING PROCESS")
        # clean memory before next loop
        clean_memory()
        
        # Pace the system
        relax(RELAX_TIME)
    
#This function read the texte
def read_and_learn(subject):
    
    global keywords
    global base_subject
    
    # BUG - Need to init the variable
    previous_subject = ""
    
    # BUG - insert the subject in the keyword array
          
    print("\n\nSTARTING KEYWORD EXTRACTION FOR TEXT BUFFER")  
    print("\nBUFFER DOCUMENT TITLE IS : " + subject)  
    relax(RELAX_TIME)
    
    PATH = "/home/dr-g/Projet/Programmation/Python/wiki-nerd-1.1/"
    files = os.listdir(PATH)   
            
    with open("buffer.txt","r") as file: 
        # reading each line
        for line in file: 
    
            if verify_line(line):
                continue  
            
            print("\n____________________________________________________")
            print("STARTING NEW LINE CLEAN UP PROCESS...")
            print("This is the line:\n")
            print(line)  
            
            # CLEANING PROCESS AND NOISE ELIMINATION
            print("checking stop sentences...")
            line = check_line_for_stop_sentences(line) 
            
            if verify_line(line):
                continue 
            
            relax(RELAX_TIME)
            
            print("checking stop code...")
            line = check_line_for_stop_code(line)
            
            if verify_line(line):
                continue 
            
            relax(RELAX_TIME)
            
            print("checking stop list...")
            line, line_clean = clean_stop_list(line)
            
            if verify_line(line_clean):
                continue  
            
            relax(RELAX_TIME)

            if (scan_for_subject(subject, line)):
 
                print("NEW subject FOUND")
                print("subject was: " + subject) 
                previous_subject = subject
                
                if(keywords!=None):
                    if (int(len(keywords)) > MIN_KEYWORDS_IN_NET):
                        # Save memory and clean memory
                        print("Creating memory entry - build_keyword_matrix")
                        build_keyword_matrix(previous_subject, line)
                        keywords.clear()
                    
                subject = line[0:line.find("[edit]")]
                
                # Create new sub-subject
                subject = create_subject(subject, base_subject, line)
                relax(RELAX_TIME)
                
                print("new subject is: " + subject)
                                                    
            ##print("UGLY FUNCTION")
            line = catch_menu(line)
            
            if verify_line(line):
                continue       
              
            # returns the line with minimal text processing
            # returns the clean_line with full text processing
            try: 
                #print("FINAL LINE CLEANSING")
                #print("BEFORE: ")
                #print(line_clean)
                
                line_clean = final_line_cleansing(line_clean) 
                
                if verify_line(line_clean):
                    continue  
                
                #print("AFTER: ")
                #print(line_clean)    
                
                relax(RELAX_TIME)                
            except:
                #print("ERROR IN FINAL LINE CLEANSING")
                continue
            
            # reading each word  
            list_words = []
                 
            for word in line_clean.split():
                
                if verify_line(word):
                    continue
                
                #print("FINAL WORD CLEANSING")
                #print("BEFORE: ")
                #print(word)
                
                # Final word clean up 
                word = clean_it(word)
                word, clean_word = clean_stop_list(word)
                
                #print("AFTER: ")
                #print(word)
                
                relax(RELAX_TIME)            
                            
                if verify_line(clean_word):
                    continue
                
                print("FIRST LEVEL: " + clean_word)
                build_keyword_frequency(clean_word)
                add_to_dictionnary(clean_word)

                if len(list_words) > 0 and not clean_word.isnumeric():
                    key = int(len(list_words))
                    old_subject = list_words[key-1]
                    build_keyword_frequency(old_subject + " " + clean_word)
                    print("SECOND LEVEL: " + old_subject + " " + clean_word)
                    
                    if len(list_words) > 1 and not clean_word.isnumeric():
                        key = int(len(list_words))
                        first_old_subject = list_words[key-2]
                        print("THIRD LEVEL: " + first_old_subject + " " + old_subject + " " + clean_word) 
                        build_keyword_frequency(first_old_subject + " " + old_subject + " " + clean_word)
                     
                        if len(list_words) > 2 and not clean_word.isnumeric():
                            key = int(len(list_words))
                            second_old_subject = list_words[key-3]
                            print("FOURTH LEVEL: " + second_old_subject + " " + first_old_subject + " " + old_subject + " " + clean_word) 
                            build_keyword_frequency(second_old_subject + " " + first_old_subject + " " + old_subject + " " + clean_word)
                     
                            if len(list_words) > 3 and not clean_word.isnumeric():
                                key = int(len(list_words))
                                third_old_subject = list_words[key-4]
                                print("FIFTH LEVEL: " + third_old_subject + " " + second_old_subject + " " + first_old_subject + " " + old_subject + " " + clean_word) 
                                build_keyword_frequency(third_old_subject + " " + second_old_subject + " " + first_old_subject + " " + old_subject + " " + clean_word)
                     
                list_words.append(clean_word)
    
    # when file is finished write last memory information       
    if(keywords!=None): 
        if (len(keywords) > MIN_KEYWORDS_IN_NET):
            # Save memory and clean memory
            print("END of document")
            print("subject: " + subject)
            print("Creating memory entry - build_keyword_matrix")        
            
            build_keyword_matrix(subject, line)
            keywords.clear()  
            subject = ""  

def verify_line(input):
    
    if (input == None):
        return True  
    
    if input == ""  or len(input) < 1 or input == " ":
        return True  
    else:
        return False
    
    
def clean_again_alien(word):
    if (len(word)-1>0):
        if word[len(word)-1] == ".":
            word = word[0:len(word)-1]
        if word[len(word)-1] == ",":
            word = word[0:len(word)-1]
        if word[len(word)-1] == ":":
            word = word[0:len(word)-1]
        if word[len(word)-1] == ";":
            word = word[0:len(word)-1]
    return word

def clean_it(word):
    
    word = clean_again_alien(word)              
    word = clean_word_final(word)
    return word

def scan_for_subject(subject, line):
    if line.find("[edit]")>0:
        return True
    return False

def sort_keyword_matrix():
    
    try:
        global keywords
        
        sorted_values = sorted(keywords.values(), reverse=True) # Sort the values
        sorted_dict = {}

        for i in sorted_values:
            for k in keywords.keys():
                if keywords[k] == i:
                    sorted_dict[k] = keywords[k]
                    continue
    except:
        return("Error in sort_keyword_matrix")     
           
    return sorted_dict

# MY UGLY FUNCTION
# ITS UGLY BUT IT WORKS
def catch_menu(line):
    
    try:
        # convert into recursive function
        if (line[0].isnumeric()):
            if len(line)>1:
                if (line[1]==" "):
                    line = line[2:len(line)]   

        return line
    except:
        #print("ERROR - In UGLY function")                                
        return line
                
#This function cleans the document title
def clean_title(file_name):
    
    # subject string variable  
    subject = format_filename(file_name)
    
    if (subject==None) or (subject==""):
        return ""
  
    return subject

def format_filename(file_name):
    # add url decoder to convert all char to readeable text
    file_name = urllib.parse.unquote(file_name)
    file_name = file_name.replace("_", " ")
    file_name = file_name.replace(".txt", " ")
    file_name = trim(file_name)
    return file_name

def create_subject(subject, previous_subject, line):
    subject = subject + " - " + previous_subject
    return subject
    
def build_keyword_frequency(word): 
    # verify keyword 
    global keywords
    global data_dates
    
    if check_for_year(word):
        if (len(word)==4):
            data_dates.append(word)
    else:
        keywords = insert_in_memory(word)     
        
# They are: pickle, shelve and json. 
# Each one has its own characteristics 
# and the one you have to use is the 
# one which is more suitable to your project.
def save_memory(subject, net, data_dates):
    
    # save memory object
    global shelf_net
    global shelf_subject
    global shelf_date
    
    # Counter 
    global semantic_net_id 
    
    # Memory    
    global net_memory
    global subject_memory
    global dates_memory
      
    # file to be used
    semantic_net_id =  semantic_net_id + 1  
    
    net_memory.append(net.copy())
    subject_memory.append(subject)
    dates_memory.append(data_dates)
    
    shelf_net = shelve.open("mem_data")
    shelf_subject = shelve.open("mem_subject")
    shelf_date = shelve.open("mem_dates")

    # serializing
    shelf_net["net_memory"] = net_memory
    shelf_subject["subject_memory"] = subject_memory
    shelf_date["dates_memory"] = dates_memory
    
    shelf_net.close() # you must close the shelve file!!!
    shelf_subject.close()
    shelf_date.close()
    
def load_memory():
    # save memory object
    global shelf_net
    global shelf_subject
    global shelf_date
    
    # Counter 
    global semantic_net_id 
    
    # Memory    
    global net_memory
    global subject_memory
    global dates_memory
    
    shelf_net = shelve.open("mem_data") # the same filename that you used before, please
    net_memory = shelf_net["net_memory"]
    shelf_net.close()
        
    shelf_subject = shelve.open("mem_subject") # the same filename that you used before, please
    subject_memory = shelf_subject["subject_memory"]
    shelf_subject.close()
    
    shelf_date = shelve.open("mem_dates") # the same filename that you used before, please
    subject_memory = shelf_date["dates_memory"]
    shelf_date.close() 

def insert_in_memory(word):
    global keywords 
    
    try:
        if word==None:
            return keywords
        
        if (len(word)>MIN_KEYWORD_LEN):   
            if word in keywords:
                keywords[word] = keywords[word] + 1
            else: 
                keywords[word] = 1
            return keywords
    except:
        print("ERROR - In insert in memory")
        return keywords
        

def add_to_dictionnary(word):
    
    global dictionnary 
    
    try:
        if word==None:
            return dictionnary
        
        if (len(word)>MIN_KEYWORD_LEN):   
            if word in dictionnary:
                dictionnary[word] = dictionnary[word] + 1
            else: 
                dictionnary[word] = 1
            return dictionnary
    except:
        print("ERROR - In insert in memory")
        return dictionnary
    
    return True

def save_dictionnary():
    global dictionnary 
    
    f = open("dictionnary.txt", "w")

    for word in dictionnary:
        f.write("[" + word + "," + str(dictionnary[word])+ "],")
    f.close
    
def build_keyword_matrix(subject, line):
    
    global semantic_net_id
    global semantic_subject
    global semantic_net
    global keywords
    global data_dates
    
    relax(RELAX_TIME)
    semantic_subject = subject
    keywords = sort_keyword_matrix()
  
    # TODO Check iterator to check the index
    index = 0
    
    print("CREATING SEMANTIC NET")
    print("Subject: " + semantic_subject)
    
    semantic_net.clear()
    
    for key in keywords:
        
        if check_for_year(key):
            if (len(key)==4):
                data_dates.append(key)
            continue
        
        # Number of semantic top nodes 
        # to be inserted into memory 
        if (KEYWORD_MATRIX_LIMIT_SIZE < index):
            break
        
        # Weight constraint of semantic net
        # to be inserted into memory 
        if (KEYWORD_MATRIX_LIMIT_WEIGHT > keywords[key]):
            continue
        
        index += 1
        
        #print("keyword: " + key)
        #print("weight: " + str(keywords[key]))

        semantic_net[key] = keywords[key]
         
    if (len(semantic_net)>MIN_KEYWORDS_IN_NET):
        semantic_subject = subject
        
        save_memory(subject, semantic_net, data_dates)
        semantic_net.clear()
    else:
        print("SEMANTIC NETWORK IS NOT BIG ENOUGHS TO SAVE TO MEMORY")
                        
    print("Number of learned documents = " + str(semantic_net_id))
    
    # Print matrix 
    print_keyword_matrix()

def print_keyword_matrix():
    global keywords
    
    matrix = ""
    print("MATRIX keywords are: ")
    
    for keyword in keywords:    
        # Build matrix   
        weight = keywords[keyword]   
        matrix = matrix + "[" + keyword + "," + str(weight)+"] - " 
    
    print(matrix)
    
    return keywords
    
def check_for_year(value):
    if (value.isnumeric()) and len(value) == 4:
        return True
    else:
        if value.isnumeric():
            return True
        else:
            return False

#This function cleans the document title
def clean_memory():
    
    global keywords  
    global data_dates
    
    # keywords NONE Bug
    if keywords == None:
        keywords = {}
        keywords["initiate"] = 0
        
    # data_dates NONE Bug
    if data_dates == None:
        data_dates = []
        data_dates.append("1972")
        
    keywords.clear()
    data_dates.clear()
 
def final_line_cleansing(line):

    # eliminate char and numbers
    line = clean_word_noise(line)

    if (line == None) or (line == "") or (line == " "):
        return ""
    
    # special text processing for lower case text 
    line = line.replace("\n", "")  
    
    # string cleansing
    line = trim(line)   
    
    return line
   
def clean_stop_list(line):    
        
    # preformating word     
    line = trim(line)
    line = clean_word_seperation(line)     
    line_clean = line.lower() 

    for word in line_clean.split():
        if word in stop_words:    
            try:    
                print("CLEANING AND ELIMINATING word")
                print("BEFORE CLEANING")
                print(line_clean)
                line_clean = line_clean.lower().replace(" " + word.lower() + " "," ")
                
                # when stop word is at the end of the sentence
                if line_clean.find(word)+len(word) == len(line_clean):
                    line_clean = line_clean.lower().replace(" " + word.lower()," ")   
                    
                # when stop word is at the start of the sentence
                if line_clean.find(word) == 0:
                    line_clean = line_clean.lower().replace(word.lower() + " "," ")   
                
                # when stop word and the line are the same
                if len(line_clean) == len(word):   
                    return line, ""
                
                print("AFTER CLEANING")
                print(line_clean)   
            except:
                print("ERROR in stoplist")    
    return line, line_clean

def check_line_for_stop_code(line):

    for word in stop_code:
        
        try:
            word, line = normalize(word.lower(), line) 
            ##print("loaded word:        \t\t" + word)
            ##print("line being verified:    \t\t" + temp_line)
            if (line.lower().find(word.lower())>=0):
                print("We have a match for:         \t\t" + temp_line[0:limit])
                print("loaded code stop code:    \t\t" + word)
                return ""
        except:
            print("ERROR in stop_code")
            return ""
            
    return line

def check_line_for_stop_sentences(line):
    
    for word in stop_sentences:
        
        try:
            word, line = normalize(word.lower(), line) 
            ##print("loaded word:        \t\t" + word)
            ##print("line being verified:    \t\t" + temp_line)
            if (line.lower().find(word.lower())>=0):
                print("We have a match for:         \t\t" + temp_line[0:limit])
                print("loaded code stop sentence:    \t\t" + word)
                return ""
        except:
            print("ERROR in stop_code")
            return ""
                    
    return line

def normalize(first_match, second_match):
    first_match = first_match.replace("\n", "") 
    second_match = second_match.replace("\n", "") 
    return first_match, second_match

def load_stop_list():
    global stop_words 

    with open("stop_list.txt","r") as file: 
    # reading each line"
        for word in file:
            word = word.replace("\n","")
            word = trim(word)
            stop_words.append(word)
            
            
def load_stop_code():
    global stop_code
    
    with open("stop_code.txt","r") as file: 
                                  
        # reading each line"
        for line in file:
            line = line.replace("\n","")
            line = trim(line)
            stop_code.append(line)

def load_stop_sentences():
    global stop_sentences
    
    with open("stop_sentences.txt","r") as file: 
                                  
        # reading each line"
        for line in file:
            line = line.replace("\n","")
            line = trim(line)
            stop_sentences.append(line)
            

def clean_word_noise(line):
    
    line = trim(line)
    index = 0
    
    for word in line:
        for char in word:
            
            try:
                if not char in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789áÁàÀâÂäÄãÃåÅæÆçéÉèÈêëËÍìÌîÎïÏñÑóÓòÒôÔöÖõÕøØœŒßúÚùÙûÛüÜ":                    
                    word = word.replace(char, " ")
    
                if char in "^\"\'()?\\/$*":
                    word = word.replace(char, " ")
            except:
                print("ERROR in clean_word_noise with char : " + char + " and word: " + word)
            index = index + 1
        index = 0
    line = trim(line)
    return line

def clean_word_noise(word):    
    for char in word:
        if not char in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789áÁàÀâÂäÄãÃåÅæÆçéÉèÈêëËÍìÌîÎïÏñÑóÓòÒôÔöÖõÕøØœŒßúÚùÙûÛüÜ":                    
            word = word.replace(char, " ")
    word = trim(word)
    return word

def clean_word_seperation(word):
    index = 0
    for char in word:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            previous_letter = ''
            if (index-1>0):
                previous_letter = word[index-1]
            if (previous_letter.islower()):
                word = word.replace(char, " " + char)
        index = index + 1
    word = trim(word)
    return word

def clean_word_final(word):
    index = 0
    for char in word:
        # ^ is the references char
        if char in "()(){},:;|*/+\"\\~^–":
            word = word.replace(char, " ")
        index = index + 1
    
    word = trim(word)
    return word

def trim(text_section): 
    text_section = text_section.strip()
    text_section = text_section.lstrip()
    return text_section 

def relax(sec):
    time.sleep(sec) 
    
def save_noise(noise):
    f = open("noise.txt", "a")
    f.write("\n" + str(noise))
    f.write("\n")
    f.close
    
def debug_log(debug_info): 
    f = open("debug.log", "a+")
    f.write("\n" + str(debug_info))
    f.write("\n")
    f.close

load_stop_list()
load_stop_code()
load_stop_sentences()

start_program()

save_dictionnary()

