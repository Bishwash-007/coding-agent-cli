def fibonacci_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        total_sum = 1  # Start with 1 because the first Fibonacci number is 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            total_sum += b
        return total_sum

if __name__ == "__main__":
    # Example usage: Calculate the sum of the first 10 Fibonacci numbers
    n = 10
    result = fibonacci_sum(n)
    print(f"The sum of the first {n} Fibonacci numbers is: {result}")
