# Modeling-Risky-Assets-and-Pricing-Options
I developed algorithms that use Monte Carlo Simulations, the Black-Scholes-Merton model, and the Binomial Lattice model to compute prices of European, Asian, Down-and-Out-Barrier call options

To find the down and out barrier option, I implemented the same concept used to find the Asian call option. However, for this particular option, the payoff is determined with an additional given fixed barrier constant 'b' which is greater than 0. With a given fixed i times in which 0<n1<n2<...<ni<T, the payoff at time T is determined by subtracting the fixed strike price 'K' from the value of the stock over the time period 'St' and multiplying it by the indicator random variable 'I'. This indicator random variable is actually just a Bernoulli(p) random variable that uses the same concept as the Bernoulli function in problem 1. In this case, the limits of what defines a success (where I{A} = 1) is the barrier constant. The 'I' function in the code below codes for this Bernoulli random variable. In my code, the 'indicator' variable is created to store the values from the 'I' function. To find the payoff Ct, it requires that the stock is above the barrier level at all specified times ni (in this case, it is n1=4 and n2=6). If the stock is below the barrier, then I{A} (where the probability of A denotes that whether stock is above the barrier, indicating a success) would equal 0, indicating that the option is knocked out and becomes worthless. This is implemented in my code with the max function that is multiplied by the indicator variable (same concept used finding the option in problems 2 and 3). Once Ct is found, I continue with the same code as the previous problems to determine the present value C0 using Monte Carlo simulations.
