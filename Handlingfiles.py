#Writing data in a text file
"""file=open('C:/Users/Administrator/Desktop/myfile.txt', 'w') #variable represents file in writing mode
file.write('This is my first statement\n')
file.write('This is my second statemen\n')
file.write('This is my third statement\n')
file.write('This is my fourth statement')
file.close()
print('Program completed')"""

#Reading data from text file
#file=open('C:/Users/Administrator/Desktop/myfile.txt', 'r') #variable represents file in reading mode
#print(file.read()) #This is my first statement This is my second statemen This is my third statement This is my fourth statement
#print(file.readline()) #.readline() will read first line: This is my first statement
#file.close()

#Add data in a file. DONE WHEN THERE IS DATA IN THE FILE ALREADY
file=open('C:/Users/Administrator/Desktop/myfile.txt', 'a') ##variable represents file in appending mode
file.write('This is my seventh statement\n')
file.write('This is my eighth statement')
file.close()
print('Program completed')