#Importerer random som rd. Bruker rd til å kaste terning og når man skal slås mot gnomen
import random as rd
# Importerer datetime sånn at jeg kan ta tiden
from datetime import datetime
# Når programmet startet får denne variabelen til verdien som klokka hadde når man startet programmet
start_time = datetime.now()
class Spiller:
    """Info om klassen spiller."""
    def __init__(self,navn,nåverendeRom,loot = 0):
        self.navn = navn
        self.nåverendreRom = nåverendeRom
        self.loot = loot
    def go(self):
        for noekkel, verdi in self.nåverendreRom.naborom.items():
            if verdi == None:
                pass
            else:
                print(f"Mulige rettninger å gå {noekkel} som følger deg til {verdi.navn}.")
        retning=input("")
        if retning == "n" or retning =="e" or retning =="w"or retning =="s":
            self.nåverendreRom =  self.nåverendreRom.naborom[retning]
            print(f"Du har annkommet {spill.nåverendreRom.navn}")
        #TODO

    def interact(self):
        for i in spill.nåverendreRom.poi:
            print(i)
        spillerinput = input("")
        for i in spill.nåverendreRom.poi:
            if spillerinput.lower() == i:
                print(spill.nåverendreRom.poi[i])
                break
        
        if spillerinput.lower() == "terning":
                spill.terning() 

        if spillerinput.lower() == "glass med melk" and spill.nåverendreRom == kjøkken:
            print("Vil du drikke melken eller ikke?")
            spørsemål = input("Ja eller nei? \nsvar: ")
            if spørsemål.lower() == "ja":
                spill.melk()
        elif spillerinput.lower() in spill.nåverendreRom.poi:
            return
        if spillerinput.lower() =="glass med melk":
            return
        if spillerinput.lower() == "gnom":
            
            pass
        else:
            print("Du må skrive inn en av objektene over.\nPrøv igjen ")
            spill.interact()
    
    def terning(self):
        side = rd.randint(1,6)
        print(f"den landet på {side}")
    def melk(self):
        print("Hvorfor gjore jeg det. Faen jeg må spy")
        print("Du springer innpå badet og spyr i doen. Deretter trekker du opp.")
        self.nåverendreRom = bad


class Sener:
    """Info om classen Sener."""
    def __init__(self,navnpårom,poi={},naborom = {}):
        self.poi = poi
        self.naborom = naborom 
        self.navn = navnpårom
        
    def visRom(self):
        for objekt in self.poi:
            print(f"Du ser {objekt}.")

    def addnaboRom(self, naborom ):
        self.naborom=naborom
    
    def hjelp(self):
        print("I dette spillet kan du utforke et hus fra rom til rom.")
        print("Velg endten interact, hvor vil du gå? eller se rom.")
        print("Interact tar opp en liste med ting du kan se nermere på.")
        print("Gå til et annet rom gir deg en meny med rettninger som du kan gå og de vil ta deg til et nytt rom.")
        print("Når man ankommer ett nytt rom vil det komme opp tekst med alle de intresange objektene i rommet, om du er uheldig og ikke får det med deg kan du bruke se rom.")
        print("Dette vil gjenta det som sto når du først kom inn i rommet. Lykke til! :)")
    
#start.adpoi("TV","Besrivelse av hva som er på tv-en")
soverompoi = {
    "dør":"Det er en hvit dør sør i rommet for deg. Den ser åpen ut.",
    "vindu":"Du ser ut vinduet, det snør. Snøen daler elegant ned og lander forskigtig på plenen, desto lengere du ser, jo mer av plenen blir dekket i snø.",
    "drikkeflaske":"Det står en halvfull drikkeflaske med vann på nattborde ditt. Du våkner alltid midt på natten og føler deg tørr i munnen, så dette er din løsning på dette.",
    "klær":"Det ligger en haug med klær på en stol du har i hjørnet av rommet. Har alle det tenker du til deg selv. (Alle har det. Ikke tenk på det).",
    
}
stuepoi = {
    "tv":"Du ser at Tv-en står på. Friends. Hvem søren putta på den driten? Det er ikke så bra som alle skulle ha det til tenker du for deg selv.",
    "stuebord":"Det ligger noen aviser på stuebordet. Det står med stor rød skrift NOAH HAR BLITT PÅKJØRT. (Overasket om du tar denne referansen Hans).",
    "terning":"Jeg elsker å kaste terninger. Du kastet terningen",
    "dør mot nord":"Denne døren går inn til soverommet.",
    "dør mot øst":"Denne døren går inn til kjøkkenet.",
    "dør mot sør":"Denne døren går inn til det mørke kottet.",
    "dør mot vest":"Denne døren går inn til badet."
}
kjøkkenpoi ={
    "glass med melk":"Det står et halvfult glass med melk på kjøkkenbenken. Uvist om hvor lenge den har stått der",
    "brød":"Brød",
    "dør mot vest":"Denne døren tar deg inn tilbake til stuen."
}
badpoi = {
    "tannbørste":"Det står en rosa jordan tannbørste oppi en gul kopp. Den ser litt sliten ut.",
    "tannkrem":"Tannkremen ser helt flat ut. Får se om jeg klarer og presse ut for nokk til en dag til.",
    "dopapir":"Det ser ut som jeg må kjøpe mer dopapir. Begynner å gå tom.",
    "dør til øst":"Denne døren tar deg inn tilbake til stuen"
}
kottpoi = {
    "gnom":"Det står en gnom mitt på rommet. Hvorfor står det en gnom midt på rommet. Den ser ikke snill ut.",
    "dør til nord":"Denne døre går inn tilbake til stuen.",
    "kniv":"Det ligger en komisk stor kniv bak gnomen. Hvordan kom den seg dit? Må ha vært King Bach."
}

soverom = Sener("soveromet",soverompoi)
stue = Sener("stua",stuepoi)
kjøkken = Sener("kjøkkenet",kjøkkenpoi)
kott = Sener("kottet",kottpoi)
bad = Sener("badet",badpoi)


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
    def __init__(self, name, health, strength, defence):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence

gnom = enemy("Gnomeo", 40, 3, 2,)

#pve rollespill
def gnomhelse():
    if enemy.health <= 0:
        print("Gnomeo er død")
        print("Han slapp noe skinner og ligger på bakken bak han") #Her kan nøkkel ligg eller nokka sånt

def attack():
    while enemy.health > 0:
    
        print("Velg ditt angrep")
        valg = input("1. Normal attack \n2. Special attack \n3. Super attack \n (25% Success rate)")

        angrip = {"1":10,
            "2":20,       
            "3":50,
            "0":0,
            }

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
print("Du våkner og ser deg rundt i romme ditt. Du kler på deg å står opp fra senga. Skriv hjelp for å få hjelp om hva du kan gjøre videre.")
gameend = False
spill.nåverendreRom.visRom()
while not gameend:

    spillerinput = input("Hva vil du nå?\n1. Interact\n2. Gå til et annet rom\n3. Se rom\nSkriv inn hær: ")

    if spillerinput == "1":
        print("Hva vil se se nermere på?")
        spill.interact()
    if spillerinput == "2":
        print("Hvilken rettning vil du gå?")
        spill.go()
    if spillerinput == "3":
        spill.nåverendreRom.visRom()
    if spillerinput == "hjelp":
        soverom.hjelp()

#Hær får en ny variabel verdien til klokkeselttet når koden har kommet seg hit til slutten
end_time = datetime.now()
#Hær regner den ut hvor mye tid du har brukt på å spille ferdig dette spillet
print('Duration: {}'.format(end_time - start_time))