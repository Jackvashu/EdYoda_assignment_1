countEven = 0
countodd = 0

numbers = (1,2,3,4,5,6,7,8,9)
for i in numbers:
    if(i%2 == 0):
        countEven +=1
    else:
        countodd +=1

print("Number of even numbers: {}".format(countEven));
print("Number of odd numbers: {}".format(countodd));

