#Variables
price = 10 #integer
rating = 4.9 #float
course_name = "Python for Beginners" #string
is_published = True #boolean

#Comments

# This is a comment and it won’t get executed.
# Our comments can be multiple lines.

#Receiving Input: input()
""" commented so it doesn't pop up
birth_Year = int(input("Input Birth Year: "))
age = 2022 - birth_Year
print(age)
"""
#Strings
course = "Python for Beginners"
course[0] # returns the first character
course[1] # returns the second character
course[-1] # returns the first character from the end
course[-2] # returns the second character from the end

print(course[2]) #Starts at index 0 should print 't'
#Strings here are similar to those in java

print(course.upper()) #should print this in upper case
"""\
other stuff

message.upper() # to convert to uppercase
message.lower() # to convert to lowercase
message.title() # to capitalize the first letter of every word
message.find(‘p’) # returns the index of the first occurrence of p
(or -1 if not found)
message.replace(‘p’, ‘q’)
"""

#Type Conversion
#bool(),int(),float(),str()
#

#Arithmetic

"""
+ 
-
*
/ float div
// int div
% mod
** exponent/pow >> new to me
"""

#Loops // very similar structure
for i in range(1,4):
    if(i%2==0) : print('*')
    else: print ("**")

#Lists // can modify unlike tuples
number = [1,3,5,6,7,8]
for i in range(5):
    print(number[i])

#Tuples // read-only lists
number_2 = (1,2,3,4)
a,b,c,d = number_2
print (a,b,c,d)

#Video https://www.youtube.com/watch?v=kqtD5dpn9C8&t=0s