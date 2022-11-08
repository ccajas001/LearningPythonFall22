print("hello world") #Textual Data - Strings
print("I can now run a simple python code")
age=20 #age is a variable now
print(age) #prints age
age=40#change age
print(age)
first_name = "Camille"
is_online = False #python is case sensitive

#Exercise
patient_name = "John Smith"
patient_age = 20
patient_new = True
print(patient_name,patient_age)
if(patient_new) : print("True")

#ReceivingInput and TypeConversion
""" <<take out blocks
receiving_name = input("what is your name? ")
receiving_birthYear = input ("enter birth year: ")
receiving_age = 2022 - int(receiving_birthYear) #type conversion
print("Hello " + receiving_name)
print(receiving_age)
"""

#Type Conversion
#bool(),int(),float(),str()
#

#Exercise2 Calc Program
firstNum = input("First: ")
secondNum = input("Second: ")
sum = float(firstNum)+float(secondNum) #convert to float
print("Sum:" + str(sum)) #convert back to string