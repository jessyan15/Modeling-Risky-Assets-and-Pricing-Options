""" 
Use Monte Carlo simulations to estimate the price of European call options and compare with the expected value that's explicitly 
computed explicitly with the Black-Scholes-Merton option pricing formula. Parameters used: T=10,r=0.05,u=1.15,d=1.01,p=.05,S0=50,K=70
where p*=(1+r−d)/(u−d)
""" 
# Import 'comb' module to be used to find probability later 
from scipy.special import comb

# Create a function 'BSM' that uses the Black-Scholes-Merton option pricing formula 
# to explicitly calculate the actual value C0 of the option that yields a payoff at time T

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
