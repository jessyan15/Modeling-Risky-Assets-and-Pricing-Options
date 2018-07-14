"""
Price a down and out barrier option that has payoff at time T
Parameters used: T=10,r=0.05,u=1.15,d=1.01,p=.05,S0=50,K=70,n1=4,n2=6,b=66
"""
# Import numpy and random modules 
import numpy as np
import random

# Create a function for the 'I' variable that demotes the indicator random variable 
# which uses the same concept as the Bernoulli random variable in which p = P(A) 
# gives the probability that the event A occurs: 1 = A occurs, 0 = A doesn't occur

def I(Sn1, Sn2, b):
    I = random.random()
    if (Sn1>=b and Sn2>=b):
        return 1
    else: 
        return 0  
       
# Create a function that determines the actual value C0 by pricing the down and 
# out barrier call option  
def barrier(n, T, r, S, u, d, K, n1, n2, b):
    # Initialize variables 
    p_star = (1+r-d)/(u-d)
    discount = 1/((1+r)**T)
    total = 0
    C= []    
    
    # Set for loop that iterates through n for the Monte Carlo simulation
    for j in range(1, n+1):
        # Initialize an empty array
        path = [0 for i in range(T+1)]
        # Set the first entry to our initial stock value S_0=S0
        path[0] = S
        
        # Create for loop that iterates through T only to find Ct for each time the outer
        # loop iterates through 'B'
        for i in range(1, T+1):
            # Generate a path by sampling from Y one at a time until T+1 to get 
            # BLM sequentially 
            path[i] = path[i-1]*Y(p_star,u,d)
            St = path[i]
        # Create variables to check later if stock at a specific time (n1, n2) is above 
        # the fixed barrier constant 'b'
        Sn1 = path[n1]
        Sn2 = path[n2]
        
        # Call the 'I' function 
        indicator = int(I(Sn1, Sn2, b))
        
        # Create a variable 'Ct' that represents the payoff from the option at time T that 
        # accounts for an additional given fixed barrier constant b>0.
        # If Ct is positive, that means the owner of such an option is 'in the money' at 
        # time T. A negative Ct is equivalent to the payoff being 0.
        Ct = max(St-K, 0)*indicator
        
        # To estimate option prices using Monte Carlo Simulations, sum the 'Ct' and 
        # average the values after taking 'n' independent identically distributed copies 
        C.append(Ct)
    avgC = np.average(C)
     
    # Multiply the average of the values by a discount factor to find the present value 
    C0 = discount * avgC
    return C0

# Call function
print("With Monte Carlo simulation when n=100: ", barrier(n=100, T=10, r=.05, S=50, u=1.15, d=1.01, K=70, n1=4, n2=6, b=66))
print("As n increases to 1000: ", barrier(n=1000, T=10, r=.05, S=50, u=1.15, d=1.01, K=70, n1=4, n2=6, b=66))
print("As n increases to 10000: ", barrier(n=10000, T=10, r=.05, S=50, u=1.15, d=1.01, K=70, n1=4, n2=6, b=66)) 
