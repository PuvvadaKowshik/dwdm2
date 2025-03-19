# Import necessary library
from scipy.stats import chi2_contingency

# Define the observed data (contingency table)
data = [[207, 282, 241], 
        [234, 242, 232]]

# Perform Chi-Square test
stat, p, dof, expected = chi2_contingency(data)

# Set significance level (alpha)
alpha = 0.05

# Display results
print(f"Chi-Square Statistic: {stat:.4f}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies Table:")
print(expected)
print(f"P-value: {p:.4f}")

# Interpretation based on p-value
if p <= alpha:
    print("Dependent (Reject H0 - Significant relationship exists)")
else:
    print("Independent (H0 holds true - No significant relationship)")
