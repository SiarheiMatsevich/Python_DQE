# #Create a python script:
#
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.
import random
#List of random numbers declaring:
randList = []

# Random generator and list filling:
while len(randList) < 100: # While loop is using for repeating actions until length of list is 100
    i = random.randint(0, 1000) # Declaring of random integer in range 0-1000
    randList.append(i) # Packing of generated integer into the list
print("Unsorted list: " + str(randList)) # Output of generated list after while loop is finished

#Bubble Sort
for b in range(len(randList)): # Repeating of for loop for each element in the array
    for j in range(len(randList) - 1): # Another for loop repeats comparing for each element except for the last one
        if randList[j] > randList[j+1]: # Comparing of j element vs j+1"next" element
            temp = randList[j] # Declaration of temporary variable and assigning j element to it if it's higher than j+1
            randList[j] = randList[j+1] # Replacing j+1 element with j element
            randList[j+1] = temp #Replacing j+1 element with j1 element using temporary variable
print("Sorted list: " + str(randList)) #Sorted list output

#Even/Odd separation
evenNums = [] # Declaration of list for even numbers
oddNums = [] # Declaration of list for odd numbers

for e in randList: # for loop to check if each randList element even or odd
    if e % 2 == 0: # Checking of e element if it even
        evenNums.append(e) # Packing of given element to list for even numbers
    else: # Actions for odd numbers
        oddNums.append(e) # Packing of given odd element to odd list

# Even and Odd avg calculation
evenAvg = int # Declaration of Even Average integer
oddAvg = int # Declaration of Odd Average integer
try: # Try statement for average even number calculation
    evenAvg = sum(evenNums) / len(evenNums) # Division of sum of all even numbers by quantity of such numbers
except ZeroDivisionError: # Exception processing for a case when there is no even numbers
    print("There are no Even Numbers to calculate Average") # Wording of the error displayed for user
print("Even Average: " + str(round(evenAvg))) # Output of average even number rounded to integer
try: # Try statement for average odd number calculation
    oddAvg = sum(oddNums) / len(oddNums) # Division of sum of all odd numbers by quantity of such numbers
except ZeroDivisionError: # Exception processing for a case when there is no odd numbers
    print("There are no Odd Numbers to calculate Average") # Wording of the error displayed for user
print("Odd Average: " + str(round(oddAvg))) # Output of average odd number rounded to integer







