def solution(data, n): 
    occurences = {}
    remove = {}
    new_list = []
    # Count number of occurences for each number in list
    for value in data:
        if str(value) in occurences:
            occurences[str(value)] = occurences[str(value)] + 1
        else:
            occurences[str(value)] = 1
            
    # Check occurences for each number in the list, add to remove if greater than n
    for value, occur in occurences.items():
        if occur > n:
            remove[str(value)] = value
            
    # Remove numbers from the list
    for value in data:
        if not str(value) in remove:
            new_list.append(value)
            
    return new_list