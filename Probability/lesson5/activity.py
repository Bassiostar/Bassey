import scipy.stats as stats
prob = 1 - stats.binom.cdf(6, 10, 0.5)

print("the probability of gettimg more than six heads in 10 coin flips is: ", prob)

Prob1 = stats.poisson.pmf(6, 10)
print("the probability of getting exactly 6 days:", Prob1)

prob2 = stats.poisson.cdf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10) 
print("the probability of raining for 12 - 14  days:", prob2)

Prob1 = 1 - stats.poisson.cdf(20, 15)
print("the probability of getting more than 20 calls:", Prob1)

prob2 = stats.poisson.cdf(21, 15) + stats.poisson.pmf(10, 15)
print("the probability of getting 17 - 21  calls:", prob2)