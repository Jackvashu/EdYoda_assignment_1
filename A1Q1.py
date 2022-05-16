
# Fibonacci series Assignment-1 

num1 = 0  # first number is 0
num2 = 1 # second number is 1
print(num2, end=" "); # firstly printing 1  with using end=" "
for i in range(50): # 0 to 50
   num3 = num1 + num2;  # adding n = (n-1) +(n-2)
   print(num3, end=" ");
   num1 = num2;
   num2 = num3;

# Expected output : 1 2 3 5 8 13 21 34 ....
# my output : 1 2 3 5 13 21 34 ....
   

 