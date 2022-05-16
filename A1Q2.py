
# assignment -1 - Send the words to mirror Dimension

takeWord = input("Enter word : ");

# using Joined function and plus reversed function 
newString = "".join(reversed(takeWord))
print("Mirror Word is : {}".format(newString));