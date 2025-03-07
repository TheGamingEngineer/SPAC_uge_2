import matplotlib.pyplot as plt
import os
text=input("Enter text file with names:")

try:
    with open(text,'r') as t:
        names=t.readlines()[0].split(",")
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


names=sorted(names)

alphabet={"a":0,"b":0,"c":0,"d":0,
          "e":0,"f":0,"g":0,"h":0,
          "i":0,"j":0,"k":0,"l":0,
          "m":0,"n":0,"o":0,"p":0,
          "q":0,"r":0,"s":0,"t":0,
          "u":0,"v":0,"w":0,"y":0,
          "z":0,"æ":0,"ø":0,"å":0,}

name_lengths=[]

sorted_alphabet=sorted([key for key in alphabet.keys() if key not in ["æ","ø","å"]])+["æ","ø","å"]

if os.path.exists("Sorted_Names.txt"):
    os.remove("Sorted_Names.txt")

with open("Sorted_Names.txt","a") as output_names:
    ## skriver den sorterede navneliste til sorted_names.txt som hver sin linje
    output_names.write("########## name list ###########\n")
    for name in names:
        output_names.write(name+"\n")
        for key in alphabet:
            alphabet[key]+=name.lower().count(key)
        print(name)
        name_lengths+=[len(name)]

## gennemsnit udregnes som sum/antal
name_length_average = sum(name_lengths)/len(name_lengths)

## medianen er det midterste tal i en sorteret liste tal. 
name_length_median = sorted(name_lengths)[int(len(name_lengths)*0.5)]
name_length_25 = sorted(name_lengths)[int(len(name_lengths)*0.25)]
name_length_75 = sorted(name_lengths)[int(len(name_lengths)*0.75)]

## minimum og maksimum længderne
name_length_min = min(name_lengths)
name_length_max = max(name_lengths)

if os.path.exists("Name_Statistics.csv"):
    os.remove("Name_Statistics.csv")
        
### skriver statistikken til Name_Statistics.csv
with open("Name_Statistics.csv","a") as name_stat:
        name_stat.write("Average Name Length," + str(name_length_average) + "\n")
        name_stat.write("Maximum Name Length," + str(name_length_max) + "\n")
        name_stat.write("Minimum Name Length," + str(name_length_min) + "\n")
        name_stat.write("Name Length at 25% Quantile," + str(name_length_25) + "\n")
        name_stat.write("Name Length Median," + str(name_length_median) + "\n")
        name_stat.write("Name Length at 75% Quantile," + str(name_length_75) + "\n")
        
        ## skriver bogstavsstatistik til name_statistics.csv
        for letter in sorted_alphabet:
            stat=letter + "," + str(alphabet[letter])
            name_stat.write(stat+ "\n")


#### laver plot til statistikken. 
labels=["Average","Max.",
        "Min.","Q25",
        "Median","Q75"]
stats=[name_length_average,name_length_max,
       name_length_min,name_length_25,
       name_length_median,name_length_75]
fig, ax = plt.subplots()
ax.bar(labels,stats)

#### laver plot til bogstavsstatistikken
sorted_letter_stats=[alphabet[x] for x in sorted_alphabet]
fig2, ax2 = plt.subplots()
ax2.bar(sorted_alphabet,sorted_letter_stats)

fig.savefig("name_statistics.png")
fig2.savefig("name_letter_frequency.png")


print("Job is Done!")        
        