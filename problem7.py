#Write a program to print multiplication table of n using for loops in reveres order
num =int(input("Enter a number "))
for i in range(10,0,-1): #Loop from 10 to 1 in reverse order 
    print(num," * ",i," =",num*i)
