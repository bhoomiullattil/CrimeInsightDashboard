import spacy
from spacy import displacy
from spacy import tokenizer
import random
from traindata import TRAIN_DATA
from spacy.util import minibatch,compounding
from pathlib import Path
from spacy.training.example import Example
nlp=spacy.load('en_core_web_sm')
nlp.pipe_names
ner=nlp.get_pipe("ner")

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
        '''texts, annotations = zip(*batch)
        nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                   # drop=0.5,  # dropout - make it harder to memorise data
                    losses=losses,
                )
        print("Losses", losses)'''
        for text, annotations in batch:
        # create Example
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
        # Update the model
            nlp.update([example], losses=losses, drop=0.3)

    random.shuffle(TRAIN_DATA)

doc=nlp("police seized drugs from van")
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])