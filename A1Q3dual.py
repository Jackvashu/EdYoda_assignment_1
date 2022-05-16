# Second example dynamic sample number to get even and Odd 

inputLength = int(input("Enter the length of sample : ")) # input for list length 
numbers = [] # new list 
countEven = 0 # counter for Even 
countOdd = 0 # counter for odd
for index in range(1, inputLength):  # iteration for list length
    newList = int(input("Add numbers : ")) # adding new numbers to list
    numbers.append(newList); # add/append number to list
    
newtuple = tuple(numbers) # type conversation for changing list to tuple
for item in newtuple: # iterating new tuple
    if item%2 ==0 :
        countEven +=1 # count even
    else : 
        countOdd +=1 # count Odd

print("Number of even numbers : {}".format(countEven))   # Numbers for even number
print("Number of odd numbers : {}".format(countOdd))   # Numbers for Odd number