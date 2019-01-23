######importe######
import spacy
nlp=spacy.load("de")

from PROJEKT_defs import *


######code#######
print ("GRAMMARCHECK")
print ("Gib einen Satz ein:")
while True:
	eingabe= nlp(input(">>> "))
###funktionenzuweisung###
	for token in eingabe: 
#		print(token.pos_) 
		if "DET" in token.pos_:
			ARTIKEL(token.text)
			PLURAL_A(token.text)
		if "NOUN" in token.pos_:
			NOMEN(token.text)
			PLURAL_N(token.text)
		if "VERB" in token.pos_:
			VERB(token.text)
		if "PRON" in token.pos_:
			PRONOMEN(token.text)
#	print (artikel)
#	print (nomen)
#	print (verb)
#	print (pronomen)
	cool_list = []
###regeln#####
	for token in eingabe:
		print(cool_list)
		cool_list.append(token.pos_)
	if "PRON" in cool_list:
		if pronomen[0] == verb [0]:
			print ("Der Satz ist korrekt1!")
		else:
			print("Der Satz ist inkorrekt, weil keine Kongruenz zwischen Pronomen und Verb besteht.")
	elif "PRON" in cool_list or "PROPN" in cool_list or "DET" in cool_list or "NOUN" in cool_list:
		if cool_list == ['PROPN', 'DET']# or cool_list == ['PRON', 'DET'] or cool_list == ['NOUN', 'PRON'] or cool_list == ['DET', 'NOUN', 'PRON'] or cool_list == ['DET, NOUN, PROPN']:
			print("Der Satz ist nicht korrekt, da der Determinierer vor dem Substantiv stehen muss!")
	elif "PROPN" in cool_list:
		if verb[0]=="S3/P2":
			print ("Der Satz ist korrekt2!")
		else:
			print("Der Satz ist inkorrekt, weil keine Kongruenz mit dem Verb besteht.")
	elif "PROPN" in cool_list:
		if verb[0]=="S3/P2":
			print ("Der Satz ist korrekt!3")
		else:
			print("Der Satz ist inkorrekt, weil keine Kongruenz mit dem Verb besteht.")
	elif "DET" in cool_list and "NOUN" in cool_list and "VERB" in cool_list:
		if artikel[0] == nomen[0] and artikel[1]== nomen[1] and nomen[1] == verb [0]: 
			print ("Der Satz ist korrekt4!")
		else:
			print ("Der Satz ist inkorrekt, weil die Wörter nicht kongruent sind!")
#vereinfachte Form für richtigen Satzbau (muss bei Adjektiven, Objekten etc. verändert werden###

#	elif "DET" in cool_list or "NOUN" in cool_list or "PRON" in cool_list or "PROPN" in cool_list:
#		cool_list.find(['PRON', 'DET'] or ['PROPN', 'DET'])
#		if cool_list.find == True:
	else:
		print("Der Satz ist korrekt!")
#	else:
#		print ("Diese Satzstruktur kennen wir nicht.")
	print ("Willst du einen weiteren Satz testen?")
	eingabe= input(">>> ")
	if eingabe == "Ja":
		del artikel[:]
		del nomen[:]
		del verb[:]
		del pronomen[:]
		print ("Dann gib einen weiteren Satz ein:")
		continue
	if eingabe == "Nein":
		print ("OK!")
		break
