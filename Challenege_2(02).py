def can_balance_scales(arr):
    total_sum = sum(arr)
    
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    
    dp = [False] * (target + 1)
    dp[0] = True

    for weight in arr:
        for s in range(target, weight - 1, -1):
            dp[s] = dp[s] or dp[s - weight]
    return dp[target]

# Test cases
print("Test 1 - Basic balanced case:")
print(can_balance_scales([1, 5, 11, 5]))  

print("\nTest 2 - Simple two elements:")
print(can_balance_scales([1, 1]))  
print(can_balance_scales([2, 2]))  

print("\nTest 3 - Odd total sum:")
print(can_balance_scales([1, 2, 4]))  
print(can_balance_scales([1, 1, 1, 1, 1]))  

print("\nTest 4 - Single element:")
print(can_balance_scales([5]))  
print(can_balance_scales([10]))  

print("\nTest 5 - Empty array:")
print(can_balance_scales([]))  