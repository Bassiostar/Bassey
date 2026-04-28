from scipy.stats import binom

# Parameters
n = 10  # Number of trials
p = 0.5 # Probability of success (heads)

# Calculate P(X=2) + P(X=3) + P(X=4)
# We can sum the Probability Mass Function (PMF) for k = 2, 3, 4
probability = sum(binom.pmf(k, n, p) for k in [2, 3, 4])

print(f"The probability of observing between 2 and 4 heads is: {probability:.4f}")