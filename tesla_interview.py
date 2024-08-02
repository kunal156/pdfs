#TESLA Interview QUESTION

#ba ba black sheep 
#have you any wool
#yes sir 
#yes sir
#three bags full
# poem = ["Ba Ba Black Sheep", 
#         "have you any wool", 
#         "yes sir", 
#         "yes sir", 
#         "three bags full"
#         ]

poem =     ["Humpty Dumpty sat on a wall",
            "Humpty Dumpty had a great fall",
            "All the kings horses and all the kings men",
            "Couldnt put Humpty together again"]

#Algorithm 
#1 Tried to convert the line into a two dimensional associative array/dictionary
#2 Calculated Max Width and lenght of the poem. 
#3 Max of two is going to be dummy matrix with same number of Rows and Colums , 
#4 Wasting memory by allocating EMPTY, which can be optimized but stills its not a list or an array
#5 

print ("-I- Creating a dictionary, MAX Length and CNT for MAX_WIDTH ")    
poem1={}; 
max_length =0 ; 
cnt = 0 

# FUNCTION That converts LIST To DIC
def list2dic(list):
    dict0 ={}
    cnt =0 
    for l in list:
        dict0[cnt] = l
        cnt = cnt+1 
    return dict0

print("-I- Reading the POEM and creating a dictionary for it" )   
for line in poem: 
    poem1[cnt] = list2dic(line.rsplit())
    print('split',cnt, poem1[cnt])
    if(max_length < len(poem1[cnt])):
        print("max_lenght", len(poem1[cnt]))
        max_length = len(poem1[cnt])
    cnt = cnt +1
    print(cnt)

print("-I- Printing Poem from Dictionary", poem1)
print(poem1)
max_value =0 
max_width = cnt  #Max widht is got from the final count 
if(max_length > max_width ):
    max_index = max_length
else :
    max_index = max_width
print ("-I- MAX", max_value, max_length , max_width)

print("-I- Creating a dummy dictionary for transpose and setting up with no data")



poem2={} #Edit the poem to fill empty space
poem3={}

for i in range(0, max_index):
    poem2[i]={}
    poem3[i]={}
    for j in range(0, max_index):
        poem2[i][j] = ""
        poem2[i][j] = ""

print(poem2)        


print("-I- \n")
for key0,value0 in poem2.items():
    print("\n")        
    for key1, value1 in value0.items(): 
        if(key0 in poem1):
            if(key1 in poem1[key0]):
                poem2[key0][key1] = poem1[key0][key1]
                print(key0, key1, poem2[key0][key1],end=" ")
            else: 
                poem2[key0][key1] = "EMPTY"
                print(key0, key1, poem2[key0][key1],end="")

print ("-I- Creating a transpose")
for key0,value0 in poem2.items():
    for key1, value1 in value0.items(): 
        poem3[key1][key0] = poem2[key0][key1]
print("\n")        

print("FINAL Output")
for key0,value0 in poem3.items():
    print("\n")        
    for key1, value1 in value0.items(): 
        if(poem3[key0][key1] !="EMPTY"):
            #print(" ",key0,key1," ", poem3[key0][key1],end="")
            print( poem3[key0][key1],end="  ")




        
