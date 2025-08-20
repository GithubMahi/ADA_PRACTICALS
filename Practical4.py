import time
def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
def time_analysis():
    n = int(input("Enter a number to calculate factorial: "))
    
    # Test iterative approach
    start_time = time.time()
    result_iter = factorial_iterative(n)
    iter_time = time.time() - start_time
    
    # Test recursive approach
    start_time = time.time()
    result_rec = factorial_recursive(n)
    rec_time = time.time() - start_time
    
    print(f"\nFactorial of {n}:")
    print(f"Iterative result: {result_iter}")
    print(f"Recursive result: {result_rec}")
    
    print("\nTime Analysis:")
    print(f"Iterative approach took {iter_time:.6f} seconds")
    print(f"Recursive approach took {rec_time:.6f} seconds")
    
    # Compare the approaches
    if iter_time < rec_time:
        print("\nIterative approach was faster")
    else:
        print("\nRecursive approach was faster")

if __name__ == "__main__":
    time_analysis()
