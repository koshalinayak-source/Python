# Write a python program to print the contents of a directory using the os module. search online for the function which does that
import os

#specify the dir you want to list
dir_path="/"

#list all the files and dir in the specified path
contents=os.listdir(dir_path)

#print each file and dir name 
for item in contents:
    print(item)