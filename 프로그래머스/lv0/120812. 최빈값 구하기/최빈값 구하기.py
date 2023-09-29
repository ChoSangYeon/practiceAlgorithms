def solution(array):
    counts = {}
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    max_count = max(counts.values())

    most_common_values = []
    for key, value in counts.items():
        if value == max_count:
            most_common_values.append(key)

    if len(most_common_values) == 1:
        return most_common_values[0]
    else:
        return -1