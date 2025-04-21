
n = int(input())
right_fish='><>'
left_fish='<><'
fish_list=[right_fish,left_fish]
# first print the tank 
#Tank dimensions: 15 rows x 25 columns
for i in range(15):  
    for j in range(25):
        if i==0 and j==0:
            print("o",end="")
        elif i==0 and j==24:
            print("o")
        elif i==0:
            print("-",end="")
        # front line done 
        if i > 0 and i <14 and j==0:
            if n ==0:
                print("|",end="                       ")
            else:
                 print("|",end="><>                    ")
                 n= n -1 
        elif i > 0 and i <14 and j==24:
            print("|")
        # side lines don e
        if i==14 and j==0:
            print("o",end="")
        elif i==14 and j==24:
            print("o",end="")
        elif i==14:
            print("-",end="")  
        # last line done
# task done 
#1. n input done 
#2. tank printed done 

# final task 
# print fish 

        

