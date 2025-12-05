def find_min_max_in_array(array):
    if len(array) == 0:
        raise Exception("Min/max of an empty array is undefined")
    min_index = 0
    max_index = 0

    for i in range(1, len(array)):
        current_value = array[i]

        if current_value < array[min_index]:
            min_index = i
        elif current_value > array[max_index]:
            max_index = i

    result = {
        'min': {'index': min_index, 'value': array[min_index]},
        'max': {'index': max_index, 'value': array[max_index]}
    }

    return result