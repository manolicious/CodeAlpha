import csv

def fibonacci(n):
    """
    Generate the first n Fibonacci numbers
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def write_to_csv(fib_sequence, filename):
    """
    Write the Fibonacci sequence to a CSV file
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Fibonacci Number", "Value"])
        for i, value in enumerate(fib_sequence):
            writer.writerow([i, value])

def read_from_csv(filename):
    """
    Read the Fibonacci sequence from a CSV file
    """
    fib_sequence = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            fib_sequence.append(int(row[1]))
    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fib_sequence = fibonacci(n)

write_to_csv(fib_sequence, 'fibonacci_data.csv')

read_fib_sequence = read_from_csv('fibonacci_data.csv')

print("Fibonacci Sequence:")
print(read_fib_sequence)