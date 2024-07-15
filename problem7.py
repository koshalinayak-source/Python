#If the names of 2 friends are same; what wil happen to the program in problem 6 ?
dict={}
for var in range(4):
      inpKey=input("Enter your Name : ")
      inpValue=input("Enter your fav languague of student : ")
      dict[inpKey]=inpValue

print(dict.items())
