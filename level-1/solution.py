def solution(data, n): 
    occurences = {}
    remove = {}
    new_list = []
    
    # Count number of occurences for each number in list
    for value in data:
        if str(value) in occurences:    # If key already exists, increment occurrence
            occurences[str(value)] = occurences[str(value)] + 1
        else:                           # Else add key, set to 1
            occurences[str(value)] = 1
            
    # Check occurences for each number in the list, add to remove if greater than n
    for value, occur in occurences.items():
        if occur > n:
            remove[str(value)] = 1
            
    # Copy over non-removed numbers to new list
    for value in data:
        if not str(value) in remove:    # If value is not in remove, add to new list
            new_list.append(value)
            
    return new_list
