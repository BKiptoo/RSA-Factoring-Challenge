import sys
import random

# Function to find the greatest common divisor of two numbers using Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to perform Pollard's Rho factorization
def pollards_rho(n):
    if n <= 1:
        return [n]

    factors = []
    while n > 1:
        x = random.randint(1, n - 1)
        y = x
        c = random.randint(1, n - 1)
        d = 1
        while d == 1:
            x = (x**2 + c) % n
            y = (y**2 + c) % n
            y = (y**2 + c) % n
            d = gcd(abs(x - y), n)

        if d == n:
            factors.append(n)
            break
        else:
            factors.append(d)
            n //= d

    return factors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <number>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        factors = pollards_rho(n)
        factors.sort()

        if len(factors) == 1:
            print(f"{n} is prime.")
        else:
            factors_str = " * ".join(map(str, factors))
            print(f"{n} = {factors_str}")
    except ValueError:
        print("Invalid input. Please provide a valid positive integer.")


