#Za svaki film je poznat naziv, broj poz komentara i broj neg komentara.
#Kreiraj program koji štampa naziv filma sa najviše poz komentara
#Vratiti informacije o filmu koji počinje sa zadatim terminom term
#Vaš zadatak je da kreirate program kojim pronalazite fiml koji ima najbolji odnos između poz i neg komentara

l=[{'Naziv':'Godfather','PozKomentar':1000,'NegKomentar':1},
   {'Naziv':'Bladerunner','PozKomentar':500,'NegKomentar':30},
   {'Naziv':'A Beatiful Mind','PozKomentar':600,'NegKomentar':45}]

max_film={}
brpoz=0
term='God'
odnos=0
odnos_film={}
for film in l:
    if film['PozKomentar']>brpoz:
        max_film=film.copy()
    if film['Naziv'].startswith(term):
        print(f"Nadjen film koji počinje sa {term} \nFilm:{film}")
    if  (film['PozKomentar']/film['NegKomentar'])>odnos:
        odnos=film['PozKomentar']/film['NegKomentar']
        odnos_film=film.copy()

print (f"Film sa najviše poz komentara je :{max_film}")
print(f"Film sa najboljim odnosom pozitivnih i negativnih komentara je :{odnos_film}")