######importe######
import nltk
from nltk import word_tokenize
import nltk.corpus.reader.tagged as tagged
import nltk.tag.hmm as hmm
from grammardefs import *
corpus_tiger=  nltk.corpus.ConllCorpusReader('.', 'tiger9', ['ignore', 'words', 'ignore', 'ignore', 'pos'],encoding='utf-8')
trainer = hmm.HiddenMarkovModelTrainer()
model = trainer.train(corpus_tiger.tagged_sents())



######code#######
eingabe= input(">>> ")
token= word_tokenize(eingabe)
pos= model.tag(token)
for word in pos: # jedes wort der eingabe wird getagged
	if "VAFIN" in word: 
		get_def VAFIN(word[1]) # wenn wort = verb, wird die dazugehörige funktion aufgerufen
		return verb # die funktion gibt dem verb eine zuweisung, z.B. verb=[S]
                            #(wenn wir personalpronomen rauslassen, brauchen wir nur Singular/Plural)
	if "NN" in word:
		get_def NN # hier zuweisung wie z.b. nomen=[M, S] 
		return nomen
	if "PDS" in word:
		get_def PDS # hier zuweisung wie z.b. artikel =[M, S]
		return artikel
.
.
.
if artikel[0] = nomen[0] and artikel[1]= nomen[1] and nomen[1] = verb [0]: # wenn alle merkmale zueinanderpassen, dann ist der Satz korrrekt
	print ("Der Satz ist korrekt!")
else:
	print ("Der Satz ist inkorrekt!")

# bei artikel und nomen ist [0]=genus und [1]=numerus
# verb ist [0]=numerus

