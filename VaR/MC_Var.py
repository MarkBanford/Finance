'''In this example, the monte_carlo_var function takes as input a list of returns, a confidence level
(expressed as a percentage), and the number of simulations to run. It generates random returns using Monte Carlo
simulation, calculates the minimum portfolio value for each simulation, and then computes the VaR at the specified
confidence level using the numpy.percentile function. The function returns the VaR as a floating point value.
In the example usage, the function is called with a list of returns, a confidence level of 95%, and a number of
simulations of 10000. The resulting VaR is printed to the console.'''

import numpy as np


def monte_carlo_var(returns, confidence_level, num_simulations):
    """
    Computes VaR using Monte Carlo simulation.
    Returns: VaR (float)
    """
    # Generate random returns using Monte Carlo simulation
    simulated_returns = np.random.normal(np.mean(returns), np.std(returns), [num_simulations, len(returns)])

    # Calculate the portfolio value for each simulation
    simulated_prices = (simulated_returns + 1).cumprod(axis=1)
    simulated_prices = np.insert(simulated_prices, 0, 1, axis=1)

    # Calculate the minimum portfolio value for each simulation
    min_simulated_prices = simulated_prices.min(axis=1)

    # Compute the VaR at the specified confidence level
    var = np.percentile(min_simulated_prices, 100 - confidence_level)

    return var


# Example usage
returns = [0.1, 0.2, 0.15, -0.05]
confidence_level = 95
num_simulations = 10000

var = monte_carlo_var(returns, confidence_level, num_simulations)
print(f'VaR at {confidence_level}% confidence level: {var:.2f}')
