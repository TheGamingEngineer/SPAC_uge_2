import re
import os

try:
    data=open("source_data.csv","r")
except FileNotFoundError as e:
    print(f"File not found: {e}. Either the filename has been given erroneously, path to file has not been provided when needed, or file simply does not exist!")
except PermissionError as e:
    print(f"Permission denied: {e}. Please change permissions of the file and try again.")
except IsADirectoryError as e:
    print(f"Expected a file but found a directory: {e}. This script only handles text-files.")
except OSError as e:
    print(f"OS error: {e}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}.")
    

cleaned=[]
n=1
for line in data:
    if "name" in line.lower():
        cleaned.append(line)
        continue
    
    Line=line.split(",")[1:]
    
    ## hvis linjen er tom, springes den iteration over. 
    if "".join(Line)=="\n":
        continue
    
    for x in Line:
        if re.match(r"[A-Za-z]+[0-9]+",x) and "@" not in x:
            continue
        
        ## er der match for et for- og efternavn, renses det for alle mellemrum, som ikke er herimellem og dette gemmes. 
        if re.match(r"[A-Za-z]+ [A-Za-z]+",x):
            name=re.sub(r"\s+(?=\S)","",x)
            name=re.sub(r'([a-z])([A-Z])',r'\1 \2',name)
        ## Hvis der ikke er givet et for- eller efternavn, udtrækkes dette fra E-mail addressen, hvis den er der. 
        elif re.match(r"[A-Za-z]+",x) and "@" not in x:
            for y in Line:
                if "@" in y:
                    name=y.split("@")[0].split(".")
                    name=" ".join([x.capitalize() for x in name])
                    if x.capitalize() not in name:
                        name=x
                    else:
                        print("WARNING CODE 01: Name of ",x," Insufficient! Replaced with Local Part of E-mail")
        if not 'name' in globals():
            print("WARNING CODE 06: No Name Provided for ",line)
            continue
        
        
        ## tjek om der er en brugbar E-mail. Denne håndteres anderledes, hvis den mangler eller hvis den er ufuldendt. 
        if "@" in x:
            if re.match(r"[A-Za-z.]+[@]{1}[A-Za-z]+[.]{1}",x):
                mail=x
            else:
                print("WARNING CODE 02: E-mail for User: ",name," Not Sufficient!")
                mail="INSUFFICIENT_DATA"
        if not 'mail' in globals():
            print("WARNING CODE 03: E-mail for User: ",name," Not Found!")
            mail="DATA_NOT_FOUND"
        
        ## tjek om priserne er angivet korrekt
        if re.match(r"[0-9]+",x):
            if re.match(r"[0-9]+[.]{1}[0-9]+",x):
                purchase=re.sub(" ","",x)
                purchase=round(float(purchase),2)
                purchase=str(purchase)
                if len(purchase.split(".")[1])==1:
                    purchase+="0"
            if "-" in x:
                print("WARNING CODE 04: Purchase for user: ",name," At E-mail: ",mail," is Negative!")
        if not 'purchase' in globals():
            print("WARNING CODE 05: No Purchase for user: ",name," At E-mail: ",mail," Found!")
            purchase="DATA_NOT_FOUND"
        
               
    cleaned.append((",".join([str(n),name,mail,purchase])+"\n"))
    n=n+1

data.close()

if os.path.exists("cleaned_source_data.csv"):
    os.remove("cleaned_source_data.csv")

with open("cleaned_source_data.csv","a") as clean:
    for x in cleaned:
        clean.write(x)
