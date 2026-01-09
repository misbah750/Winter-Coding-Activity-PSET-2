def count_ways_to_summit(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    
    # base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Check for already calculated
    if n in memo:
        return memo[n]
    
    # Recursive case with memoization
    memo[n] = count_ways_to_summit(n - 1, memo) + count_ways_to_summit(n - 2, memo)
    return memo[n]


# Test cases
def test_count_ways_to_summit():
    # Base cases
    assert count_ways_to_summit(1) == 1, "Failed: n=1"
    assert count_ways_to_summit(2) == 2, "Failed: n=2"
    
    # Small values
    assert count_ways_to_summit(3) == 3, "Failed: n=3"
    assert count_ways_to_summit(4) == 5, "Failed: n=4"
    assert count_ways_to_summit(5) == 8, "Failed: n=5"
    
    # Larger values
    assert count_ways_to_summit(6) == 13, "Failed: n=6"
    assert count_ways_to_summit(7) == 21, "Failed: n=7"
    assert count_ways_to_summit(10) == 89, "Failed: n=10"
    
    # larger values 
    assert count_ways_to_summit(20) == 10946, "Failed: n=20"
    assert count_ways_to_summit(30) == 1346269, "Failed: n=30"
    
    print("All test cases passed!")



test_count_ways_to_summit()