# Python program 
# TEXTE PARSING and pre-processing

# Import brain modules
import os
import shutil
import urllib.parse
import time

RELAX_TIME = 0
LENGTH_LINE_LIMIT = 6

# TEXTE PARSING AND INFORMATION EXTRACTION
#This function read the texte
def read_files():

    print("Starting document cleaner...")
    PATH = "/home/dr-g/Projet/Programmation/Python/wiki-url-spider-1.0/spider/"
    files = os.listdir(PATH)
    relax(RELAX_TIME)
    
    print("Starting loop process...")
    for file_name in files:
        # Read file
        text_content = ""

        print("Getting document in the folder...")
        relax(RELAX_TIME)
        
        PATH = "/home/dr-g/Projet/Programmation/Python/wiki-url-spider-1.0/spider/"
        print("Document path : " + PATH)
        files = os.listdir(PATH)
        relax(RELAX_TIME)
        
        # Getting document in the folder
        with open(PATH + file_name, "r", encoding="UTF-8") as file: 
            # reading each line     
            text_content = file.read()
            file.close() 

        print("Transfer text information into local buffer...")
        relax(RELAX_TIME)

        PATH = "/home/dr-g/Projet/Programmation/Python/wiki-nerd-1.1/"
        files = os.listdir(PATH)
        relax(RELAX_TIME)
        
        with open(PATH + "buffer.txt", "w", encoding="UTF-8") as file: 
            # reading each line     
            file.write(text_content)
            file.close() 

        # transfer text information into buffer
        subject = clean_title(file_name)
        print("Start cleaning process...")
        relax(RELAX_TIME)

        # start reading process
        clean_text(subject)
        relax(RELAX_TIME)
        

def relax(s):
    time.sleep(s)
 
def check_line_stop_sentences(line):
    
    PATH = "/home/dr-g/Projet/Programmation/Python/wiki-nerd-1.1/"
    files = os.listdir(PATH)
    relax(RELAX_TIME)
    
    temp_line = line.lower() 
    with open("stop_sentences.txt","r") as file: 
        # reading each line"
        for sentence in file:
            sentence, temp_line = normalize(sentence, temp_line) 
            #print("loaded sentence:        \t\t" + sentence)
            #print("line being verified:    \t\t" + temp_line)
            if sentence in temp_line:
                limit = int(len(temp_line)/4)
                #print("We have a match for:         \t\t" + temp_line[0:limit])
                #print("loaded stop sentence:        \t\t" + sentence)
                return " "
    return line

def check_line_for_stop_code(line):
    
    PATH = "/home/dr-g/Projet/Programmation/Python/wiki-nerd-1.1/"
    files = os.listdir(PATH)
    relax(RELAX_TIME)

    temp_line = line.lower() 
    with open("stop_code.txt","r") as file: 
        # reading each line"
        for sentence in file:
            sentence, temp_line = normalize(sentence, temp_line) 
            #print("loaded sentence:        \t\t" + sentence)
            #print("line being verified:    \t\t" + temp_line)
            if sentence in temp_line:
                limit = int(len(temp_line)/4)
                #print("We have a match for:         \t\t" + temp_line[0:limit])
                #print("loaded code stop sentence:    \t\t" + sentence)
                return " "
    return line

def normalize(first_match, second_match):
    first_match = first_match.replace("\n", "") 
    second_match = second_match.replace("\n", "") 
    return first_match, second_match

#This function cleans the document title
def clean_title(file_name):
    
    # subject string variable
    subject = ""
    file_name = trim(file_name)  
    
    # add url decoder to convert all char to readeable text
    file_name = urllib.parse.unquote(file_name)
    file_name = file_name.replace("_", " '")

    # clean the filename to convert into text subject
    for word in file_name.split():
        # clean problematic char from title string
        word = clean_word_noise(word)
        # final string triming
        word = trim(word)
        # concatenate subject
        subject = subject + " " + word
        subject = trim(subject)
        
    return subject

def check(text):
    if len(text) > 0:
        print(text)
        return True
    else:
        return False

#This function read the texte
def clean_text(subject):

    line = ""
    full_text = ""
    
    PATH = "/home/dr-g/Projet/Programmation/Python/wiki-nerd-1.1/"
    files = os.listdir(PATH)
    relax(RELAX_TIME)
    
    with open("buffer.txt","r") as file: 
        # reading each line
        for line in file: 
            # ELIMINATE WIKI SPIDERED STATISTICS
            if (line == "NewPP limit report\n"): 
                break
            
            # clean line content
            # ELIMINATE LINE WITH CODE AND CSS
            line = check_line_for_stop_code(line)
            line = check_line_stop_sentences(line) 
            
            # ELIMINATE UNIDENTIFIED CHAR IN EACH SENTENCE WORD
            line = clean_sentence(line) 

            # Eliminate all double line returnsWS
            full_text = full_text.replace("\n\n\n", "\n")

            # Identify title of the section of text
            if line.find("[edit]") > 0:
                full_text = full_text + "\n" + line + "\n"
            else:
                # Find the content section in the text
                if line == "Contents":
                    full_text = full_text + "\n" + line + "[edit]\n"
                else:
                    # TODO - Need to fix this problem
                    # CAREFULL THIS FILTER ELIMINATE WORDS THAT
                    # HAVE LESS THEN 6 CHAR LENGTH IT IS TO
                    # SIMPLIFY THE PROGRAM 
                    # Needs to be insterted eventally in the memory
                    if len(line)>LENGTH_LINE_LIMIT:
                        full_text = full_text + line + "\n"
            
        file.close()

    # clean file name to extract cleanest 
    # subject for data classification
    subject = subject.replace(" txt", "")
    #print("Before cleaning title: " + subject)

    subject = clean_word_noise(subject)
    subject = format_file_name(subject)
    
    print("Subject: " + subject)

    # construct path to save data
    PATH = "./data/"+ str(subject)
    #print("After cleaning title: " + PATH)

    if (len(subject)>1):
        # Save cleaned data
        with open(PATH,"w") as file: 
            file.write(full_text)
            file.close()
        
def clean_word_noise(word):
    
    index = 0
    word = trim(word)  
      
    for char in word:
        if not char in ",.[]{}();:?!aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789áÁàÀâÂäÄãÃåÅæÆçéÉèÈêëËÍìÌîÎïÏñÑóÓòÒôÔöÖõÕøØœŒßúÚùÙûÛüÜ":                    
            word = word.replace(char, " ")

    word = trim(word)  
    return word

def clean_sentence(line):
    
    line = trim(line)
    index = 0
    
    for char in line:
        # sentence list     
                       
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
                
            previous_letter = ''
            
            if (index-1>=0):
                previous_letter = line[index-1]
        
            if (previous_letter.islower()):
                #print("LINE BEFORE : " + line)
                line = line.replace(previous_letter+char, previous_letter + " " + char)
                #print("SEPERATING WORDS AFTER REPLACEMENT : " + line)
                
            if (previous_letter.isnumeric() and not char.isnumeric()):
                #print("LINE BEFORE : " + line)
                line = line.replace(previous_letter+char, previous_letter + " " + char)
                #print("SEPERATING WORDS AFTER REPLACEMENT : " + line)
                
        index = index + 1        
    
    line = trim(line)
    
    return line

def format_file_name(word):
    
    if (word[0]=="_"):
        word = word[1:len(word)]
        
    word = trim(word)
    word = word.replace(" txt", "")
    word = word.replace(".txt", "")
    word = word.replace("  ", "_")
    word = word.replace(" ", "_")
    word = word.replace("__", "_")
    word = trim(word)
    return word

def debug_log(debug_info): 
    f = open("debug.log", "a+")
    f.write("\n" + str(debug_info))
    f.write("\n")
    f.close
    
def trim(text_section): 
    text_section = text_section.strip()
    text_section = text_section.lstrip()
    text_section = text_section.rstrip()
    return text_section 

def save_noise(noise):
    f = open("noise.txt", "a")
    f.write("\n" + str(noise))
    f.write("\n")
    f.close
    
read_files()