""" helloOOP.py
    helloIO converted to OOP
"""
#import the graphic user interface
from tkinter import *

#make the app
class App(Tk):
  
  def __init__(self):
    Tk.__init__(self)

    #title the app
    self.title("Body Mass Index")

    #set the font
    self.headerFont = ("Times New Roman", "16", "bold")
   
    #make a label for height in feet
    Label(self, text = "Height(ft)", font = self.headerFont).grid(row = 0, column = 0)

    #make a textbox for height in inches
    self.txtHeightInFeet= Entry(self)
    self.txtHeightInFeet.grid(row = 0, column = 1)
    
    #make a label for height in inches
    Label(self, text = "Height(inches)", font = self.headerFont).grid(row = 1, column = 0)

    #make a textbox for height in inches
    self.txtHeightInInches= Entry(self)
    self.txtHeightInInches.grid(row = 1, column = 1)

    #make a label for weight
    Label(self, text = "Weight(lbs)", font = self.headerFont).grid(row = 2, column = 0)

    #make a textbox for weight
    self.txtInputWeight = Entry(self)
    self.txtInputWeight.grid(row = 2, column = 1)

    #make a button for BMI calculation
    self.btnCalculation = Button(self, text = "Body Mass", command = self.bodyMass, font = self.headerFont)
    self.btnCalculation.grid(row = 5, columnspan = 2)

    #make a label for output
    self.lblMass = Label(self, text = "",font = self.headerFont)
    self.lblMass.grid(row = 7, columnspan = 2)
    
    self.mainloop()

  #calculate BMI
  def bodyMass(self):

    #convert values of height
    heightinfeet = float(self.txtHeightInFeet.get())
    heightininches = float(self.txtHeightInInches.get())

    #find height in inches
    height = (heightinfeet * 12) + heightininches
    
    #get weight and convert it
    weight = float(self.txtInputWeight.get())
    
    
    #solve for body mass
    bodymass = (weight * 703) /  (height * height)

    #use if to find the catoegory for user's BMI
    if bodymass <= 18.5:
      self.lblMass["text"] = "Your status is underweight"
    elif bodymass >= 18.51 and bodymass <= 24.9:
      self.lblMass["text"] = "Your status is normal"
    elif bodymass >= 25 and bodymass <= 29.99:
      self.lblMass["text"] = "Your status is overweight"
    else:
      self.lblMass["text"] = "Your status is obese"
      
    

def main():
  a = App()
  
if __name__ == "__main__":
  main()
