# your code goes here!
import time

def countdown (i):
    
    while (i <= i and i > 0):
        print (f"{i} SECOND(S)!")
        i -= 1      
    print("HAPPY NEW YEAR!")  
    pass

countdown(10)
def countdown_with_sleep(i):
    while (i <= i and i > 0):
        print (f"{i} SECOND(S)!")
        time.sleep(1)
        i -= 1      
    print("HAPPY NEW YEAR!")  
countdown_with_sleep(5)
     