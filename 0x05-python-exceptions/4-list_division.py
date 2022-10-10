#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_arr = []
    count = 0
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            count = 1
        except ZeroDivisionError:
            print("division by 0")
            count = 1
        except IndexError:
            print("out of range")
            count = 1

        finally:
            if count:
                count = 0
                new_arr.append(0)
            else:
                new_arr.append(res)
    return new_arr
