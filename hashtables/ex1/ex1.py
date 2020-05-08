def get_indices_of_item_weights(weights, length, limit):

    weights_dict = dict()

    for i in range(length):
        y = weights_dict.get(limit - weights[i])
        if y != None:
            return (i, y)
        else:
            weights_dict[weights[i]] = i
    
    print(weights_dict)
    return None
