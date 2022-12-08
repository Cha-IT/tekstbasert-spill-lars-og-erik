import random as rd

N = "North"
W = "West"
S = "South"
E = "East"

posisjonx = 0
posisjony = 0

class Spill:
    def __init__(self,startsene):    
        self.sene=startsene
        """Her finner man hjelp til hvordan man spiller"""
    def visRom(self):
        print("")
    def go(self, rettning):
        pass
    def interact(self, poi):
        pass


class Sener:
    def __init__(self ):
        self.poi = {}
    def adpoi(self, poi, beskrivelse):
        
        self.poi[poi] = beskrivelse

    def adpois(self, dic):
        for keys,beskrivelse in dic.items():
            self.adpoi(keys,beskrivelse) 
    def visInfo(self):
        print(self.poi)

start=Sener()
#start.adpoi("TV","Besrivelse av hva som er på tv-en")
stuepoi = {
    "TV":"Besrivelse av hva som er på tv-en",
    "Stuebord":"Besrivelse av hva som ligger på stuebordet"
}

start.adpois(stuepoi)
start.visInfo()


#Fiender?
class gnom(object):
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
        "3":50}

    if valg == "1":
        angrep = "Normal attack"
        print("Du slår fienden")
        print(f"Fienden mister 10 liv og har igjen {gnom.health - 10} liv")
    
    elif attack == "2":
        angrep = "special attack"
        print("Du sparker fienden")
        print(f"fienden mister 20 liv og har igjen {gnom.health - to} liv")
    
    elif attack == "3":
        angrep = "super attack"
        print("Du løper mot fienden for å angripe alt du kan")
        sjanse = rd.randint(1,4)
        if sjanse == 1 or sjanse == 2 or sjanse == 3:
            print("Du slår og sparker fienden med en syk kombo")
            print(f"fienden mister 50 liv og har igjen {gnom.health - tre} liv")
        else:
            print("du dreit deg ut")
    

    

