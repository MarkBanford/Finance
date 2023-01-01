'''

To bootstrap a yield curve using Python, we must do the following steps

1. Define a function bootstrap_yield_curve that takes in the following parameters:
maturities: a list of maturities (in years) for the yield curve
yields: a list of yields (as percentages) for the yield curve

2. Inside the function, create a list rates to store the bootstrapped rates

3. Sort the maturities and yields lists in ascending order by maturity

4. append the first element of the yields list to the rates list

5. Iterate over the remaining elements in the maturities and yields lists (using a for loop). For each element,
do the following:
  Calculate the rate for the element using the following formula:
    rate = (yields[i] + rates[-1]) / (1 + maturities[i])
    where rates[-1] is the last element in the rates list and maturities[i] is the current maturity
    Append the rate to the rates list

6. Return the rates list


'''


def bootstrap_yield_curve(maturities, yields):
    rates = []
    maturities, yields = zip(*sorted(zip(maturities, yields)))
    rates.append(yields[0])
    for i in range(1, len(maturities)):
        rate = (yields[i] + rates[-1]) / (1 + maturities[i])
        rates.append(rate)
    return rates


maturities = [0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00]
yields = [0.06, 0.065, 0.07, 0.078, 0.08, 0.084, 0.088, 0.091, 0.096, 0.099, 0.104, 0.108]

print(bootstrap_yield_curve(maturities, yields))
