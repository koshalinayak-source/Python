#Write a program to input 8 numbers from the user and display all the unique numbers(once)

s=set()

for var in range(8):
      inp=input("Enter a number from 0-9 : ")
      s.add(int(inp))

print(s)      