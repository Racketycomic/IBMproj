import pandas as pd
import spacy
import nltk
from pdfminer.high_level import extract_text
from searchextra import skill_extract
import sampleextract
from pyresparser import ResumeParser
from extractnames import extract_name
data = ResumeParser('VINAY_S_1BG17IS051.pdf').get_extracted_data()
print(data)

skilla = skill_extract(data['skills'])

#print(skilla)

resume_text = extract_text('VINAY_S_1BG17IS051.pdf')
nlp = spacy.load('en_core_web_sm')
nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
tokens=[]
for token in nlp_text:
    if token.text is not token.is_stop:
        tokens.append(token.text)
    #tokens = [token.text for token in nlp_text if not token.is_stop]
print(tokens)

data['skills'] = skilla
data['name'] = None
if data['name'] == None:
    name = extract_name(resume_text)
print(name)

    



