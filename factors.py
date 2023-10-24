import sys

# Function to factorize a number into two smaller numbers
def factorize(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return i, number // i
    return number, 1

# Main function to read the input file and factorize numbers
def factor_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                number = int(line.strip())
                factors = factorize(number)
                print(f"{number}={factors[0]}*{factors[1]}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factor_numbers(file_path)

