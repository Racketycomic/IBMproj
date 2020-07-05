# only extracation function
import pandas as pd
import spacy
import nltk
from pdfminer.high_level import extract_text


from pyresparser import ResumeParser
data = ResumeParser('VINAY_S_1BG17IS051.pdf').get_extracted_data()
