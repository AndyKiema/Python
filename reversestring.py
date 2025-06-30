#Reversing a string
#Method 1
s='welcome'
rev_string=''
for i in s:
    rev_string=i+rev_string
print(rev_string) #emoclew
#i takes on the value of each character in the string
#First, it takes on 'w', so rev_string='w'+'', which is 'w'
#Second, it takes on 'e', so rev_string='e'+'w' which is 'ew'
#Third, it takes on 'l', so rev_string='l'+'ew' which is 'lew'
#Fourth, it takes on 'c', so rev_string='c'+'lew' which is 'clew'
#Fifth, it takes on 'o', so rev_string='o'+'clew' which is 'oclew'
#Sixth, it takes on 'm', so rev_string='m'+'oclew' which is 'moclew'
#Second, it takes on 'e', so rev_string='e'+'moclew' which is 'emoclew'

#Method 2
s='welcome'
sr=s[::-1]
print(sr) #emoclew
#Slicing method is used here
#The first : means starting from the beginning since starting point hasnt been specified
#The second : means finishing at the end since ending point hasnt been specified
# -1 means moving backwards