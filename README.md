# Qoi
Questions of Interest - HackKings 6.0

Members: Oskar Ljungdell, Ivan Hristev, Alexis Dumon, Hadi Rizvi

NLP Query Summarizer 

BACKEND--------------

Three major parts:
1. Getting the input from a user (voice) and turning it into an efficient query
2. Web scrapping for the results of the query
3. Summarize text obtained from the selected webpages using spaCy

FRONTEND-------------
1. Build an application which can take input from the user
2. Shows summary of text query in a nice format

APIs USED-------------
- NLP input processor => spaCy
- Speech recognition => pocketsphinx and pyaudio
- Search browswing => Google search
- Web scraping => BeautifulSoup4, lxml, requests
- Text Summariser => spaCy
- GUI => TkInter
