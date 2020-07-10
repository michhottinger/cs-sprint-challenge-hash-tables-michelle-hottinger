



def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}
    for i in weights:#put weights values into hash table if not already there
        if i not in hash:
            hash[i] = limit - i
        else:
            hash[f'{i + 1}'] = limit - i
     
    for i in hash:#loop through i and j in hash to see if they sum to limit
        for j in hash:
            if hash[i] + hash[j] == limit and i != j:
                #return the correct format which is index keys j and i
                return list(hash.keys()).index(j), list(hash.keys()).index(i)
    else:
        return None
