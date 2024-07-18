#Write a program to calculate the factorial of a given number using loop
fact=1
num =int(input("Enter a number "))

for i in range(1,num+1):
    fact=i*fact

print(fact)