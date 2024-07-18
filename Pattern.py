print("Pattern 1")

'''
   ####
   ####
   ####
   ####

'''
for i in range(4):
     print("#"*4)


print()
print("Pattern 2")

'''
#
##
###
####
'''
for i in range(1,5):
    print("#"*i)


print()
print("Pattern 3")
'''
   *
  ***
 *****  for n = 3  
'''
n = int (input("Enter number "))

for i in range(1,n+1):
    print(" "*(n-i),end="") #spaces
    print("*"*(2*i-1))



print()
print("pattern 4")
'''
####
###
##
#
'''
for i in range(4): #rows
    for j in range(4-i): #colonms
        print("#",end="")
    print()


print()
print("Pattern 5")
'''
  ***
  * *              
  ***  for n = 3

  ****
  *  *
  *  *
  ****  for n = 4

  *****
  *   *
  *   *
  *   *
  *   *
  ***** for n = 5
'''
n = int (input("Enter number "))

for i in range(1,n+1):
    if(i==1 or i==n):
       print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")

        

