import random as rd
startrom = "Soverom"
playerinput = input("Hva gjør du?\n skriv hær: ")

class Spiller:
    def __init__(self,poi = {}):
        self.poi = poi
        """Her finner man hjelp til hvordan man spiller"""
    def interact(self, poi):
        self.poi = poi


class Sener:
    def __init__(self,poi={},naborom = {}):
        self.poi = poi
        self.naborom = naborom 
    def adpoi(self, poi, beskrivelse):
        
        self.poi[poi] = beskrivelse

    def adpois(self, dic):
        for keys,beskrivelse in dic.items():
            self.adpoi(keys,beskrivelse) 
    def visInfo(self):
        print(self.poi)

    def go(self, rettning, naborom ={}):
        self.rettning = rettning
        self.naborom = naborom
        for i in naborom:
            if i.value() == "ingenting":
                print("Du går rett inni veggen, prøv å gå gjennom en dør istedet")
        
    def visRom(self, poi={}):
        self.poi = poi
        for i in poi:
            print(f"Du ser rundt i rommet. Det du legger merke til er {i}")
    def addnaboRom(self, naborom ):
        self.naborom=naborom

#start.adpoi("TV","Besrivelse av hva som er på tv-en")
soverompoi = {
    "Dør":"Det er en hvit dør sør i rommet for deg. Den ser åpen ut",
    
}
stuepoi = {
    "TV":"Besrivelse av hva som er på tv-en",
    "Stuebord":"Besrivelse av hva som ligger på stuebordet",
    "Terning":"Beskrivelse av terning på stuebordet"
}
kjøkkenpoi ={
    "Glass med melk":"Det står et halvfult glass med melk på kjøkkenbenken. Uvist om hvor lenge den har stått der",
    "Brød":"Brød",
}
badpoi = {
    "Tannbørste":"Det står en rosa jordan tannbørste oppi en gul kopp. Den ser litt sliten ut.",
    "Tannkrem":"Tannkremen ser helt flat ut. Får se om jeg klarer og presse ut for nokk til en dag til."
}
kottpoi = {
    "Gnom":"Det står en gnom mitt på rommet. Hvorfor står det en gnom midt på rommet. Den ser ikke snill ut."
}

soverom = Sener(soverompoi)
stue = Sener(stuepoi)
kjøkken = Sener(kjøkkenpoi)
kott = Sener(kottpoi)
bad = Sener(badpoi)


stuerom = {
    "n":soverom,
    "e":kjøkken,
    "s":kott,
    "w":bad
}
soverom = {
    "n":ingenting,
    "e":ingenting,
    "s":stue,
    "w":ingenting
}
kjøkkenrom = {
    "n":ingenting,
    "e":ingenting,
    "s":ingenting,
    "w":stue
}
kottrom = {
    "n":stue,
    "e":ingenting,
    "s":ingenting,
    "w":ingenting   
}
badrom = {
    "n":ingenting,
    "e":stue,
    "s":ingenting,
    "w":ingenting
}
#Fiender?
class gnom(object):     #Ikke bruk class.... sier hans
    name = "Gnomeo"
    health = 20
    strength = 3
    defence = 2
    loot = "Nøkkel#123" #?????


#pve rollespill uwu
def attack():
    print("Velg ditt angrep")
    valg = input("1. Normal attack \n2. Special attack \n3. Super attack \n (25% Success rate)")

    angrip = {"1":10,
        "2":20,         #ordbok?
        "3":50,
        "0":0}

    if valg == "1":
        angrep = "Normal attack"
        print("Du slår fienden")
        print(f"du bruker et {angrep}, fienden mister {angrip[valg]} liv og har igjen {gnom.health - angrip[valg]} liv")
    
    elif attack == "2":
        angrep = "special attack"
        print("Du sparker fienden")
        print(f"du bruker et {angrep}, fienden mister {angrip[valg]} liv og har igjen {gnom.health - angrip[valg]} liv")
    
    elif attack == "3":
        angrep = "super attack"
        print("Du løper mot fienden for å angripe alt du kan")
        sjanse = rd.randint(1,4)
        if sjanse != 4:
            print("Du slår og sparker fienden med en syk kombo")
            print(f"fienden mister 50 liv og har igjen {gnom.health - 50} liv")
        else:
            print("du dreit deg ut")
            valg = 0

    else:
        print("velg bare 1, 2 eller 3")
        attack()

    

