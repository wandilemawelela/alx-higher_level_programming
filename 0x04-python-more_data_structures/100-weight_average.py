#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        sum = 0
        for sub in my_list:
            for i in sub:
                sum = i * i
        result = sum / len(my_list)
    return result