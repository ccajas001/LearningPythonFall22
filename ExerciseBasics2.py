"""
Exercises from https://pynative.com/python-basic-exercise-for-beginners/
Tuesday 11/02/2022 - moving forward with be putting timestamps on source code

Total time (1:48 - 3:11) 1 hr 23 mins

    (5) Write a function to return True if the first and last number of a given
    list is same.If numbers are different then return False.

    Starttime 1:48
    Endtime 2:12
"""


def first_last_same(number_list):
    print("Given number list: " + str(number_list))
    count = len(number_list)
    if number_list[0] == number_list[count-1]:
        print("True")
    else:
        print("False")


print()
print("Exercise 5: ")
ex5_numberList1 = [20, 40, 56, 23, 30]
ex5_numberList2 = [20, 30, 40, 70, 20]
first_last_same(ex5_numberList1)
first_last_same(ex5_numberList2)

"""

    (6) Iterate the given list of numbers and print 
    only those numbers which are divisible by 5
    Start time: 2:12
    End time: 2:18
"""
print()
print("Exercise 6: ")
ex6_numberList1 = [15, 3, 6, 34, 20, 15, 50]
print("Given list: " + str(ex6_numberList1))
for i in range(len(ex6_numberList1)):
    if ex6_numberList1[i] % 5 == 0:
        print("Index:" + str(i) + " Value:" + str(ex6_numberList1[i]))



"""
    (7) Write a program to find how many 
    times substring “Emma” appears in the given string.
    
    Start time: 2:18
    End time: 2:46 (unable to do on my own)
    
"""
print()
print("Exercise 7: Failed")
ex7_string = "Emma is coming to school tomorrow. I like Emma."
ex7_length = len(ex7_string)-1
ex7_count = 0
for i in range(ex7_length):
    if ex7_string[i:ex7_length].find("Emma") == -1:
        i = ex7_length
    else:
        ex7_count += 1
        ex7_nextString = ex7_string[i:ex7_length].find("Emma") + 4
        i = ex7_nextString
print(ex7_count)

"""
    (7) Solution 1:
    
str_x = "Emma is good developer. Emma is a writer"
# use count method of a str class
cnt = str_x.count("Emma")
print(cnt)
    
    Solution 2:
    
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")
 Run

(8) print following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

Start time: 2:48
End time: 2:54
"""
print()
print("Exersice 8: ")

#forloop
for i in range(1,6):
    string = ""
    for j in range(i):
        string += " " + str(i)
    print(string)

"""
(9) Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse. 
For example 545, is the palindrome numbers

Star time : 3:56
end time : 3:11

"""

print()
print("Exercise 9: ")

ex9_inputNum = int(input("Please typ in an integer: "))
ex9_reverse = 0
ex9_original = ex9_inputNum

#reversing input number
while ex9_inputNum > 0:
    remainder = ex9_inputNum % 10
    ex9_reverse = (ex9_reverse*10) + remainder
    ex9_inputNum //= 10

#if numbers are the same then print out appropiate respond
if ex9_original == ex9_reverse:
    print("Given Number is a palindrome")
else:
    print("Given number is not a palindrome")
