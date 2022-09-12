import os
import csv
import json
from re import A
from textwrap import indent
import tools.modules_and_stuff as modules 
# אני רוצה לבנות תוכנית מוסך (עם  class)
# יש לי מטודה של להוסיף מכונית , להציג את כל המכוניות 
# *אני רוצה חיפוש , נגיד להציג את כל המכוניות הכחולות (display) דיספליי עם תנאי DisplayByColor
# * remove של מכונית שהיוזר מחליט removeCar 
# * אני רוצה לשמור את המכוניות שלי לתוך קובץ (csv, json לא משנה אaיזה קובץ) save , saveJson

# תרגיל מספר 2

# "*אני רוצה שחלק מהפונקציות של המוסך יהיו במודול אחר, מודול שנמצא בספריית tools 
# *אני רוצה שכל הפרוייקט הזה יהיה בתוך virtual environment  


garage=[]

class Car:

    def getCarData(self):
        return self.cartype + " "+ self.carcolor + " " + str(self.modelyear)

    
    def __init__(self, type, color, year) :
        self.cartype = type 
        self.carcolor =color 
        self.modelyear = year 

def display():
    for car in garage:
        print(car.getCarData())

def addCar():
    temp= Car(input("car type ") , input("car color ") , input("model year "))
    return temp 


def removeCar():
    display()
    removetype = input("type car from the list to remove ")
    removecolor = input("choose a color to remove ")
    removeyear= input("choose a year to remove ")
    for car in garage:
        if car.cartype == removetype:
            if car.carcolor == removecolor:
                if car.modelyear == removeyear:
                    garage.remove(car)
   
    

def displaycolor(color):
    for car in garage :
        if car.carcolor ==color:
            print(car.getCarData())


def writeToCsv():
    header = ["car type","car color" , " model year"]
    with open("carsgarage.csv" , "w", encoding="UTF8" , newline="") as f:
       writer = csv.writer(f)
       writer.writerow(header)
       
       for car in garage :
           savelist = [car.cartype , car.carcolor , car.modelyear]
           writer.writerow(savelist)

def writeToJson():
    carslist = []
    for car in garage:
        dictlist = {"car type ":car.cartype,"car color":car.carcolor,"year of model":car.modelyear}
        carslist.append(dictlist)
    jsondata = json.dumps(carslist , indent=-3)
    with open ("jsonlist.json", "w",) as file:
        file.write(jsondata)

def main():
    global garage 
    msg ="welcome to the garage , please select an option "
    while(True):
        print(msg)
        print("a -add a car ")
        print("d- display all cars ")
        print("c - show  cars by color")
        print("r- remove a car")
        print("s- save cars list to csv file")
        print("j - save to json file")
        print("x- to exit ")
        userinput = input (" plesse choose one of the options from the menu ")
        modules.clearConsole()
        if userinput == "a":
            garage.append(addCar())
            msg = " car was added to garage list"
        elif userinput == "d":
            display()
            msg = " garage list of cars displayed "
        elif userinput =="c":
          displaycolor(input("please enter color you want to see "))
            
          msg = " displayed cars by users color"
        elif userinput== "r":
            removeCar()
            msg= " the car has been removed from the list"
        elif userinput =="s":
            writeToCsv()
            msg = " garage list of cars saved to  csv file"

        elif userinput=="j":
            writeToJson()
            msg = "garage list of cars saved to json file"

            
        elif userinput =="x":
            print ("thank you , come again ")
            return
        else:
            print ("your choise is invalid, try again")


if __name__ == "__main__":
 main()
    


           





      
