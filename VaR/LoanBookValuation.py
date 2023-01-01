'''Monte Carlo simulation to compute the estimated loss on a book of loans that have known default probabilities
and recovery rates

1. Define a function monte_carlo_loss that takes in the following parameters:
default_prob: a list of default probabilities for each loan in the book
recovery_rate: a list of recovery rates for each loan in the book
principal: a list of principal amounts for each loan in the book
num_samples: the number of samples to use in the Monte Carlo simulation

2. Inside the function, create a variable loss initialized to 0

3. Use a for loop to perform the Monte Carlo simulation num_samples times. For each iteration of the loop, do the
following:
Generate a random number between 0 and 1 for each loan in the book. If the random number is less than the default
probability for the loan, set the default status for the loan to 1 (defaulted), otherwise set it to 0 (not defaulted).
Calculate the loss for the book of loans using the following formula:
loss = sum(default_status[i] * (principal[i] * (1 - recovery_rate[i])) for i in range(len(default_prob)))
Add the loss for the book of loans to the loss variable

4. After the for loop, divide the loss variable by num_samples to get the average loss across all samples


5. Return the average loss

'''

import random


def monte_carlo_loss(default_prob, recovery_rate, principal, num_samples):
    loss = 0
    for i in range(num_samples):
        default_status = [1 if random.random() < default_prob[j] else 0 for j in range(len(default_prob))]
        loss += sum(default_status[i] * (principal[i] * (1 - recovery_rate[i])) for i in range(len(default_prob)))
    return loss / num_samples


default_prob = [0.2, 0.3, 0.4]
recovery_rate = [0.4, 0.4, 0.4]
principal = [1000000, 8000000, 6000000]
num_samples = 10000

print(monte_carlo_loss(default_prob=default_prob, recovery_rate=recovery_rate, principal=principal,
                       num_samples=num_samples))
