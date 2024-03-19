#classes!!!!!!!!!!!!!!!!!!!!!!!!!!!
""" 
class Calculator():
    #encapsulation
    def add(x,y):
        return x+y
    def subtract(x,y):
        return x-y
print(Calculator.add(5,6))
print(Calculator.subtract(5,6))

class Score():
    def add(x,y):
        return x+y """

import datetime
today=datetime.date.today()
year = today.year

class Album():
    #create template for Album
    def __init__(self,title,artist,year):
        self.title=title
        self.artist=artist
        self.year=year
    def how_old(self):
        return year-self.year
    def __str__(self):
        return f"{self.title}, {self.artist}"

Abbey_Road = Album("Abbey Road", "Beatles", 1969)
Midnights = Album("Midnights", "Taylor Swift", 2022)
print(Abbey_Road.how_old())
print(Midnights)