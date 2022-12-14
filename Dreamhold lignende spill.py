import random as rd
startrom = "Soverom"
class Spiller:
    """Skriv interact også tingen du vil interacte med og den vil gi den en beskrivelse av objecte"""
    def __init__(self,navn,nåverendeRom,):
        self.navn = navn
        self.nåverendreRom = nåverendeRom

        """Her finner man hjelp til hvordan man spiller"""
    def interact(self, poi):
        self.poi = poi
    def go(self):
        for noekkel, verdi in self.nåverendreRom.naborom.items():
            if verdi == None:
                pass
            else:
                print(f"Nøkkel: {noekkel}, verdi: {verdi.navn}.")
        retning=input("")
        if retning == "n" or retning =="e" or retning =="w"or retning =="s":
            self.nåverendreRom =  self.nåverendreRom.naborom[retning]
            print(f"Du har annkommet{spill.nåverendreRom.navn}")

 
        #todo
        """Bruke arv til å iverksette gnom battle
        class under sene class
        """




class Sener:
    """Skriv visInfo så vil det skrives ut alle tingene du kan gjøre noe med på rommet.
    Skriv Go også en rettning n,w,s,e for å bevege deg til en dør."""
    def __init__(self,navnpårom,poi={},naborom = {}):
        self.poi = poi
        self.naborom = naborom 
        self.navn = navnpårom
    def adpoi(self, poi, beskrivelse):
        
        self.poi[poi] = beskrivelse

    def adpois(self, dic):
        for keys,beskrivelse in dic.items():
            self.adpoi(keys,beskrivelse) 
        
        
    def visRom(self):
        for noekkel in self.poi.items():
            print(f"Du ser en{noekkel}")
    def addnaboRom(self, naborom ):
        self.naborom=naborom

#start.adpoi("TV","Besrivelse av hva som er på tv-en")
soverompoi = {
    "Dør":"Det er en hvit dør sør i rommet for deg. Den ser åpen ut",
    
}
stuepoi = {
    "TV":"Besrivelse av hva som er på tv-en.",
    "Stuebord":"Besrivelse av hva som ligger på stuebordet.",
    "Terning":"Beskrivelse av terning på stuebordet.",
    "Dør mot nord":"Denne døren går inn til soverommet.",
    "Dør mot øst":"Denne døren går inn til kjøkkenet.",
    "Dør mot sør":"Denne døren går inn til det mørke kottet.",
    "Dør mot vest":"Denne døren går inn til badet."
}
kjøkkenpoi ={
    "Glass med melk":"Det står et halvfult glass med melk på kjøkkenbenken. Uvist om hvor lenge den har stått der",
    "Brød":"Brød",
    "Dør mot vest":"Denne døren tar deg inn tilbake til stuen."
}
badpoi = {
    "Tannbørste":"Det står en rosa jordan tannbørste oppi en gul kopp. Den ser litt sliten ut.",
    "Tannkrem":"Tannkremen ser helt flat ut. Får se om jeg klarer og presse ut for nokk til en dag til.",
    "Dør til øst":"Denne døren tar deg inn tilbake til stuen"
}
kottpoi = {
    "Gnom":"Det står en gnom mitt på rommet. Hvorfor står det en gnom midt på rommet. Den ser ikke snill ut.",
    "Dør til nord":"Denne døre går inn tilbake til stuen."
}

soverom = Sener("soverom",soverompoi)
stue = Sener("stue",stuepoi)
kjøkken = Sener("kjøkken",kjøkkenpoi)
kott = Sener("kott",kottpoi)
bad = Sener("bad",badpoi)


stuerom = {
    "n":soverom,
    "e":kjøkken,
    "s":kott,
    "w":bad
}
soveromrom = {
    "n":None,
    "e":None,
    "s":stue,
    "w":None
}
kjøkkenrom = {
    "n":None,
    "e":None,
    "s":None,
    "w":stue
}
kottrom = {
    "n":stue,
    "e":None,
    "s":None,
    "w":None   
}
badrom = {
    "n":None,
    "e":stue,
    "s":None,
    "w":None
}
bad.addnaboRom(badrom)
stue.addnaboRom(stuerom)
soverom.addnaboRom(soveromrom)
kjøkken.addnaboRom(kjøkkenrom)
kott.addnaboRom(kottrom)

#Fiender?
class enemy:
    def __init__(self, name, health, strength, defence, loot):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.loot = loot
gnom = enemy("Gnomeo", 40, 3, 2, "Nøkkel1")

#pve rollespill
def gnomhelse():
    if enemy.health <= 0:
        print("Gnomeo er død")

"""def attack():
    print("Velg ditt angrep")
    valg = input("1. Normal attack \n2. Special attack \n3. Super attack \n (25% Success rate)")
    angrip = {"1":10,
        "2":20,       
        "3":50,
        "0":0}
    if valg == "1":
        angrep = "Normal attack"
        print("Du slår fienden")
        print(f"du bruker et {angrep}, fienden mister {angrip[valg]} liv og har igjen {gnom.health - angrip[valg]} liv")
        enemy.health = enemy.health - angrip[valg]
        gnomhelse()

    elif attack == "2":
        angrep = "special attack"
        print("Du sparker fienden")
        print(f"du bruker et {angrep}, fienden mister {angrip[valg]} liv og har igjen {gnom.health - angrip[valg]} liv")
        enemy.health = enemy.health - angrip[valg]
        gnomhelse()

    elif attack == "3":
        angrep = "super attack"
        print("Du løper mot fienden for å angripe alt du kan")
        sjanse = rd.randint(1,4)
        if sjanse != 4:
            print("Du slår og sparker fienden med en syk kombo")
            print(f"fienden mister 50 liv og har igjen {gnom.health - 50} liv")
            enemy.health = enemy.health - angrip[valg]
            gnomhelse()
        else:
            print("du dreit deg ut")
            valg = 0
            enemy.health = enemy.health - angrip[valg]
            gnomhelse()

    else:
        print("velg alternativ 1, 2 eller 3")
        attack()
if enemy.health <= 0: #Spesifisere fienden (gnom)
    print("Gnomeo pines og venter en smertefull og ikke heroisk død.\n LOL.\n Han er ley seg og vil hjem til hans mor og beelskede Juliet - Gnomeo og Juliet")
"""

def attack():
    while enemy.health > 0:
    
        print("Velg ditt angrep")
        valg = input("1. Normal attack \n2. Special attack \n3. Super attack \n (25% Success rate)")

        angrip = {"1":10,
            "2":20,       
            "3":50,
            "0":0}

        if valg == "1":
            angrep = "Normal attack"
            print("Du slår fienden")
            print(f"du bruker et {angrep}, fienden mister {angrip[valg]} liv og har igjen {gnom.health - angrip[valg]} liv")
            enemy.health = enemy.health - angrip[valg]
            gnomhelse()

        elif valg == "2":
            angrep = "special attack"
            print("Du sparker fienden")
            print(f"du bruker et {angrep}, fienden mister {angrip[valg]} liv og har igjen {gnom.health - angrip[valg]} liv")
            enemy.health = enemy.health - angrip[valg]
            gnomhelse()

        elif valg == "3":
            angrep = "super attack"
            print("Du løper mot fienden for å angripe alt du kan")
            sjanse = rd.randint(1,4)
            if sjanse != 4:
                print("Du slår og sparker fienden med en syk kombo")
                print(f"fienden mister 50 liv og har igjen {gnom.health - 50} liv")
                enemy.health = enemy.health - angrip[valg]
                gnomhelse()
            else:
                print("du dreit deg ut")
                valg = 0
                enemy.health = enemy.health - angrip[valg]
                gnomhelse()
        else:
            print("velg alternativ 1, 2 eller 3")


# her skjer spillet:
#navn=input("Hva heter du?\nSkriv inn her: ")
navn = "test"
spill = Spiller(navn,soverom)
print("Du våkner og ser deg rundt i romme ditt. Du kler på deg og står opp fra senga. Skriv help(Sener) eller (Spiller) for å få hjelp om hva du kan gjøre videre.")
gameend = False
while not gameend:
    spill.nåverendreRom.visRom()
    spillerinput = input("Hva vil du?\n 1. Interact\n 2. Gå til et annet rom\nSkriv inn hær:")
    if spillerinput == "1":
        print("Hva vil se se nermere på?")
        for i in spill.nåverendreRom.poi:
            print(i)
        spillerinput = input("")
        if spillerinput in spill.nåverendreRom.poi:
            print("test")
    if spillerinput == "2":
        print("Hvilken rettning vil du gå?")
        spill.go()

print("Spillet er over, dette var en Beta versjon")

if gnom.health <= 0:
    gameend = True

if gameend == True:
    print("GG's")