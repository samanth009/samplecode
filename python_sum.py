def sum_list(a):
    sum_test = 0
    for i in a:
        sum_test += i

    return sum_test


a = [1, 1, 2, 3, 5]
print(sum_list(a))