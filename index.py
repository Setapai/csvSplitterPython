import pandas as pd
import os

print("Csv Splitter \n")
columnName = input("Column Name : ")
split = input("Split the entries into? EX. 10, 100, 1000, 10000 etc: ")
fileName = input("\nFile Name : ")

# Variables
filteredCsv = {
    columnName: [],
}

# Functions
def readFile(file):
    file_Data = pd.read_csv(fr"{file}.csv")
    file_List = file_Data[columnName].to_list()
    return file_List

try:
    for index,entries in enumerate(readFile(fileName)):
        if index % int(split) == 0 and index != 0:
            data = pd.DataFrame(filteredCsv)
            if not os.path.exists("split"):
                os.makedirs("split")

            data.to_csv(fr"Split\\{columnName}{index}.csv", index=False)
            filteredCsv[columnName] = []
        else:
            filteredCsv[columnName].append(entries)
except NameError:
    print(f"\nName Error | Error : {NameError}")
except FileNotFoundError: 
    print(f"\nFile Not Found | Error : {FileNotFoundError}") 
except PermissionError:
    print(f"\nPermission Problem | Error : {PermissionError}")
except IsADirectoryError:
    print(f"\nDirectory Problem | Error : {IsADirectoryError}")
except KeyError:
    print(f"\nColumn Not Found | Error : {KeyError}")

print('\nSplit Complete File are located in Split Folder')
input("press Enter to Exit")