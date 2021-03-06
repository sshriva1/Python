#Sourav Shrivastava
#Bowling_Kata.py
#Kent State University
#810836263

import math
import random

final_score = 0

#Game Class defined
class Game():
    def __init__(self):                   
        return
 
    def __score__(self,a,b):            #Calculation if neither spare nor strike           
        return a+b
    
    def __spare__(self,a,b,c):          #Calculation if it's a spare              
        return a+b+c
    
    def __strike__(self,a,c,d):         #Calculation if it's a strike
        return a+c+d
        

        
#Game Class Calling inside the function
def submain(a,b,c,d):
    myVector = Game()
    global final_score
    if a == 10:                         #It's a Strike
            z = myVector.__strike__(a,c,d) 
            final_score = final_score + z
            print final_score
            
    elif ((a != 10) and (a+b == 10)):    #It's a Spare
            z = myVector.__spare__(a,b,c)
            final_score = final_score + z
            print final_score
    else:
        z = myVector.__score__(a,b)         #Neither a Strike nor Spare 
        final_score = final_score + z
        print final_score

#Main Function is called to loop the frame for 10 times. If it's 10th frame it can accept 3 valid rolls value.
def main():
    a=[]
    b=[]
    j=0
    for frame in range(10):
        if frame == 9:          #Final Frame Value
            print "\nWarning ! Use the third score if applicable in this final frame, if not enter Zero in digits:"
            f1=int(input("Please Enter the first score of your final frame:   "))
            f2=int(input("Please Enter the second score of your final frame:  "))
            f3=int(input("Enter the third number, if not applicable it will be considered as zero: "))

            if (f1 > 10 or f2 > 10 or f3 > 10):
                print " You Entered a wrong Value1"
                quit()
            
            if  (f1 != 10):
                if f1+f2 > 10:
                    print " You Entered a wrong Value2"
                    quit()
                elif (f1+f2 == 10):
                    a.append(f1)
                    a.append(f2)
                    a.append(f3)
                else:
                    f3 = 0
                    a.append(f1)
                    a.append(f2)                    
                    a.append(f3)
            else: 
                if (f2 != 10) and f2+f3 > 10:
                    print " You Entered a wrong Value3"
                    quit()
                else:
                    a.append(f1)
                    a.append(f2)                    
                    a.append(f3)

            a.append(j)
            a.append(j)

        else:
            f1=int(input("Enter the First Bowling score in digits:   "))
            f2=int(input("Enter the Second Bowling score in digits:  "))
            if (f1+f2 > 10):
                print " You Entered a wrong Value"
                quit()
            else:
                a.append(f1)
                a.append(f2)

                
        print a[0:21]

    #Calling Submain function to calculate score based on strike or spare or simple score in bowling
    for i in range(0,20,2):
        x = a[i]
        y = a[i+1]
        m = a[i+2]
        n = a[i+3]        
        submain(x,y,m,n)
    global final_score
    print "\nYour Final Score is: " + str(final_score)
        
main()
