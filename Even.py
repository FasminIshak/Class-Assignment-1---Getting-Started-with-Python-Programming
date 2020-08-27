n = int(input("enter the total number of elements:"))
sum = 0

for n in range(1,1+n):
    if (n % 2 == 0):
        print("{0}".format(n))
        sum = sum + n
        
print("The Sum of Even Numbers from 1 to {0} = {1}".format(n, sum))