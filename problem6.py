#Create an empty dict. Allow 4 friends to enter their fav language as value and use key as their names. Assume that the names are unique.
dict={}
for var in range(4):
      inpKey=input("Enter your Name : ")
      inpValue=input("Enter your fav languague of student : ")
     # dict[inpKey]=inpValue
      dict.update({inpKey:inpValue})

print(dict.items())