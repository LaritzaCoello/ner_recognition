import spacy

ner = spacy.load('es_core_news_sm')

def ner_sentence(sentence): 
    entidades = {}
    docs = ner(sentence)
    for doc in docs.ents:
        entidades[doc.text] = doc.label_
    return entidades
