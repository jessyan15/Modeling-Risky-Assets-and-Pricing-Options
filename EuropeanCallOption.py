'''
Price the European call option using Monte Carlo Simulations and the Black-Scholes-Merton 
option pricing formula. Parameters used: T=10,r=0.05,u=1.15,d=1.01,p=.05,S0=50,K=7, 
where p*=(1+r−d)/(u−d)
''' 

# Import 'comb' module to be used to find probability later 
from scipy.special import comb

# This function 'BSM' uses the Black-Scholes-Merton option pricing formula to explicitly
# calculate the actual value C0 of the European call option that yields a payoff at time T.

def BSM(T, r, u, d, S, K):
    # Initialize variables 
    discount = 1/(1+r)**T
    total = 0
    p_star = (1+r-d)/(u-d)
    
    # Use for loop to iterate T times 
    for k in range(1,T+1):
        # Find the number of combinations of T things taken k at a time and exact 
        # long integer is computed. This will be used later to calculate Ct 
        prob = comb(T, k, exact = True) 
        # Calculate a potential payoff which is the difference between the stock price  
        # over time and the fixed strike price 'K' and expiration date n=T 
        payoff = (((u**k)*(d**(T-k))*S)-K)
        # To find the options of the stock, find the max of the payoff. If payoff is 
        # positive, that means the owner of such an option is 'in the money' at 
        # time T. A negative Ct is equivalent to the payoff being 0.
        if payoff > 0:
            payoff
        else:
            payoff = 0
        # Calculate the expected value E*(Ct) where Ct is the payoff and sum them together 
        expected = prob*(p_star**k)*((1-p_star)**(T-k))*payoff
        total += expected
    # Multiply the sum of the values by a discount factor to find the present value 
    C0 = discount * total  
    return C0

# Call function
BSM(T=10, r=.05, u=1.15, d=1.01, S=50, K=70)

# This function uses Monte Carlo simulations to determine the actual value C0 
# of the European call option 
def Monte_Carlo(n, T, r, S, u, d, K):
    # Initialize variables 
    p_star = (1+r-d)/(u-d)
    discount = 1/(1+r)**T
    total = 0
    
    # Create variable B to contain all the binomial distributions that will be used later
    # to find St 
    B = np.random.binomial(T, p_star, n)
    
    # Iterate through each value of 'B' where 'k' indicates the number of successes and 
    # 'T-k' indicates the number of failures 
    for k in B:
        # Calculate the stock price St at any fixed time using binomial probability 
        St = (u**k)*(d**(T-k))*S
        # To find the European Call Option, the payoff is the difference between 
        # the stock value at T - the fixed strike price 
        payoff = St-K
        # Create variable 'Ct' that represents the payoff from the option at time T. 
        # If Ct is positive, that means the owner of such an option is 'in the money' at 
        # time T. A negative Ct is equivalent to the payoff being 0.
        Ct=max(0, payoff)
        
        # To estimate option prices using Monte Carlo Simulations, sum the 'Ct' and 
        # average the values after taking 'n' independent identically distributed copies 
        total += Ct
    average = total/n
    
    # Multiply the average of the values by a discount factor to find the present value 
    C0 = average*discount
    return C0

# Call funtion using different n values          
print("With Monte Carlo simulation when n=100: ", Monte_Carlo(n=100, T=10, r=.05, S=50, u=1.15, d=1.01, K=70))
print("As n increases to 1000: ", Monte_Carlo(n=1000, T=10, r=.05, S=50, u=1.15, d=1.01, K=70))
print("As n increases to 10000: ", Monte_Carlo(n=10000, T=10, r=.05, S=50, u=1.15, d=1.01, K=70))
