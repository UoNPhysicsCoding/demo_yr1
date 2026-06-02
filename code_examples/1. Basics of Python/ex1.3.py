import numpy as np
import matplotlib.pyplot as plt
#  The warning triangle appears because although we have imported the package
#  as plt, we haven't actually used it within this section of the code.
y = np.sin(1.2)
#  importing modules 'numpy' and 'matplotlib.pyplot' as np and plt respectively
#%% 
import numpy
import matplotlib.pyplot
#  importing modules 'numpy' and 'matplotlib.pyplot' wihtout assigning
#  name. Would be required to write full module name for use. e.g. numpy.sin
#  for use of sine function.
#%%
from numpy import sin, cos, tan
y = sin(1.2)
x = cos(1.2)
z = tan(1.2)
#  importanting one or more functions from a package. Generally not used as
#  it makes it hard to read code.
#%% 
import numpy as np
from scipy import special 
x = special.factorial(np.arange(1,11))

def get_primes_up_to(n):
    """Returns a list of prime numbers up to n."""
    if n < 2:
        return []
    
    # Create a boolean list "is_prime" and initialize all entries to True
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Sieve of Eratosthenes
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            # Mark multiples of p as False
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
                
    # Collect all numbers that remain True
    return [p for p in range(2, n + 1) if is_prime[p]]

# Calculate and print primes up to 100
primes = get_primes_up_to(100)
print(primes)