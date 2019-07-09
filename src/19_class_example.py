def centered_average_1(arr):
    highest = 0
    lowest = 0
    total = 0

    for i in arr:
        if i < lowest:
            lowest = i
        if i > highest:
            highest = i
        total += i

    total -= highest
    total -= lowest
    return total // (len(arr) - 2)


print(centered_average_1([1, 6, 2, 9, 4, 3, 8, 4, 10]))


def centered_average_2(arr):
    arr.sort()
    temp_array = arr[1:-1]
    # total = 0
    # for i in arr:
    #     total += i
    # return total // len(temp_arr)
    return sum(temp_array) // len(temp_array)


centered_average_2([1, 6, 2, 9, 4, 3, 8, 4, 10])
print(centered_average_2([1, 6, 2, 9, 4, 3, 8, 4, 10]))
