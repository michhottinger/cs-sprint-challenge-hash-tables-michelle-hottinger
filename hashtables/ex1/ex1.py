



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
            hash[i + 1] = limit - i

    for i in hash:#loop through i and j in hash to see if they sum to limit
        for j in hash:
            if hash[i] + hash[j] == limit and i != j:
                #return the correct format which is index keys j and i
                return list(hash.keys()).index(j), list(hash.keys()).index(i)
    else:
        return None




def get_indices_of_item_weights_fast(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}#start with the empty dict
    for idx, weight in enumerate(weights):#weight is key, idx is value
        #enumerate increases idx
        #saves time to look up weights/values and get back idx
        if weight not in hash:
            hash[weight] = [idx]#put weight into hash with new idx
        else:
            hash[weight].append(idx)

    for idx, weight in enumerate(weights):
        rest_weight = limit - weight
        if rest_weight in hash:
            for rest_idx in hash[rest_weight]:
                if idx != rest_idx:
                    if idx > rest_idx:
                        return idx, rest_idx
                    else:
                        return rest_idx, idx

    return None


def get_indices_of_item_weights_normal(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    rest_weight = limit - weight
    for idx, weight in enumerate(weights):
        for rest_idx, rest_weight in enumerate(weights):
            if rest_idx > idx and weight + rest_weight == limit:
                return rest_idx, idx

    return None
