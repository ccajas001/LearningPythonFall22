"""
Exercises from https://pynative.com/python-basic-exercise-for-beginners/

    (1) Given two integer numbers return their product only if the
   product is equal to or lower than 1000, else return their sum.

    My attempt:
"""

#variables
print("Exercise 1: ")
ex1_number1 = int(input("Give me an integer: "))
ex1_number2 = int(input("Give me another integer: "))
print("Number 1: " + str(ex1_number1))
print("Number 2: " + str(ex1_number2))

#conditions
if ((ex1_number2 * ex1_number1)<=1000): print("Product of both numbers: " + str(ex1_number2 * ex1_number1))
else: print("Sum of the two numbers: " + str(ex1_number2 + ex1_number1))
"""
    Ending notes: could have used a function to set the conditional, too messy



    (2) Write a program to iterate the first 10 numbers and in
    each iteration, print the sum of the current and previous number.
    
    My attempt:
"""
print("")
print("Exercise 2:")

# set base variables
ex2_current = 0
ex2_prev = 0

# conditional
for i in range(10):
    ex2_prev = ex2_current
    ex2_current = i
    ex2_sum = ex2_prev + ex2_prev
    print("Current Number: " + str(ex2_current) + " + Previous Number: " + str(ex2_prev) + "  Sum: " + str(ex2_sum))

"""
    Ending notes: feel like i did the exercise properly


    (3) Write a program to accept a string from the user 
    and display characters that are present at an even index number.
    
    My Attempt:
"""
print()
print("Exercise 3: ")

ex3_inputString = input("Give me a string: ")
print("Printing char in even index only")
for i in range(len(ex3_inputString)):
    if i%2==0: print(ex3_inputString[i])

"""

    (4) Write a program to remove characters from a string starting from 
    zero up to n and return a new string.
    
    Failed Attempt
    Solution online V V V 
"""
print()
print("Exercise 4: ")

def remove_chars(ex4_word,ex4_number):
    print("Original String: ", ex4_word)
    x = ex4_word[ex4_number:] #
    return x

print(remove_chars("pynative",2))
print(remove_chars("pynative",4))
