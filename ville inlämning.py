import random
print('-----------------------------------')
print('Välkommen till sten/sax/påse spelet')
print('-----------------------------------')
loop1=1
while loop1==1: #vi satte en variabel istället för while true och break enligt Alinas rekommendation, denna loop säkerställer att användaren väljer ett positivt heltal
    try:
        vinnandepoang=int(input('Välj hur många poäng som behövs för att vinna: ')) #användaren bestämmer hur många poäng krävs det att vinna
    except ValueError: 
        print()
        print('Du måste välja ett heltal!')
        print()
    else:
        if vinnandepoang<=0:
            print()
            print ('Du måste välja ett heltal!')
            print()
        else:
            print()
            print('Ditt svar har sparats')
            print()
            loop1=0
totala_poang_spelare=0 #basvärden för spelarens poäng
totala_poang_dator=0 #basvärden för datorns poäng
def runda(spelarens_poang,datorns_poang):
    print('*****************************************')
    print()       
    while True: #denna loop säkerställer att användaren väljer ett av alternativen
        try:
            spelarens_val=int(input('Gör ditt val av följande alternativ: \n 1:Sten \n 2:Sax \n 3:Påse\n Ditt val: '))
            print()   
        except ValueError:
            print()
            print('Du måste välja ett av alternativen!')
            print()
        else:
            if spelarens_val>3 or spelarens_val<1:
                print('Du måste välja ett av alternativen!')
                print()
            else:
                datorns_val=random.randint(1,3) #Datorn generarar ett slumpmässig tal mellan 1 till 3 dvs sten, sax eller påse.
                resultat_runda=checkResults(spelarens_val,datorns_val)
                if resultat_runda=='spelaren_vann':# kollar att vem vann och returnerar ett värde enligt det
                    return 1
                elif resultat_runda=='datorn_vann':
                    return -1
                else:
                    return 0
        
def checkResults(user,computer):# funktion checkResults jämför användares val till datorns val och sedan anger vem vann
    if user==1:
        if computer==2:
            print('Du valde sten, datorn valde sax, du vann')
            return 'spelaren_vann'
        elif computer==1:
            print('Båda valde sten, det blir oavgjort')
            return 'oavgjort'
        else:
            print('Du valde sten, datorn valde påse,datorn vann')
            return 'datorn_vann'
    elif user==2:
        if computer==3:
            print('Du valde sax, datorn valde påse, du vann')
            return 'spelaren_vann'
        elif computer ==1:
            print('Du valde sax, datorn valde sten, datorn vann')
            return 'datorn_vann'
        else:
            print('Båda valde sax, det blir oavgjort')
            return 'oavgjort'
    else:
        if computer==1:
            print('Du valde påse, datorn valde sten, du vann')
            return 'spelaren_vann'
        elif computer==3:
            print('Båda valde påse, det blir oavgjort')
            return 'oavgjort'
        else:
            print('Du valde påse, datorn valde sax,datorn vann')
            return 'datorn_vann'

while True: #denna loop kör runda-funktionen och tar resultatet och gör olika saker på basen av vem som vann, när någons poäng uppnår vinnande kravet avbryts loopen
    resultat_runda=(runda(totala_poang_spelare,totala_poang_dator)) #kollar värdet som returneras av runda funktionen och gör olika saker på basen av det
    if resultat_runda==1:
        totala_poang_spelare+=1
        print()
        print('Ställningen är: \nspelare:',totala_poang_spelare,'\ndator:',totala_poang_dator)
        print()
        if totala_poang_spelare==vinnandepoang:
            print()
            print('******************')
            print('Ställningen blev:\nspelare:',totala_poang_spelare,'\ndator:',totala_poang_dator,'\n \nSpelaren vann spelet!')
            print('******************')
            print()
            break
    elif resultat_runda==-1:
        totala_poang_dator+=1
        print()
        print('Ställningen är: \nspelare:',totala_poang_spelare,'\ndator:',totala_poang_dator)
        print()
        if totala_poang_dator==vinnandepoang:
            print()
            print('******************')
            print('Ställningen blev:\nspelare:',totala_poang_spelare,'\ndator:',totala_poang_dator,'\n \nDatorn vann spelet!')
            print('******************')
            print()
            break
    else:
        print()
        print('Ställningen är: \nspelare:',totala_poang_spelare,'\ndator:',totala_poang_dator)
        print()
