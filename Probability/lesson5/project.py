from scipy.stats import poisson

expected_rainy_days = 10

prob_12_or_more = 1 - poisson.cdf(11, expected_rainy_days)

prob_between_12_18 = poisson.cdf(18, expected_rainy_days) - poisson.cdf(11, expected_rainy_days)

print(f"Probability of 12 or more days: {prob_12_or_more:.4f}")
print(f"Probability between 12 and 18 days: {prob_between_12_18:.4f}")