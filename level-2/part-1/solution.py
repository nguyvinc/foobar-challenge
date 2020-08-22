def solution(xs):
    # I guess at least one value from the array must be used
    if len(xs) == 1:
        return str(xs[0])
    
    # Flag in case no multiplication occurs
    zero = 1
    power = 1
    neg = 0
    
    # Count negative numbers in array
    for num in xs:
        if num < 0:
            neg += 1
    # If the number of negative values is odd, subtract 1 or result will be negative
    if neg % 2 == 1:
        neg -= 1
    
    # Sort the array
    xs.sort()
    # Iterate through sorted array
    for num in xs:
        # Multiply power by negative values, will multiply by most negative values
        #   Since array is sorted, the negative counter condition will ignore the least negative value
        if num < 0 and neg > 0:
            power *= num
            neg -= 1
            zero = 0
        # Multiply power by all positive values
        elif num > 0:
            power *= num
            zero = 0
    # If no multiplication occurred, power is 0
    if zero == 1:
        power = 0
        
    return str(power)