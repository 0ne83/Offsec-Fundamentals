import math
 
# function to check
# Pronic Number
def checkPronic (x) :
 
    i = 0
    while ( i <= (int)(math.sqrt(x)) ) :
         
        # Checking Pronic Number
        # by multiplying consecutive
        # numbers
        if ( x == i * (i + 1)) :
            return True
        i = i + 1
 
    return False
 
# Driver Code
 
# Printing Pronic
# Numbers upto 200
i = 4000
while (i <= 4999 ) :
    if checkPronic(i) :
        print(i,end=" ")
    i = i + 1
