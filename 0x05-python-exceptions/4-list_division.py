#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    x = list_length
    for i in range(0, x):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            result.append(res)
    return result
