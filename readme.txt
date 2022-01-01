THIS AN OLD PROJECT NOT MAINTAINED AND FOR EDUCATIONAL PURPOSES

**wiki-nerd_0.1**

This is an AI project for exploring machine learning with Wikipedia. 

It uses nlp techniques to read wikipedia text data. 
This is an exploration project for testing NLP techniques and text extraction techniques from structured documents.

WikiNerd memories data and classifies it by extracting semantic based on keyword frequencies found in diferent section of a same wikipedia document. 

The system self-learn by reading wikipedia texts and linking subjects together it is still in developpement.

After the learning process the system can be switched to detection mode. 

It then reads a text and then matches the networks to try to classify the documents subjects being read.

INSTALLATION GUIDE
Just copy these folders to your working directory

/wiki-nerd_1.0
/wiki-url-spider_1,0
/wiki-semantix_1.0

OPERATION GUIDE

1) LETS SPIDER SOME WIKI PAGES

From the bash terminal just use this commands

Python 2

python ./wiki-url-spider_1,0.py

Python 3

python3 ./wiki-url-spider_1,0.py

insert wiki url in urls.txt

Find a page you would like the system to start spidering and insert de url in the urls.txt. The spider will download the page extract the ebglish links and safe a copy to the data folder and spider folder.

2) TEXT UNIFORMATION AND PREPROCESSING

Run text uniformisation and preparation script

text_tools.py

3)  LEARNING PROCESS

Running wiki-nerd_1.0.py will start the learning process

4)  CLASSIFICATION 

Run after learning process to classify document

Set MODE in script to DETECTING
wiki-nerd.py

UNDER THE HOOD 
PROJECT DETAILS: MECHANICS AND ARCHITECTURE

LEARNING PHASE

1) The system finds the subject. 
2) The system reads the text 
3) Then the system converts the text into semantique networks. 
3) It stores it to memory

CLASSIFICATION PHASE

The system can then read text, evaluate them and classify them so it can find related subjects. The system also summarizes in a dynamique changing template the information extracted during the classification phase.

OPEN SOURCE PHILOSOPHIE

The software is taylord for wikipedia texts.
But can be modified to work with any textual data source. 
If you want to modify the software you are welcome.

DATA GATHERING WORKFLOW

First the documents data must be spidered. I specifique wiki spider was developed to download and extract text from wikipedia. 

The work is passed to a text cleaner that simplifies the actual reading process. Then the program reads and learns the textual information. It stores it. Then the system can run in detection mode and read and identify the subject of any text document. A copy of the html was saved for further development and smarter text extraction. 

The learning program reads the collected and cleaned document.

LET THE NERD LEARN

System reads a document and is feeded a subject for the document from the spider program.

System stores high frequency keywords in relation to related subjects that are identified in the text. 

The data being used as many sections and sub titles the main subject is related to other related subjects and the frequency of the keywords are related to these sections. 

Semantic network
title - subtitle - keywords

We store the title then the subtitle and the keywords related. 
Keyword frequency is represented by weights. 

1,2 After the learning process

The system reads a text file and checks memory for matches then it tries to identify the text subject. It will also try to summarize the information and make relations with other subjects. The ability to identify a subject can then be used to search the internet automatically for a user leaving automating the search process for users and delivering automatically content with high quality value. 

Project objectives and application

1) Auto classification of text documents
2) Auto evaluation of text documents
3) Query generation and exploration 
4) Semantic networks with binary memory
5) Self-learning capability 
6) Search process automation

TODO - needed for the project

Memory dictionnary
User profile 
Search algorithms
Spreading activation
Text evaluation
Tests
Refine stoplists 
Website interface
Summarization
Text creation 
Internet module 

THIS AN OLD PROJECT NOT MAINTAINED AND FOR EDUCATIONAL PURPOSES

Memo SIM - Happy to share

SIM - Service Memosa
https://services-memosa.weebly.com/
