# Input Processor v0.1 ALPHA
# 30/11/2019 14:27
#
#

from speechToText import *
from WebParser import *
from summariser import *
import spacy
from spacy.symbols import nsubj, VERB

class inputProcessor:

    def __init__(self):
        print("input processor intialized...")


    def getSummary(self, input):
        # Load English tokenizer, tagger, parser, NER and word vectors
        nlp = spacy.load("en_core_web_sm")

        #Process whole documents
        #text = input("QOI: Hi there, how can I help? ")
        #s1 = SpeechToText()
        #text = s1.recognizeSpeech()

        doc = nlp(input)
        output = set()

        for token in doc:
            print(token.text, token.pos_, token.dep_)

        # Analyze syntax
        print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
        print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

        # Find named entities, phrases and concepts
        for entity in doc.ents:
            print(entity.text, entity.label_)
                  
        # Finding a verb with a subject from below — good
        verbs = set()
        for possible_subject in doc:
            if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
                verbs.add(possible_subject.head)
        print(verbs)

        # Refining text
        nouns = [chunk.text for chunk in doc.noun_chunks]
        arrayOfEntities = []

        for entity in doc.ents:
            output.add(entity.text)

        if arrayOfEntities:
            for entity in doc.ents:
                nouns.remove(entity.text)
            
        if nouns:
            longestChunk = (max(nouns, key=len))
            output.add(longestChunk)


        for token in doc:
            if token.pos_=="VERB":
                if token.dep_!="xcomp":
                    if token.lemma_!="tell":
                        if token.lemma_!="give":
                            output.add(token.lemma_)

        if not output:
            biggestNoun=max(nouns, key=len)
            if biggestNoun != "me" :
                output.add(biggestNoun)

                  
        print(output)

        # google search
        try: 
            from googlesearch import search 
        except ImportError:  
            print("No module named 'google' found") 
          
        # to search
        query = ""
        for x in output:
            query += " " + x


        print(query)

        urlArrayList = []

        wikiFound = False;
        for url in search(query, stop=7):
            if 'wikipedia' in url:
                if (wikiFound == False):
                    wikiFound = True;
                    urlArrayList.append(url)
            else:
                urlArrayList.append(url)

        print(urlArrayList)
                

        w1 = WebScrapper()
        webStrings = w1.webScrape(urlArrayList)

        summarise1 = Summarizer()
        outputResult = summarise1.summarize(webStrings)

        #print(webStrings)
        print(outputResult)

        
        print(" ")
        print("Statistics:")
        print("Web scrapping scrapped ",len(webStrings)," characters.");
        print("Summarizer summarized it to " ,len(outputResult), " characters.");

        returnArray = []
        returnArray.append(outputResult)
        returnArray.append(len(webStrings))
        returnArray.append(len(outputResult))

        return returnArray













