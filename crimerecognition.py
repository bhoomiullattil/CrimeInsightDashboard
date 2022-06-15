import spacy
from spacy import displacy
from spacy import tokenizer
'''nlp = spacy.load('en_core_web_sm')
  
#Load the text and process it
# I copied the text from python wiki
text ="21 people kidnapped in USA"
# text2 = # copy the paragraphs from  https://www.python.org/doc/essays/ 
doc = nlp(text)
print(type(doc))
#doc2 = nlp(text2)
sentences = list(doc.sents)
print(sentences)
# tokenization
for token in doc:
    print(token.text)
# print entities
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print(ents)
# now we use displaycy function on doc2
displacy.render(doc, style='ent', jupyter=True)'''
import random
from spacy.util import minibatch,compounding
from pathlib import Path
nlp=spacy.load('en_core_web_sm')
nlp.pipe_names
ner=nlp.get_pipe("ner")
with open('C:/Users/ullattil/Desktop/project/Crime_Loc_Visualizer/codes/main/TRAIN_DATA.py') as trainer:

    TRAIN_DATA=trainer.readlines()
print(TRAIN_DATA)
'''
for _, annotations in TRAIN_DATA:
  for ent in annotations.get("entities"):
    ner.add_label(ent[2])
    print(ent[2])
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
nlp.disable_pipes(unaffected_pipes)
for iteration in range(30):

    # shuufling examples  before every iteration
    
    losses = {}
    # batch up the examples using spaCy's minibatch
    batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        texts, annotations = zip(*batch)
        nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                   # drop=0.5,  # dropout - make it harder to memorise data
                    losses=losses,
                )
        print("Losses", losses)
    random.shuffle(TRAIN_DATA)

doc=nlp("police seized drugs from van")
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])'''