def can_balance_scales(arr):
    total_sum = sum(arr)
    # If total sum is odd  we cannot split it evenly
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    def dfs(index, current_sum):
        # success case
        if current_sum == target:
            return True
        # failure cases
        if index == len(arr) or current_sum > target:
            return False
        
        if dfs(index + 1, current_sum + arr[index]):
            return True
        return dfs(index + 1, current_sum)
    return dfs(0, 0)

# Test cases
print("Test 1 - Basic balanced case:")
print(can_balance_scales([1, 5, 11, 5]))  

print("\nTest 2 - Simple two elements:")
print(can_balance_scales([1, 1]))  

print("\nTest 3 - Odd total sum:")
print(can_balance_scales([1, 2, 3]))  
print(can_balance_scales([1, 2, 4]))  

print("\nTest 4 - Single element:")
print(can_balance_scales([5]))  

print("\nTest 5 - Empty array:")
print(can_balance_scales([]))  