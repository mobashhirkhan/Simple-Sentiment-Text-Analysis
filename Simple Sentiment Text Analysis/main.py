from textblob import TextBlob
from newspaper import Article
# import nltk
# nltk.download('punkt')

val = input("Enter a url or sentence: ")

if val.startswith("http"):
    url = val
    article = Article(url)

    # to get it into the script
    article.download()
    # to parse the article and make it readable
    article.parse()
    # to perform natural language processing
    article.nlp()
    # getting the summary of the article
    text = article.summary
    # print(text)

    blob = TextBlob(text)
    # to get a score of -1 to 1
    sentiment = blob.sentiment.polarity

    print(sentiment)

else:
    text = val
    blob = TextBlob(text)
    # to get a score of -1 to 1
    sentiment = blob.sentiment.polarity

    print(sentiment)