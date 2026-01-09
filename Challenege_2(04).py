def count_payment_combinations(coins, total_sum):
    def helper(index, remaining_sum):
        if remaining_sum == 0:
            return 1
        if remaining_sum < 0 or index == len(coins):
            return 0
        take = helper(index, remaining_sum - coins[index])
        skip = helper(index + 1, remaining_sum)
        return take + skip
    return helper(0, total_sum)

# Test cases
print("Test 1  Basic coin change:")
print(count_payment_combinations([1, 2, 5], 5))  

print("\nTest 2  Single coin:")
print(count_payment_combinations([1], 5))  
print(count_payment_combinations([5], 5))  
print(count_payment_combinations([2], 5))  

print("\nTest 3 Target is 0:")
print(count_payment_combinations([1, 2, 5], 0))  
print(count_payment_combinations([], 0))  

print("\nTest 4  Empty coins array:")
print(count_payment_combinations([], 5))  
print(count_payment_combinations([], 10))  
