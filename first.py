def fibonacci_count(n):
    """Generate the first n Fibonacci numbers."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fibonacci_up_to(max_value):
    """Generate Fibonacci numbers up to a maximum value."""
    fib_sequence = []
    a, b = 0, 1
    while a <= max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fibonacci_memoization(n, memo={}):
    """Generate the nth Fibonacci number using memoization."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

# Example usage
while True:
    if __name__ == "__main__":
        print("Fibonacci Generator")
        choice = input("Choose an option:\n1. Generate first n Fibonacci numbers\n2. Generate Fibonacci numbers up to a maximum value\n3. Get nth Fibonacci number using memoization\nEnter choice (1/2/3): ")

        if choice == '1':
            n = int(input("Enter the number of Fibonacci numbers to generate: "))
            print(f"The first {n} Fibonacci numbers are: {fibonacci_count(n)}")
        
        elif choice == '2':
            max_value = int(input("Enter the maximum value for Fibonacci numbers: "))
            print(f"Fibonacci numbers up to {max_value} are: {fibonacci_up_to(max_value)}")
        
        elif choice == '3':
            n = int(input("Enter the position of the Fibonacci number to retrieve: "))
            print(f"The {n}th Fibonacci number is: {fibonacci_memoization(n)}")
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")