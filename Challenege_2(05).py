def min_cancelled_bookings(intervals):
    def is_overlap(a, b):
        return a[1] > b[0] and b[1] > a[0]

    n = len(intervals)
    if n <= 1:
        return 0

    def helper(index, accepted):
        if index == n:
            return 0

        # Option 1: skip current meeting
        skip = 1 + helper(index + 1, accepted)

        # Option 2: accept current meeting if no overlap
        can_accept = True
        for a in accepted:
            if is_overlap(a, intervals[index]):
                can_accept = False
                break

        take = 0
        if can_accept:
            take = helper(index + 1, accepted + [intervals[index]])

        return min(skip, take)

    return helper(0, [])

# Test cases
print("Test 1 No overlaps:")
print(min_cancelled_bookings([[1, 2], [3, 4], [5, 6]])) 

print("\nTest 2  Complete overlap:")
print(min_cancelled_bookings([[1, 5], [2, 4], [3, 6]])) 

print("\nTest 3 Two intervals overlapping:")
print(min_cancelled_bookings([[1, 3], [2, 4]])) 

print("\nTest 4  Empty list:")
print(min_cancelled_bookings([]))  


