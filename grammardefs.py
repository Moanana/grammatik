def VAFIN(word): #mit dieser funktion wird dem verb numerus zugewiesen
#VAFIN = word[1] #hiermit bekommt man den zweiten teil des pos-tags, also das verb 
länge= len(word)
if VAFIN[länge-1] = "t": # wenn der letzte buchstabe des verbs ein "t" ist, weise verb das Merkmal "S" zu.
	verb = []
	append.verb[S]
if VAFIN[länge-1] = "n":
	verb= []
	append.verb[P] # das ergibt dann verb=[P]


def NN: #mit dieser funktion wird dem nomen genus zugewiesen
NN = word[1] 
if NN = Hund or Mond or Schuh or Tisch:
	nomen = []
	append.nomen[M]
if NN = Tier or Schiff or Spiel or Gerät:
	nomen=[]
	append.nomen[N]
if NN = Kasse or Straße or Küche or Sache:
	nomen= []
	append.nomen[F]
.
.
.
länge = len[NN] #hiermit wird dem nomen numerus zugewiesen
if NN[länge-1] = "e":
	append.nomen[P]
else:
	append.nomen[S] # das ergibt dann z.b. nomen=[F, S]

def PDS: #hier wird den artikeln genus zugewiesen
PDS = wort[1]
if PDS = der or dieser or welcher or jener:
	artikel = []
	append.arikel[M]
if NN = das or dieses or welches or jenes:
	nomen=[]
	append.nomen[N]
if NN = die or diese or welche or jene:
	nomen= []
	append.nomen[F]
.
.
.
länge = len[PDS] #hier wird den artikeln numerus zugewiesen
if PDS[länge-1] = "e":
	append.artikel[P]
else:
	append.nomen[S] # das ergibt dann z.b. artikel=[F, S]

