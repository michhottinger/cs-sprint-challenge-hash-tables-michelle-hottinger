def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #below is the solution if rules did not prohibit set use:
    #result = list(set.intersection(*map(set, arrays)))
    dict_arr = {} #create a dictionary
    result = [] #create a results list of the common numbers
    length = len(arrays)
    #save num in array to the dict so it can be called upon quickly
    for arr in arrays:#for list of lists
        for n in arr:#get number in list
            if n not in dict_arr:#if number isn't in the dict
                dict_arr[n] = 1#put it in at 1
            else:
                dict_arr[n] +=1#if its already in there, increment
                
    for n in dict_arr:#Now look over the dict and if its result is more than one
        if dict_arr[n] == length:#add it to our results lists
            result.append(n)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
