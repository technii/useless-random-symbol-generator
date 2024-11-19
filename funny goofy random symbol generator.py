import random

amount = 0
letters = ["!","£","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]",":",";","@","'","<",",",".","?","/"]
output = []
amount = input("imput amount of characters you wish for -> ") 
foram = int(amount)
while foram > 0:
    arraynumber = random.randrange(0,25)
    output.append(letters[int(arraynumber)])
    foram = foram - 1
printoutput = "".join(output)
print("output =",printoutput)
input("")
