def has_negatives(a):

    num_dict = dict()
    result = list()

    for num in a:
        if num_dict.get(abs(num)):
            if (num_dict.get(abs(num)) + num) == 0:
                result.append(abs(num))
        else:
            num_dict[abs(num)] = num 


    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
