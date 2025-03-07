#############################
####### INTRODUKTION ########
#############################

Hver mappe i denne uge indeholder mine skripter for opgaveløsningerne for de individuelle opgaver. 

** Jeg erklarer herved, at jeg har løst opgaven uden anden støtte end en basis internetforbindelse til at finde funktionsbeskrivelse. 
** Alle skript i denne mappe og disses undermapper er udarbejdet udelukkende af undertegnede, Alexander Kruhøffer Bloch Andersen. 

#########################################
###### OPGAVE 1 - intro til python ######
#########################################
 
I mappen "opgave_1-intro_til_python" finder du filerne "opgave_1.py", som fremover vil blive henvist til som skriptet i denne sektion. , og "Navne_liste.txt", som fremover vil blive henvist til som navneliste-filen i denne sektion. 

py-filen indeholder mit skript, som løsning på opgaven. 

Den kan køres som et almindeligt skript i et redigeringsprogram, som spyder, eller i en kommando propt, såsom mobaxterm. 
# OBS! for at skriptet kan køre, kræver det at brugeren har installeret pakkerne 'matplotlib' og 'os' på forhånd. 

Når skriptet køres, vil brugeren blive spurgt om filen, som skal analyseres og skal skrives i terminalen. 
# OBS! for enkelthedens skyld anbefales det at køre skriptet i/fra samme mappe, som navneliste-filen. Alternativt skal hele stien til navneliste-filen angives her. 

Når skriptet kører, vil navnene i navneliste-filen blive printet ud i terminalen i alfabetisk rækkefølge. Efterfølgende vil der i terminalen blive skrevet: 
	Job is Done!
Dette er tegn på at skriptet er gennemkørt. 


Når Skriptet er færdig med at køre, vil der i samme mappe som skriptet være genereret 4 filer: 
	1) 'Sorted_Names.txt'. Denne fil indeholder en liste over alle navnene fra den anvendte navneliste-fil sorteret alfabetisk
	2) 'Name_Statistics.csv'. Denne fil indeholder de samlede statistikker for alle navnene i navneliste-filen:
		a) gennemsnits navnelængden
		b) den maksimale navnelængde
		c) den minimale navnelængde
		d) navnelængden ved 25% kvantilen
		e) median navnelængden
		f) navnelængden ved 75% kvantilen
		g) frekvensen over alle bogstaverne i alle navnene i navneliste-filen. 
	3) 'name_statistics.png'. Et billede af et enkelt søjlediagram over punkt 2a-f fra 'Name_Statistics.csv' filen
	4) 'name_letter_frequency.png' Et billede af et enkelt søjlediagram over punkt 2g fra 'Name_Statistics.csv' filen.

# OBS! Når skripet har kørt, anbefales det at gemme de nyligt genererede (tekst)filer, da en ekstra kørsel af skriptet vil overskrive tekstfilerne. 

#######################################
###### OPGAVE 2 - logfil analyse ######
#######################################

I mappen "opgave_2-logfil_analyse" finder du filerne "opgave_2.py", som fremover vil blive henvist til som skriptet i denne sektion, og "app_log (logfil analyse) - random.txt", som fremover vil blive henvist til som log-filen i denne sektion. 

py-filen indeholder mit skript, som løsning på opgaven. 

Den kan køres som et almindeligt skript i et redigeringsprogram, som spyder, eller i en kommando propt, såsom mobaxterm. 

Når skriptet køres, vil brugeren blive spurgt om filen, som skal analyseres og skal skrives i terminalen. 
# OBS! for enkelthedens skyld anbefales det at køre skriptet i/fra samme mappe, som log-filen. Alternativt skal hele stien til log-filen angives her. 

Når skriptet kører, vil det skrive i terminalen at visse filer er dannet ("X successfully created!"), hvilket indikere at de sorterede log-filer er blevet lavet. 

Skriptet vil generere 4 .txt-filer baseret på log-filens navn, som vil betegnes her som X:
	1) 'X_warnings.txt' : Denne fil indeholder alle advarselsmeddelelser, angivet ved tilstedeværelsen af ordet "WARNING"
	2) 'X_errors.txt'   : Denne fil indeholder alle fejlmeddelelser, angivet ved tilstedeværelsen af ordet "ERROR"
	3) 'X_successes.txt': Denne fil indeholder alle succesmeddelelser, angivet ved tilstedeværelsen af ordet "SUCCESS"
	4) 'X_info-logs.txt': Denne fil indeholder alle andre meddelelser, som ikke er angivet på de førhenværende måder. 


############################################
###### OPGAVE 3 - kort fejlhåndtering ######
############################################

I mappen "opgave_3-kort_fejlhåndtering" finder du filerne "opgave_3.py", som fremover vil blive henvist til som skriptet i denne sektion, og "source_data.csv", som fremover vil blive henvist til som det rå data. 

py-filen indeholder mit skript, som løsning på opgaven. 

Den kan køres som et almindeligt skript i et redigeringsprogram, som spyder, eller i en kommando propt, såsom mobaXterm. 
## OBS! Skriptet kræver pakkerne re og os for at kunne køre. 
## OBS! Filen med det rå data er hårdt kodet ind i skriptet, så det er vigtigt at det rå data er i samme mappe som skriptet. 

Når skriptet kører, vil det gå direkte igang med at analysere og rengører det rå data. 
Imens skriptet kører, vil det give en række advarsler ang. data:
	**advarselsmeddelelse**									**håndtering**
	WARNING CODE 01: Name of <user> Insufficient! Replaced with Local Part of E-mail	brugernavn udtrækkes fra den lokale del af E-mail addressen.
	WARNING CODE 02: E-mail for User: <user> Not Sufficient!				E-mail addressen erstattes med "INSUFFICIENT_DATA"
	WARNING CODE 03: E-mail for User: <user> Not Found!					E-mail addressen erstattes med "DATA_NOT_FOUND"
	WARNING CODE 04: Purchase for user: <user> At E-mail: <email> is Negative!		beløbet beholdes i det rensede datasæt
	WARNING CODE 05: No Purchase for user: <user> At E-mail: <email> Found!			beløbet erstattes med "DATA_NOT_FOUND"
	WARNING CODE 06: No Name Provided for <line>						købet med bruger og email fjernes fra datasættet

Når skriptet er færdig med at køre, vil der være en ny fil i arbejdsmappen. Denne fil vil hedde "cleaned_source_date.csv". Denne fil vil indholde de rensede data. 
## OBS! hvis skriptet køres en gang til lige bagefter uden denne fil bliver håndteret, vil denne fil blive slettet og erstattet med en ny version af samme navn.



###############################
###### OPGAVE 4 - pandas ######
###############################

I mappen "opgave_4-pandas" finder du filerne "opgave_4.py", som fremover vil blive henvist til som skriptet i denne sektion, og "DKHousingPricesSample100k.csv", som fremover vil blive henvist til som dataarket. 

py-filen indeholder mit skript, som løsning på opgaven. 

Den kan køres som et almindeligt skript i et redigeringsprogram, som spyder, eller i en kommando propt, såsom mobaXterm. 
## OBS! Skriptet kræver pakkerne matplotlib, numpy og pandas for at kunne kører 
## OBS! filen med Dataarket er hårdt kodet ind i skriptet, så det er vigtigt at dataarket er i samme mappe som skriptet. 

Når skriptet kører, vil det først printe de første 10 rækker af dataarket. 
Når skriptet er færdig med at køre, vil der være 4 png-filer i samme mappe som skriptet. 
Disse png-filer er plots, som er generet over gennemsnitshuspriserne. 

