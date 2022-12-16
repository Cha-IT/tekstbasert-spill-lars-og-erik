#Det er viktig at du killer terminalen når du vil restarte game.
#Importerer random som rd. Bruker rd til å kaste terning og når man skal slås mot gnomen
import random as rd
# Importerer datetime sånn at jeg kan ta tiden
from datetime import datetime
#Jeg tar en input fra spilleren for å se hvilken modus han vil spille
modus = input("Hvilke modus vil du spille i?\n1. vanlig \n2. speedrun modus\nSkriv inn hær: ")
#Dette er en funsjon som jeg laget for å skape mellom rom mellom tekstene så det blir enklere og lese all teksten som kommer opp på engang.
def clear():
    for i in range(10):
        print(" ")

if modus == "2":
    # Når programmet startet får denne variabelen til verdien som klokka hadde når man startet programmet
    start_time = datetime.now()
if modus == "1":
    #siden det ikke skjer noe om han velger 1 eller noe annet så vil koden alltid være på vanlig modus med mindre de skriver 2
    print("Hærlig")

#Dette er classen spiller. Den har egenskapene til navnet på spilleren og det nåverende rommet til spilleren.
class Spiller:
    """Info om klassen spiller."""
    def __init__(self,navn,nåverendeRom):
        self.navn = navn
        self.nåverendreRom = nåverendeRom
    def go(self):
        #Her er funksjonen som lar deg gå fra rom til rom. Den ser på naborommene som er i romme du er i nå og ser hvilke det er mulige å gå til. Om det er noen som det er mulige å gå til vil den si hvilken himmel rettning og hvor den døren tar deg
        for noekkel, verdi in self.nåverendreRom.naborom.items():
            if verdi == None:
                pass
            else:
                print(f"Mulige rettninger å gå {noekkel} som følger deg til {verdi.navn}.")
                
        retning=input("")
        if retning == "n" or retning =="e" or retning =="w"or retning =="s":
            self.nåverendreRom =  self.nåverendreRom.naborom[retning]
            print(f"Du har annkommet {spill.nåverendreRom.navn}")


        #Funksjonen som lar deg se beskrivelsen på ting
    def interact(self):
        #her får du opp alle tingene du kan se  nermere på i en liste med hjelp av en for løkke
        for i in spill.nåverendreRom.poi:
            print(i)
        spillerinput = input("")
        clear()
        #om det du skrev inn finns i ordboken så vil den skrive ut beskrivelsen til den nøkkelen
        for i in spill.nåverendreRom.poi:
            if spillerinput.lower() == i:
                print(spill.nåverendreRom.poi[i])
                break
        #Jeg lagg til disse for spiessiele ting som skjer når man ser nermere på spesefike ting slik som terningen, melke glasset og gnomen
        if spillerinput.lower() == "terning":
                spill.terning() 
        
        if spillerinput.lower() == "glass med melk" and spill.nåverendreRom == kjøkken:
            print("Vil du drikke melken eller ikke?")
            spørsemål = input("Ja eller nei? \nsvar: ")
            if spørsemål.lower() == "ja":
                #Om du tar ja vil spilleren springe inn til badet for å spy. Som endrer det nåverende rommet til spilleren og posisjonen deres.
                spill.melk()

        if spillerinput.lower() == "gnom" and spill.nåverendreRom == kott:
            print("gnomen kaller moren din for noen frekke ting og forbreder seg til å slåss mot deg")
            #Om du ser nermere på gnomen vil dere komme i en duell, litt som pokemon. Med hjelp av funksjonen attack
            attack()
            return

        elif spillerinput.lower() in spill.nåverendreRom.poi:
            return
        # her måtte jeg legge til en spesefik løsning for glass med melk. FOrdi nå spilleren springer fra kjøkkenet til badet vil fortsatt tingen de valgte være en ting som bare er i kjøkkenet og nå er de i badet.
        #Så det ville stå at de måtte velgge noe fra badet. Så jeg lagg inn denne sånn at det ikke skulle bli sånn.
        if spillerinput.lower() =="glass med melk":
            return
        else:
            print("Du må skrive inn en av objektene over.\nPrøv igjen ")
            spill.interact()
    #funksjon som kaster terning
    def terning(self):
        side = rd.randint(1,6)
        print(f"den landet på {side}")
    def melk(self):
        print("Hvorfor gjore jeg det. Faen jeg må spy")
        print("Du springer innpå badet og spyr i doen. Deretter trekker du opp.")
        self.nåverendreRom = bad
#klassen sener
class Sener:
    """Info om classen Sener."""
    #Den holder på informasjonen på navnet på rommet, ting som er interesanne på rommet og naborommene
    def __init__(self,navnpårom,poi={},naborom = {}):
        self.poi = poi
        self.naborom = naborom 
        self.navn = navnpårom
        
    def visRom(self):
        #viser rommet og sier alle de interessane objektene
        for objekt in self.poi:
            print(f"Du ser {objekt}.")

    def addnaboRom(self, naborom ):
        #Bruker denne for å legge til naborom til objektene
        self.naborom=naborom
    
    def hjelp(self):
        #skal hjelpe spilleren med tingene man kan gjøre
        print("I dette spillet kan du utforke et hus fra rom til rom.")
        print("Velg endten interact, hvor vil du gå? eller se rom.")
        print("Interact tar opp en liste med ting du kan se nermere på.")
        print("Gå til et annet rom gir deg en meny med rettninger som du kan gå og de vil ta deg til et nytt rom.")
        print("Når man ankommer ett nytt rom vil det komme opp tekst med alle de intresange objektene i rommet, om du er uheldig og ikke får det med deg kan du bruke se rom.")
        print("Dette vil gjenta det som sto når du først kom inn i rommet. Lykke til! :)")
    
#Her er ordbøkene med alle points of interest til alle rommene som blir lagt til objektene når de lages
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
    "brød":"Det ligger brød på kjøkken benken. Det ser ut som om noen har tatt en bit rett ut ifra brødskiva istede for å skjere den opp. Merkene på brødskiven ser veldig likt ut til gnome tenner tenker du for deg selv. Ikke spørr hvorfor du veit det.",
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
#Her lager vi objektene
soverom = Sener("soveromet",soverompoi)
stue = Sener("stua",stuepoi)
kjøkken = Sener("kjøkkenet",kjøkkenpoi)
kott = Sener("kottet",kottpoi)
bad = Sener("badet",badpoi)

#Her skriver jeg hvor rommene er i forhold til hverandre så man vet hvor man kan gå når man er i et rom.
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
#Naborommene legges til i objektene med hjelp av funksjonen vi lagde i sener
bad.addnaboRom(badrom)
stue.addnaboRom(stuerom)
soverom.addnaboRom(soveromrom)
kjøkken.addnaboRom(kjøkkenrom)
kott.addnaboRom(kottrom)


#klasse for fiender. Regen er health regen som betyr hvor mye fienden healer etter hvert trekk
class enemy:
    def __init__(self, name, health, regen):
        self.name = name
        self.health = health
        self.regen = regen
#lager objektet
gnom = enemy("Gnomeo", 80, 7)

#Det som kommer opp når fienden dør. en funksjon
def gnomhelse():

    if gnom.health <= 0:
        print("Gnomeo pines og venter en smertefull og ikke heroisk død.\n LOL.\n Han er ley seg og vil hjem til hans mor og beelskede Juliet - Gnomeo og Juliet")


def attack():
    #Denne funksjonen kjøres når man ser nermere på gnomen, dette er hele fighting simmen i spillet. Her bruker jeg objektet spiller sitt navn til å prite navnet, men jeg kunne også bare bruke navn men dette er kulere og viser kompetanse i klasser og hvordan man bruker det i python
    print(f"Gnomeo: Hei {spill.navn} jeg har ventet på deg. Slåss mot meg til døden.")
    while gnom.health > 0:
        print("Velg ditt angrep")
        valg = input("1. Normal attack \n2. Special attack \n3. Super attack \n (25% Success rate)")
        #Man kan velge forskjellige angrep som gjør forskjellig skade 

        angrip = {"1":10,
            "2":20,       
            "3":50,
            "0":0,
            }

        if valg == "1":
            angrep = "Normal attack"
            print("Du tar kniven i kottet og stikker gnomen i foten")
            print(f"du bruker et {angrep}, fienden mister {angrip[valg]} liv og har igjen {gnom.health + gnom.regen - angrip[valg]} liv")
            gnom.health = gnom.health + gnom.regen - angrip[valg]
            gnomhelse()

        elif valg == "2":
            angrep = "special attack"
            print("Du tar kniven og slår stikker han i øret")
            print(f"du bruker et {angrep}, fienden mister {angrip[valg]} liv og har igjen {gnom.health+ gnom.regen - angrip[valg]} liv")
            gnom.health = gnom.health + gnom.regen - angrip[valg]
            gnomhelse()

        elif valg == "3":
            angrep = "super attack"
            print("Du tar kniven og forbreder deg til å angripe")
            sjanse = rd.randint(1,4)
            if sjanse != 4:
                print("Du stikker den komeiske store kniven gjennom gnomen. Han hyler i smerte.")
                print(f"fienden mister 50 liv og har igjen {gnom.health + gnom.regen - angrip[valg]} liv")
                gnom.health = gnom.health + gnom.regen - angrip[valg]
                gnomhelse()
            else:
                print(f"Gnomen beveget seg i siste sekund og du bommet. Han flirer og tar en backflip. Ikke denne gangen {spill.navn} ")
                valg = "0"
                gnom.health = gnom.health + gnom.regen - angrip[valg]
                gnomhelse()
        else:
            print("velg alternativ 1, 2 eller 3")


# her skjer spillet:
#Spør om navnet til spilleren
navn=input("Hva heter du?\nSkriv inn her: ")
#lager spiller objektet
spill = Spiller(navn,soverom)
print("Du våkner og ser deg rundt i romme ditt. Du kler på deg å står opp fra senga. Skriv hjelp for å få hjelp om hva du kan gjøre videre.")
# gameend er det som får while løkken med input som spør spilleren om hva man skal gjøre til å ikke slutte.
gameend = False
spill.nåverendreRom.visRom()
while not gameend:
    #Her kommer det valgmeny om hva man kan gøre. Alle disse valgene har en egen funksjon i klassene som blir kjørt.
    spillerinput = input("Hva vil du nå?\n1. Interact\n2. Gå til et annet rom\n3. Se rom\nSkriv inn hær: ")
    if spillerinput == "1":
        clear()
        print("Hva vil se se nermere på?")
        spill.interact()
    if spillerinput == "2":
        clear()
        print("\nHvilken rettning vil du gå?")
        spill.go()
    if spillerinput == "3":
        clear()
        spill.nåverendreRom.visRom()
    if spillerinput == "hjelp":
        clear()
        soverom.hjelp()
    if gnom.health <= 0:
        #når dette skjer så har man slått spillet fordi gameend blir true og whike løkken slutter
        clear()
        gameend = True
print("Du finner en pokal i gnomes enorme sekk")
print("Litt rart at gnomen vill kjempe til døden. Han sto der jo bare og ble slått, han slo aldri tilbake. Nokk om det tenker du mens du ser din smilende refleksjon i pokalen.")
print("GG! Du vant og fortsatte dagen din som om det var en helt vanelig dag.")
print("Takk for at du spilte. Dette er en beta versjon så stay tuned. :3 OwO")
if modus == "2":
    #Hær får en ny variabel verdien til klokkeselttet når koden har kommet seg hit til slutten
    end_time = datetime.now()
    #Hær regner den ut hvor mye tid du har brukt på å spille ferdig dette spillet
    print("Tid brukt: {}".format(end_time - start_time))
if modus == "1":
    print("prøv speedrun modus neste gang :)")
#Håper dere liker spillet.