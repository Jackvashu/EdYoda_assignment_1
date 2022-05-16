# 2nd solution for reverse

takeInput = input("Input : ")

# [::-1] slice the string means start 
# form end go upto 0 index with step -1

reverseWord = takeInput[::-1];

print("Output : {}".format(reverseWord));