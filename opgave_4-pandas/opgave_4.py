import pandas as pd
import matplotlib.pyplot as plt
from numpy import unique,arange

try:
    data=pd.read_csv("DKHousingPricesSample100k.csv",sep=",")
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


## print de første 10
print(data.head(10))

## gruppering af data per region. 
regional_groupies=data.groupby('region')

## gennemsnits huspriserne og antal huse per region.
regional_mean_price=regional_groupies.agg(
    highest_price=('purchase_price','max'),
    lowest_price=('purchase_price','min'),
    average_price=('purchase_price','mean'),
    std_price=('purchase_price','std'),
    number_of_houses=('region','count')).reset_index()


fig, ax = plt.subplots(layout='constrained')
ax.bar(regional_mean_price['region'],regional_mean_price['average_price'])
regional_mean_price.plot(y="average_price",kind="bar")
fig.savefig('Gennemsnitshuspriserne over regionerne.png')

## gruppering og plotting af hustype over regionerne.
house_groupies=data.groupby(['house_type','region'])
house_groupies=house_groupies.agg(
    average_price=('purchase_price','mean')).reset_index()

regions=list(unique(house_groupies['region']))
house_prices={}

for x in list(unique(house_groupies["house_type"])):
    house_prices[x]=list(house_groupies[house_groupies["house_type"]==x]["average_price"])

fig, ax = plt.subplots(layout='constrained')
multiplier=0
x = arange(len(regions))
width=0.15

for attribute, measurement in house_prices.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    #ax.bar_label(rects, padding=10)
    multiplier += 1
    
ax.set_ylabel('gennemsnitshuspris')
ax.set_title('gennemsnitshuspriserne over regioner og typer')
ax.set_xticks(x + width, regions)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, max(house_groupies["average_price"]))
plt.show()
fig.savefig('gennemsnitshuspriserne over regioner og typer.png')

### gennemsnitshustypepriser over tidsperioder. 
data["year"]=data.quarter.str.split("Q",expand=True)[0]
prices_through_ages=data.groupby(["house_type","year"])
prices_through_ages=prices_through_ages.agg(
    average_price=('purchase_price','mean')).reset_index()

ages=list(unique(prices_through_ages['year']))
fig, axs = plt.subplots(1,figsize=(12,10))

for x in list(unique(prices_through_ages['house_type'])):
    axs.plot(prices_through_ages[prices_through_ages['house_type']==x]['year'],
             prices_through_ages[prices_through_ages['house_type']==x]['average_price'],
             label=x)


plt.xlabel('år')
plt.ylabel('Gennemsnitshusprisen')
plt.title('Gennemsnitshusprisen for hustyper igennem tiden.')    
plt.legend(title='Hustype')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
fig.savefig('Gennemsnitshusprisen for hustyper igennem tiden.png')

### samme som før men for regionerne.
prices_ages=data.groupby(["region","house_type","year"])
prices_ages=prices_ages.agg(
    average_price=('purchase_price','mean')).reset_index()

fig, axs = plt.subplots(2, 2,figsize=(12,10))
axs = axs.flatten()

for i,region in enumerate(list(unique(prices_ages['region']))):
    regional_data=prices_ages[prices_ages['region']==region]
    
    for y in list(unique(regional_data['house_type'])):
        house_data=regional_data[regional_data['house_type']==y]
        axs[i].plot(house_data['year'],house_data['average_price'],label=y)
        
    

    axs[i].set_xlabel('år')
    axs[i].set_ylabel('gennemsnitshusprisen')
    axs[i].set_title(f'Gennemsnitshusprisen for {region} igennem Tiden')    
    axs[i].legend(title='region')
    axs[i].tick_params(axis='x',rotation=90)

plt.tight_layout()
plt.show()
fig.savefig("gennemsnitshusprisen for hver region igennem tiden.png")