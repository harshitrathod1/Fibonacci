#print fib series upto n terms
def fib(n):
    #IF THE INPUT NUMBER IS LESS THAN 1
    if n<1:
        print("INCORRECT INPUT")
    #IF THE INPUT NUMBER IS GREATER OR EQUAL TO 1
    else:
        f=1 #first number
        s=1 #second number
        print(f,s,end=" ") #printing(1,1) of series
        for i in range(2,n):  
            next=f+s  
            print(next,end=" ")
            f,s=s,next #swapping and updating next
