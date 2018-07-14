""" 
Price the Asian call option using Monte Carlo Simulations and the Black-Scholes-Merton formula. 
The payoff CT at time T is based on the average value of the stock over T time units.
Use the Binomial Lattice model to generate a random variable that will be used to calculate 
the stock price at time T.
Parameters used: T=10,r=0.05,u=1.15,d=1.01,p=.05,S0=50,K=70, where p*=(1+r−d)/(u−d)
"""
# Import numpy and random modules 
import numpy as np
import random

# This function generates a Y random variable in the Binomial Lattice model. 
# This random variable will be defined by Yn = u if Bn = 1 and Yn = d if Bn = 0.
# This will be used later to calculate the stock price at time T 

def Y(p, u, d):
    # Generate a uniform random variable 'U'
    U = random.random()
    
    # Call the Bernoulli function from problem 1 and return 'u' if the Bernoulli function 
    # returns a '1', indicating success. If Bernoulli returns a '0', return 'd' to 
    # indicate failure 
    if Bernoulli(p):
        return u
    else:
        return d
    
# Create a function that determines the actual value C0 by pricing the Asian call option
def Asian_Call_Option(n, T, r, S, u, d, K):
    p_star = (1+r-d)/(u-d)
    discount = 1/((1+r)**T)
    C=[]
    
    # Set for loop that iterates through n for the Monte Carlo simulation
    for j in range(1, n+1):
        # Initialize an empty array
        path = [0 for i in range(T+1)]
        # Set the first entry to our initial stock value S_0=S0
        path[0] = S
        # Create an empty list to store total of stock prices before averaging them later
        Stotal= []
        
        # Create for loop that iterates T times to find Ct for each nth trial of the 
        # Monte Carlo simulations
        for i in range(1, T+1):
            # Generate a path by sampling from Y one at a time until T+1 to get 
            # BLM sequentially 
            path[i] = path[i-1]*Y(p_star,u,d)
            # This path is equivalent to the stock price on a given day 
            St = path[i]
            # Sum up all the prices and calculate the average over T times  
            Stotal.append(St)
        Saverage = np.average(Stotal)
        
        # For each nth trial, find the payoff which is equal to the difference 
        # between the average value of the stock and the fixed strike price 'K' 
        payoff = Saverage-K
        
        # Set a new variable 'Ct' that represents the payoff from the option at time T. 
        # If Ct is positive, that means the owner of such an option is 'in the money' at 
        # time T. A negative Ct is equivalent to the payoff being 0.
        Ct = max(0, payoff)
        
        # To estimate option prices using Monte Carlo Simulations, sum the 'Ct' and 
        # average the values after taking 'n' independent identically distributed copies 
        C.append(Ct)
    avgC = np.average(C)
    
    # Multiply the average of the values by a discount factor to find the present value 
    C0 = discount * avgC
    return C0

# Call funtion      
print("With Monte Carlo simulation when n=100: ", Asian_Call_Option(n=100, T=10, r=.05, S=50, u=1.15, d=1.01, K=70))
print("As n increases to 1000: ", Asian_Call_Option(n=1000, T=10, r=.05, S=50, u=1.15, d=1.01, K=70))
print("As n increases to 10000: ", Asian_Call_Option(n=10000, T=10, r=.05, S=50, u=1.15, d=1.01, K=70))

