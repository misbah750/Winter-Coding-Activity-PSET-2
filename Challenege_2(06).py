def maximize_freelance_profit(deadlines, profits):
    jobs = list(zip(deadlines, profits))
    jobs.sort(key=lambda x: x[1], reverse=True)
    max_deadline = max(deadlines)
    slots = [False] * (max_deadline + 1)  
    total_jobs = 0
    total_profit = 0
    for deadline, profit in jobs:
        for t in range(deadline, 0, -1):
            if not slots[t]:
                slots[t] = True
                total_jobs += 1
                total_profit += profit
                break  
    return [total_jobs, total_profit]

# Test cases
print("Test 1 Basic example:")
print(maximize_freelance_profit([2, 1, 2, 1, 3], [100, 19, 27, 25, 15]))  

print("\nTest 2  No conflicts:")
print(maximize_freelance_profit([1, 2, 3], [50, 60, 70]))  

print("\nTest 3  All same deadline:")
print(maximize_freelance_profit([1, 1, 1, 1], [10, 20, 30, 40]))  

print("\nTest 4  Single job:")
print(maximize_freelance_profit([1], [100]))  

print("\nTest 5  Two jobs, same deadline:")
print(maximize_freelance_profit([2, 2], [50, 100]))  


