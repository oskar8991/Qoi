from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import urllib.request
from googlesearch import search

# tag_visible() and text_from_html() taken from:
# https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text

class WebScrapper:

    def __init__(self):
        print("Web scraping initialized...")

    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True


    def text_from_html(self, body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)

    def webScrape(self, webList):
        toSummarize = ""
        text = ""
        for x in webList:
                if "wikipedia" in x:
                    #print('wiki')
                    source = requests.get(x).text
                    soup = BeautifulSoup(source, 'lxml')
                    #print(soup)
                    response = requests.get(x)
                    html = BeautifulSoup(response.text, 'html.parser')

                    title = html.select("#firstHeading")[0].text
                    paragraphs = html.select("p")
                    #print(paragraphs)
                    allText = '\n'.join([para.text for para in paragraphs])
                    #toSummarize += " " + allText
                    for para in paragraphs:
                        if(len(toSummarize) < 5000):
                            toSummarize += " " + para.text
                        else:
                            break
                else:
                    html = urllib.request.urlopen(x).read()
                    #summarise1 = Summarizer()
                    #outputResult = summarise1.summarize(text_from_html(html))
                    #print(outputResult)
                    #toSummarize += " " + self.text_from_html(html)
                    if(len(toSummarize) < 5000):
                        toSummarize += " " + self.text_from_html(html)
                    else:
                        break

        return(toSummarize)

    
    




