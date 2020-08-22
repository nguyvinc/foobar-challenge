def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    power = 1
    neg_vals = []
    pos_vals = []
    
    # Check each value in the array and store nonzero values in a new array
    for num in xs:
        if num < 0:
            neg_vals.append(num)
        elif num > 0:
            pos_vals.append(num)
            
    # If there are an odd number of negative values
    if len(neg_vals) % 2 != 0:
        # Sort the negative values
        neg_vals.sort()
        # Remove the last value, which is the least negative value now that it's sorted
        neg_vals.pop()
    
    # Edge case if only value(s) in provided list is/are 0
    if len(pos_vals) == 0 and len(neg_vals) == 0:
        power = 0
    else:
        # Multiply all leftover non-zero values to get the power
        # Only multiply with negative list is there were at least 2 values
        if len(neg_vals) >= 2:
            for num in neg_vals:
                power *= num
        for num in pos_vals:
            power *= num
    
    return str(power)