# Matthew Groenendijk
# 1034947
# BIM105

# Eerst moet er een welkoms bericht uitgestuurd worden met de informatie over de tarieven
print('Welkom bij het pretpark, hier is wat meer informatie over onze prijzen.\n')
print('Het regulier tarief indien je de kaarten ter plekke koopt is voor volwassenen €37.50 en voor kinderen €35.\n')
print('Bij online bestellen is het tarief voor volwassenen €35 en voor kinderen €28.50.\n')
print('Indien je een kortingspas hebt is het tarief voor volwassenen €30 en voor kinderen €25. Het tarief met een kortingspas geldt zowel bij aankoop ter plekke als online.\n')

# Dan wordt er gevraag of de kaarten online zijn besteld
while True:
    kaartenOnline = input('Zijn de kaarten online gekocht? (J/n) : ')
    if kaartenOnline == '' or not kaartenOnline[0].lower() in ['j', 'n']:
        print('Antwoord alsjeblieft met ja of nee!')
    else:
        break

# Er wordt gevraagd of er gebruik gemaakt is van een kortingspas
while True:
    metKortingspas = input(
        '\nIs er gebruik gemaakt van een kortingspas? (J/n) : ')
    if metKortingspas == '' or not metKortingspas[0].lower() in ['j', 'n']:
        print('Antwoord alsjeblieft met ja of nee!')
    else:
        break

# Er wordt gevraagd om hoeveel personen het gaat
aantalVolwassenen = int(input('\nOm hoeveel volwassenen gaat het? : '))

# En tot slot wordt er gevraagd om hoeveel kinderen het gaat
aantalKinderen = int(input('\nOm hoeveel kinderen gaat het? : '))

print('------------------------------------------------------')
# Dan wordt er gecheckt of de gebruiker ja heeft geantwoord
if kaartenOnline[0].lower() == 'j':
    # Dan wordt er gekeken of er een kortingspas aanwezig is
    # Als dit het geval is worden de prijzen aangepast naar 30 en 25 en wordt het totaal berekend
    if metKortingspas[0].lower() == 'j':
        totalePrijs = (aantalVolwassenen * 30) + (aantalKinderen * 25)
        # Het totaal bedrag wordt dan laten zien met de tekst dat het online gekocht is met een kortingspas
        print('Online gekocht met kortingspas:', totalePrijs)
    # Als er geen kortingspas aanwezig is worden de prijzen aangepast naar 35 en 28.50 en het totaal berekend
    elif metKortingspas[0].lower() == 'n':
        totalePrijs = (aantalVolwassenen * 35) + (aantalKinderen * 28.50)
        # Het totaal bedrag wordt dan laten zien met de tekst dat het online gekocht is zonder kortingspas
        print('Online gekocht:', totalePrijs)
    else:
        pass
# Er wordt gecheckt of de gebruiker dan nee heeft geantwoord op online kaarten
elif kaartenOnline[0].lower() == 'n':
    # Er wordt gecheckt of de kaarten dan wel een met kortingspas zijn gekocht
    if metKortingspas[0].lower() == 'j':
        # Als dit het geval is dan wordt de prijs aangepast naar 30 en 25 en wordt het totaal berekend
        totalePrijs = (aantalVolwassenen * 30) + (aantalKinderen * 25)
        # Het totaal bedrag wordt dan laten zien met daarbij de tekst of het ter plekke gekocht is met een kortingspas
        print('Ter plekke gekocht met kortingspas:', totalePrijs)
    # Dan wordt er gecheckt of de gebruiker de kaarten niet online gekocht heeft en ook niet met een kortingspas
    elif metKortingspas[0].lower() == 'n':
        # Als dit het geval is wordt de prijzen aangepast naar 37.50 en 35 en wordt het totaal berekend
        totalePrijs = (aantalVolwassenen * 37.50) + (aantalKinderen * 35)
        # Het totaal bedrag wordt dan laten zien met daarbij de tekst of het ter plekke gekocht zonder kortingspas
        print('Ter plekke gekocht:', totalePrijs)
    else:
        pass
# Als er mogelijk iets fout is gegaan wordt er een foutmelding laten zien
else:
    print('Er gaat iets fout')
