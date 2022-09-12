import os 
import csv
import json
garage =[]
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

header = ["cartyple", "carcolor","modelyear"]

def writeToCsv():
    with open("carsgarage.csv" , "w", encoding="UTF8" , newline="") as f:
       writer = csv.writer(f)
       writer.writerow(header)
       
       for car in garage :
           savelist = [car.cartype , car.carcolor , car.modelyear]
           writer.writerow(savelist)
      

def display():
    for car in garage:
        print(car.getCarData())

def displaycolor(color):
    for car in garage :
        if car.carcolor ==color:
            print(car.getCarData())
