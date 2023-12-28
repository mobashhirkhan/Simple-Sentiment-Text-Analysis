Enter a url or a sentence for it to give you a score between -1 and 1. -1 means the sentence or the website is too negative, and 1 means it is positive. 0 indicates that it is fairly neutral.

To run this, you need to run a virtual environment and install from textblob and newspaper.

The first time you run, you also need to uncomment the lines:
import nltk
nltk.download('punkt')

and then comment them out again.