
# function fibonacci will return the value at the position passed as argument
def fibonacci(n):
    # Fibonacci series always starts with number 0
    if n==0: 
        return 0     
    # Second number in the Fibonacci series always be number 1
    elif n==1: 
        return 1
    # Third number in the Fibonacci series will be the sum of previous 2 numbers and the sequence continues on.
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 

# function lucas will return the value at the position passed as argument
def lucas(n):
    # Lucas series always starts with number 2
    if n==0:
        return 2
    # Second number in the Lucas series always be number 1
    elif n==1:
        return 1
     # Third number in the Lucas series will be the sum of previous 2 numbers and the sequence continues on.
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(a,b=0,c=1):
    # Based on the optioinal parameter this function calls either fibonacci or lucas or return the new series
    if b==0 and c==1:
        # If value b & c not passed then call the fibonacci method and return the value
        return fibonacci(a)
    elif b==2 and c==1:
        # If value b & c passed as 2 & 1 respectively then call the lucas method and return the value
        return lucas(a)
    else:
        # If none of the above values matched for b & c then form a new series based on b & c
        if a==0:
            # Return the value as b
            return b        
        elif a==1:
            # Return the value as c
            return c        
        else:
            # Return the sum of previous 2 immediate values of b & c
            return sum_series(a-1,b,c) + sum_series(a-2,b,c)
