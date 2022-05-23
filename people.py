
#create a function
#pass in a parameter
#Request user for input
#condition the input if divisible by 2 and 3
#Display 
def divisible(numb):
    numb=int("Enter a number ")
    if ((numb%2==0) and (numb%3==0)):
        print("Number is divisible by both 3 and 2")
    elif((numb%3==0) and(numb%2!=0)):
        print("This number is divisible by 3")
    elif(numb==0):
        print("O is not divisible by 2 and three")
        
                                                      #does not cover 3 and zero as an integer
    