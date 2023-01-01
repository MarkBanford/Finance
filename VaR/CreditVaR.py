'''Here is an example of Python code that uses Monte Carlo simulation to compute the credit risk of a portfolio of loans
This code generates random default probabilities, recovery rates, and loan values for a portfolio of 100 loans.
It then runs 10,000 simulations to calculate the expected loss and risk for the portfolio. In each simulation,
it determines which loans default based on the default probabilities, calculates the total loss for the simulation,
and stores the result in an array. Finally, it calculates the expected loss and risk by taking the mean and
standard deviation of the results array.
'''

import numpy as np

# Number of simulations
num_sims = 100000

# Number of loans in the portfolio
num_loans = 100

# Probability of default for each loan
default_probs = np.random.uniform(0, 1, size=num_loans)

# Recovery rate for each loan (percentage of the loan value that will be recovered in the event of default)
recovery_rates = np.random.uniform(0, 1, size=num_loans)

# Loan values
loan_values = np.random.uniform(1000, 10000, size=num_loans)

# Initialize array to store the results of each simulation
results = np.zeros(num_sims)

# Loop through each simulation
for i in range(num_sims):
    # Determine which loans default in this simulation
    defaults = np.random.uniform(0, 1, size=num_loans) < default_probs

    # Calculate the total loss for this simulation
    loss = np.sum(loan_values[defaults] * (1 - recovery_rates[defaults]))

    # Store the result in the results array
    results[i] = loss

# Calculate the expected loss (mean of the results array)
expected_loss = np.mean(results)

# Calculate the standard deviation of the results (a measure of risk)
risk = np.std(results)

# Print the results
print("Expected loss: ", expected_loss)
print("Risk: ", risk)
