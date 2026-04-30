import numpy as np
import matplotlib.pyplot as plt

# 1. Create a non-normal (Exponential) population
# Most values are small, with a few very large ones (highly skewed)
population = np.random.exponential(scale=1.0, size=100000)

sample_sizes = [2, 5, 10, 30]
num_samples = 5000

fig, axes = plt.subplots(1, len(sample_sizes) + 1, figsize=(20, 4))

# Plot the original skewed population
axes[0].hist(population, bins=50, color='gray', alpha=0.7)
axes[0].set_title("Original Population\n(Highly Skewed)")

# 2. Demonstrate CLT by taking sample means
for i, n in enumerate(sample_sizes):
    # Calculate the mean of 'n' random picks, repeated 5000 times
    sample_means = [np.mean(np.random.choice(population, n)) for _ in range(num_samples)]
    
    # Plot the distribution of these means
    axes[i+1].hist(sample_means, bins=50, color='skyblue', edgecolor='white')
    axes[i+1].set_title(f"Sample Means\n(Sample Size n={n})")

plt.tight_layout()
plt.show()