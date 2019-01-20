####lexikon######

neutra= ["Kind", "Auto", "Buch", "Schaf", "Schiff", "Lied", "Haus"]

feminina= ["Frau", "Mutter", "Studentin", "Gitarre", "Wolke"]

maskulina= ["Mann", "Vater", "Stundent", "Hof", "Stift"]

plurale= ["Kinder", "Autos", "Bücher", "Schafe", "Schiffe", "Lieder", "Häuser", "Frauen", "Mütter", "Studentinnen", "Gitarren", "Wolken", "Männer", "Väter", "Stundenten", "Höfe", "Stifte"]


###leere listen##
nomen=[]
artikel=[]
verb=[]
pronomen=[]

##defintionen###

def ARTIKEL(wort): 
	if wort[-1]=="r":
		artikel.append("M")
	elif wort[-1]== "s":
		artikel.append("N")
	elif wort[-1]== "e":
		artikel.append("F/P")


def PLURAL_A(wort):
	if wort[-1] == "e":
		artikel.append("F/P")
	else:
		artikel.append("S3/P2")

def NOMEN(wort): 
	if wort in maskulina:
		nomen.append("M")
	elif wort in neutra:
		nomen.append("N")
	elif wort in feminina:
		nomen.append("F/P")
	if wort in plurale:
		nomen.append("F/P")

def PLURAL_N(wort):
	if wort in plurale:
		nomen.append("F/P")
	else:
		nomen.append("S3/P2")



def VERB(wort): 
	if wort[-1] == "e":
		verb.append("S1")
	elif wort[-2] == "s" and wort[-1] == "t":
		verb.append("S2")
	elif wort[-1] == "t": 
		verb.append("S3/P2")
	elif wort[-1]== "n":
		verb.append("F/P")

def PRONOMEN(wort):
	if wort == "Ich":
		pronomen.append("S1")
	elif wort == "Du" or wort == "DU":
		pronomen.append("S2")
	elif wort == "Er"or wort == "Es":
		pronomen.append("S3/P2")
	elif wort == "Wir" or wort == "Sie":
		pronomen.append("F/P")
	elif wort == "Ihr":
		pronomen.append("S3/P2")


