#Deeya Bachani
#how to make a list
#how to manipulate the element to find what we need
import os
import sys
import time
os.system('cls')




file=open("asdfre.txt", 'r')
sort=file.readlines()
sortedscore=sorted(sort,reverse=True)[::-1]
for line in range(3):
    print(str(line+1)+"\t"+str(sortedscore[line]))
file.close()

#file= "asdfre.txt"
#FILE=open(file, 'r')
#content= FILE.read() #is string with whole content of file
#print(content)
#FILE.close()
#FILE=open(file, 'r')
#content_List= FILE.readlines() #is a list of each line of the file
#print(content_List)
#FILE.close()
#for element in content_List:
#    print("line : ", element)
#    elem_list=element.split()
#    print(elem_list)
#    time.sleep(1)
#How do we rearrange our scores file by highest to lowest?
