def count_ways_to_summit(n: int) -> int:
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    # Recursive case
    return count_ways_to_summit(n - 1) + count_ways_to_summit(n - 2)


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
    
    print("All test cases passed!")


# Run the tests
test_count_ways_to_summit()