######importe######
#pip3 install colorama
import colorama #mögliche Farben: Magenta, Green, Red, Cyan, Yellow, White, Black
from colorama import init, Fore, Style
init(autoreset=True)
import spacy
nlp=spacy.load("de")

from mitsatzstrukturDEF import *

######code#######
print (Fore.CYAN+"GRAMMARCHECK")
print ("Gib einen Satz ein:")
while True:
	eingabe= nlp(input(">>> "))
###funktionenzuweisung###
	for token in eingabe: 
#		print(token.pos_) 
		if "DET" in token.pos_:
			ARTIKEL(token.text)
			PLURAL_A(token.text)
		if "ADJ" in token.pos_:
			ADJEKTIV(token.text)
		if "NOUN" in token.pos_:
			NOMEN(token.text)
			PLURAL_N(token.text)
		if "VERB" in token.pos_:
			VERB(token.text)
		if "PRON" in token.pos_:
			PRONOMEN(token.text)
	print (artikel)
	print (adjektiv)
	print (nomen)
	print (verb)
	print (pronomen)
	cool_list = []
###regeln#####
	switch=0
	for token in eingabe:
		cool_list.append(token.pos_)
	try:
#regel für satzstellung
		if "PRON" in cool_list or "PROPN" in cool_list or "DET" in cool_list or "NOUN" in cool_list:
			cool_string = " ".join(cool_list)
			print(cool_string)
			if "PROPN DET" in cool_string or "PRON DET" in cool_string or "NOUN PRON" in cool_string or "DET NOUN PRON" in cool_string or "DET NOUN PROPN" in cool_string or "PRON NOUN" in cool_string or "PROPN PRON" in cool_string:
				print(Fore.RED+"Der Satz ist nicht korrekt, da die Satzstruktur von Determinierer, Nomen und Pronomen nicht korrekt ist!")
				switch=1
#regel für pronomen
		if "PRON" in cool_list:
			if pronomen[0] == verb[0] and switch==0:
				print (Fore.GREEN +"Der Satz ist korrekt!")
			elif switch==0:
				print(Fore.RED + "Der Satz ist inkorrekt, weil keine Kongruenz zwischen Pronomen und Verb besteht.")
#regel für eigennamen
		elif "PROPN" in cool_list:
			if verb[0]=="S3/P2":
				print (Fore.GREEN +"Der Satz ist korrekt!")
			else:
				print(Fore.RED + "Der Satz ist inkorrekt, weil keine Kongruenz mit dem Verb besteht.")
#regel für sätze mit adjektiv
		elif "ADJ" in cool_list and "DET" in cool_list and "NOUN" in cool_list and "VERB" in cool_list:
			if artikel[0]=="D":
				if adjektiv[0]== nomen[1] and adjektiv[1] == nomen[1] and artikel[1] == nomen[0] and artikel[2]== "F/P" and nomen[1] == verb[0]: 
					print (Fore.GREEN +"Der Satz ist korrekt!")
				elif adjektiv[0]== artikel[0] and adjektiv[1] == nomen[1] and artikel[1] == nomen[0] and artikel[2]== "F/P" and nomen[1] == verb[0]: 
					print (Fore.GREEN +"Der Satz ist korrekt!")
				elif artikel[0]==adjektiv[0] and adjektiv[1] == nomen[1] and artikel[1] == nomen[0] and artikel[2]== nomen[1] and nomen[1] == verb[0]:
					print (Fore.GREEN +"Der Satz ist korrekt!")
				else:
					print (Fore.RED +"Der Satz ist inkorrekt, weil die Wörter nicht kongruent sind!")
			if artikel[0]=="I":
				if adjektiv[0]==nomen[0] and artikel[1] == nomen[0] and artikel[2]== nomen[1] and nomen[1] == verb [0]: 
					print (Fore.GREEN +"Der Satz ist korrekt!")
				elif  adjektiv[0]==nomen[0] and artikel[1]=="M/N" and nomen[0]=="M" or nomen[0]=="N" and artikel[2]== nomen[1] and nomen[1] == verb[0]:
					print (Fore.GREEN +"Der Satz ist korrekt!")
				elif adjektiv[0]==nomen[0] and artikel[1] == nomen[0] and artikel[2]== "F/P" and nomen[1] == verb [0]: 
					print (Fore.GREEN +"Der Satz ist korrekt!")
				else:
					print (Fore.RED + "Der Satz ist inkorrekt, weil die Wörter nicht kongruent sind!")
#regel für sätze ohne adjektiv
		elif "DET" in cool_list and "NOUN" in cool_list and "VERB" in cool_list:
			if artikel[0]=="D":
				if artikel[1] == nomen[0] and artikel[2]== "F/P" and nomen[1] == verb [0]: 
					print (Fore.GREEN +"Der Satz ist korrekt!")
				elif artikel[1] == nomen[0] and artikel[2]== nomen[1] and nomen[1] == verb [0]:
					print (Fore.GREEN +"Der Satz ist korrekt!")
				else:
					print (Fore.RED + "Der Satz ist inkorrekt, weil die Wörter nicht kongruent sind!")
			if artikel[0]=="I":
				if artikel[1] == nomen[0] and artikel[2]== nomen[1] and nomen[1] == verb [0]: 
					print (Fore.GREEN +"Der Satz ist korrekt!")
				elif artikel[1]=="M/N" and nomen[0]=="M" or nomen[0]=="N" and artikel[2]== nomen[1] and nomen[1] == verb [0]:
					print (Fore.GREEN +"Der Satz ist korrekt!")
				elif artikel[1] == nomen[0] and artikel[2]== "F/P" and nomen[1] == verb [0]: 
					print (Fore.GREEN +"Der Satz ist korrekt!")
				else:
					print (Fore.RED + "Der Satz ist inkorrekt, weil die Wörter nicht kongruent sind!")
#unbekannte satzstruktur
		else:
			print (Fore.YELLOW+"Diese Satzstruktur kennen wir nicht.")
#regel für indexfehler
	except IndexError:
		if switch==0:
			print ("Oopps...Das gab es einen Fehler!")
		pass
###########
	print ("Willst du einen weiteren Satz testen?")
	eingabe= input(">>> ")
	if eingabe == "Ja":
		del artikel[:]
		del adjektiv[:]
		del nomen[:]
		del verb[:]
		del pronomen[:]
		print ("Dann gib einen weiteren Satz ein:")
		continue
	if eingabe == "Nein":
		print ("OK!")
		break
