import tkinter.messagebox
from tkinter import simpledialog

#This function reads the animal.txt file data and organizes it into lists.
def readme():
    AnimalInfo = open('animals.txt', 'r')
    global AnimalList
    AnimalList = AnimalInfo.readlines()
    AnimalList.sort()
    tkinter.messagebox.showinfo('Success', 'File has been read')
    global AnimalPhy
    global AnimalDiet
    global AnimalName
    AnimalPhy = []
    AnimalDiet = []
    AnimalName = []
    for sequence in AnimalList:
        AnimalName.append(sequence.split(",")[0])
        AnimalPhy.append(sequence.split(",")[1])
        AnimalDiet.append(sequence.split(",")[2].replace("\n",""))

#This function displays the first animal phylum list.
def displayanimals():
    print("Name\t    Diet\tPhylum")
    print("----\t    ------\t----")
    for position in range(0,len(AnimalName)):
        print(str(format(AnimalName[position], "12s")) + str(format(AnimalDiet[position], "12s")) + str(AnimalPhy[position]))
#I used format to indicate the number of spaces between each category.

#This function contains the copied code from the instructions.
def displayphylum():
    outMam = ""
    outRep = ""
    outBird = ""
    output = "\n\n--- Animals by Phylum ---"
    for i in range(len(AnimalName)):
        if AnimalPhy[i] == "Mammal":
            outMam += "\n" + format(AnimalName[i], "10s") + AnimalDiet[i]
        elif AnimalPhy[i] == "Bird":
            outBird += "\n" + format(AnimalName[i], "10s") + AnimalDiet[i]
        elif AnimalPhy[i] == "Reptile":
            outRep += "\n" + format(AnimalName[i], "10s") + AnimalDiet[i]
        
    output += "\n\nMammals\n----------"
    output += outMam
    output += "\n\nReptiles\n----------"
    output += outRep
    output += "\n\nBirds\n----------"
    output += outBird
    print(output)

#This function asks the user for an animal and displays its phylum and diet.
def askanimal():
    animal = simpledialog.askstring("Animal to Show", "Enter an animal")
    animal = animal.capitalize()
    for index in range(0,len(AnimalName)):
        if AnimalName[index] == animal:
            print("\n\n" + AnimalName[index] + " is a " + AnimalPhy[index] + ", " + AnimalDiet[index])
#I used the capitalize method to compare the input data with the list.

#Functions are called here.
readme()
displayanimals()
displayphylum()
askanimal()
