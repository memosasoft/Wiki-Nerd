**THIS AN OLD PROJECT NOT MAINTAINED AND FOR EDUCATIONAL PURPOSESE**

**wiki-nerd_0.1**

This is a AI project for exploring machine learning with Wikipedia. 

It uses nlp techniques to read wikipedia text data. 
This is an exploration project for tests NLP techniques and text extraction techniques from structured document.

WikiNerd memories data and classifies it by extracting semantic based on keyword frequencies found in diferent section of a same wikipedia document. 

The system self-learn by reading wikipedia texts and linking subjects together it still in developpement.

After the learning process the system can by switched to detection mode. 

It then reads a text and the matches the networks to try to classsify the documents subjets being read.

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

3)  LEARNING PROCESS

Running wiki-nerd_1.0.py will start the learning process

4)  CLASSIFICATION 

Run after learning process to classify document

Set MODE in script to DETECTING
wiki-nerd.py

UNDER THE HOOD 
PROJECT DETAILS: MECANICS AND ARCHITECTURE

LEARNING PHASE

1) The system finds the subject. 
2) The system reads the text 
3) Then the system converts the text into semantique networks. 
3) It stores it to memory

CLASSIFICATION PHASE

The system can then read text, evaluate them and classify them it can find related subjects. The system also to summarize in a dynamique changing template the information extracted during the classification phase.

OPEN SOURCE PHILOSOPHIE

The software is taylord for wikipedia texts.
But can be modified to work with any textual data source. 
If you want to modify the software you are welcome.

DATA GATHERING WORKFLOW

First the documents data must be spidered. I specifique wiki spider was developped to download and extract text from wekipedia. 

The works is passed to text cleaner that simplifies the actual reading process. Then the program read and learns the textual information. It store it. Then the system can run in detection mode and read and identifie the subject of any text document. A copy of the html was saved for futher developement and smarter text extraction. 

The the learning program reads the coillected and cleaned docunent.

LET THE NERD LEARN

System read a document and is feeded a subject for the document from the spidee program.

System stores high frequency keywords in relation to related subjects that are identified in the text. 

The data being used as many section and sub titles the main subject is related other relate subjects and the freqency of the keywords are related to this sections. 

Semantic network
title - subtitle - kewords

We store the title then the subtiltle and the keywords related. 
Keyword frequency is used represented by weights. 

1,2 After the learning process

The system read a text file and check memory for matches then it try to identify the text subject. It will also try to summurize the information and make relation with other subjects. The ability to identify a subject can then be used to search the internet automaticly for a user leaving autommating the search process for users and delivery automaticly content with high quality value. 

Project objetives and application

1) Auto classification of text documents
2) Auto evaluation of text documents
3) Query generation and exploration 
4) Semantic netwoks with binary memory
5) Self-learning capabilitie 
6) Search process automation

TODO - needed for the project

Memory dictionnary
User profile 
Search algorithms
Spreading activation
Text evalution
Tests
Refine stoplists 
Website interface
Summarization
Text creation 
Internet module 
